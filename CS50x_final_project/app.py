import os
from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename
from PIL import Image
import numpy as np
import zipfile


app = Flask(__name__)

# Helper function to shuffle pixels


def shuffle_pixels(arr, key):
    h, w, c = arr.shape
    flat = arr.reshape(-1, c)
    np.random.seed(key)
    perm = np.random.permutation(len(flat))
    shuffled = flat[perm]
    return shuffled.reshape(h, w, c), perm
# Helper function to unshuffle pixles


def unshuffle_pixels(arr, perm):
    h, w, c = arr.shape
    flat = arr.reshape(-1, c)
    unshuffled = np.zeros_like(flat)
    unshuffled[perm] = flat
    return unshuffled.reshape(h, w, c)


@app.route("/")
def index():
    return render_template("index.html", title="IMAGE LOCKER")


@app.route("/encrypt", methods=["POST"])
def encrypt():
    # Installing and saving the image safely
    if not ("image" in request.files and "key" in request.form and "confirmation" in request.form):
        return render_template("index.html",title="IMAGE LOCKER",error="Missing Image and/or Key!")

    image = request.files["image"]
    try:
        key = int(request.form["key"])
        confirmation = int(request.form["confirmation"])
        if key < 0 or confirmation < 0:
            raise ValueError
    except (ValueError):
        return "Enter a Valid Key/Confirmation!"
    if not (key == confirmation):
        return render_template("index.html", title="IMAGE LOCKER", error="Confirmation Failed!")

    filename = secure_filename(image.filename)
    upload_path = os.path.join("uploads", filename)
    image.save(upload_path)

    img = Image.open(upload_path)
    arr = np.array(img)

    shuffled_arr, perm = shuffle_pixels(arr, key)
    encrypted_arr = shuffled_arr ^ key
    encrypted_img = Image.fromarray(encrypted_arr.astype("uint8"))
    output_name = f"{os.path.splitext(filename)[0]}_Yenc.png"
    output_path = os.path.join("encrypted", output_name)
    encrypted_img.save(output_path)

    # saving the permutation
    perm_path = os.path.join("encrypted", f"{os.path.splitext(output_name)[0]}_perm.npy")
    np.save(perm_path, perm)

    zip_name = f"{os.path.splitext(filename)[0]}_bundle.zip"
    zip_path = os.path.join("encrypted", zip_name)
    with zipfile.ZipFile(zip_path, "w") as zf:
        zf.write(output_path, arcname=output_name)
        zf.write(perm_path, arcname=os.path.basename(perm_path))

    return send_file(zip_path, as_attachment=True)


@app.route("/decrypt", methods=["POST"])
def decrypt():
    if not ("image" in request.files and "key" in request.form and "confirmation" in request.form):
        return render_template("index.html", title="IMAGE LOCKER", error="Missing Image and/or Key!")
    zip_file = request.files["image"]
    try:
        key = int(request.form["key"])
        confirmation = int(request.form["confirmation"])
        if key < 0 or confirmation < 0:
            raise ValueError
    except ValueError:
        return render_template("index.html", title="IMAGE LOCKER", error="Enter a Valid Key/Confirmation!")
    if key != confirmation:
        return render_template("index.html",title="IMAGE LOCKER",error="Confirmation Failed!")
    filename = secure_filename(zip_file.filename)
    upload_path = os.path.join("uploads", filename)
    zip_file.save(upload_path)

    with zipfile.ZipFile(upload_path, "r") as zf:
        zf.extractall("uploads")

        encrypted_img_name = [f for f in zf.namelist() if f.endswith("Yenc.png")][0]
        perm_file_name = [f for f in zf.namelist() if f.endswith("_perm.npy")][0]

    img = Image.open(os.path.join("uploads", encrypted_img_name))
    arr = np.array(img)
    perm_path = os.path.join("uploads", perm_file_name)

    if not os.path.exists(perm_path):
        return "Permutation file not found!"
    perm = np.load(perm_path)

    decrypted_arr = arr ^ key
    unshuffled_arr = unshuffle_pixels(decrypted_arr, perm)
    decrypted_img = Image.fromarray(unshuffled_arr.astype('uint8'))
    output_name = f"{os.path.splitext(encrypted_img_name)[0]}_Ydec.png"
    output_path = os.path.join("decrypted", output_name)
    decrypted_img.save(output_path)

    return send_file(output_path, as_attachment=True)
