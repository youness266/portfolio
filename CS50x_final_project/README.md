# YOUR PROJECT TITLE
#### Video Demo:  <https://youtu.be/7lOO94hYNs4>
#### Description:
Introduction:
This project is called Image Locker. It is my final project for CS50x. The goal of the project is to take an image, scramble it so that it cannot be understood, and then allow the user to restore it if they know the correct key. In simple terms, it is an image encryption and decryption web application. The app is built using Flask (Python) for the backend, and it uses HTML/CSS for the frontend. The encryption logic is based on pixel shuffling and XOR operations.

The inspiration for this project came from two problem sets in CS50:

The Caesar cipher problem set in C, where we learned how to shift letters in text using a key.

The Filter (image) problem set in C, where we applied transformations like grayscale and sepia to images by manipulating pixels.

By combining these two ideas — encryption from Caesar and pixel manipulation from Filter — I created Image Locker.

Motivation
I wanted to build something that connects cryptography with images. Text encryption is interesting, but it is not very visual. With images, you can actually see the difference between the original and the encrypted version. This makes the project more fun to demo and also easier to explain to people who don’t know much about programming.

Another motivation was to practice Flask. I had already done small Flask apps before, but I wanted to build a complete project with routes, templates, and file handling. This project gave me the chance to do that.

How It Works
The app has two main features: Encrypt and Decrypt.

Encrypt

The user uploads an image and enters a numeric key (and confirmation of the key).

The program shuffles the pixels of the image using a permutation generated from the key.

Then it applies XOR with the key to the pixel values.

The result is a scrambled image that looks nothing like the original.

The app saves both the encrypted image and the permutation file. These are bundled together in a ZIP file and sent back to the user.

Decrypt

The user uploads the ZIP file and enters the same key (with confirmation).

The app extracts the encrypted image and the permutation file.

It applies XOR with the key again to restore the pixel values.

Then it unshuffles the pixels using the saved permutation.

The result is the original image, which is sent back to the user.

Technical Details
Backend: Flask (Python). Routes are defined for /encrypt and /decrypt.

Libraries:

PIL (Pillow) for image handling.

NumPy for array manipulation and shuffling.

zipfile for bundling files together.

Frontend: HTML templates with CSS styling. The design is simple but clean, with forms for uploading files and entering keys.

The encryption method is not meant to be secure in a professional sense. It is more of a learning exercise. Real encryption would use algorithms like AES or RSA. But for a student project, pixel shuffling + XOR is enough to demonstrate the concept.

Inspiration from CS50:
The Caesar cipher problem set taught me the idea of using a key to transform data. In Caesar, the key shifts letters in the alphabet. In my project, the key is used to shuffle pixels and XOR values. The concept is similar: without the key, you cannot restore the original data.

The Filter problem set taught me how to manipulate images at the pixel level. In Filter, we changed colors to grayscale or sepia by applying formulas to pixel values. In my project, I shuffle and XOR pixel values. Again, the concept is similar: you take an image array and apply transformations to it.

So Image Locker is basically a combination of Caesar and Filter, but implemented in Python with Flask.

User Experience:
I wanted the app to be easy to use. The user just uploads a file, enters a key, and clicks a button. If something goes wrong (like missing key or mismatch), the app shows an error message on the same page. This is better UX than printing errors on a separate page.

Error messages are displayed inline, with a clear style so the user knows what went wrong. Success messages are displayed in a different style so the user knows when the process worked. This makes the app feel more user‑friendly.

Future Work:
In the future, I want to upgrade the app to support steganography. That means hiding data inside images. For example, the permutation file could be hidden inside the encrypted image itself, instead of being saved separately. This would make the app more advanced and closer to real cryptography applications.

I also want to improve the frontend with more CSS and maybe some JavaScript. For example: live validation of keys, and loading spinners. But for now, the app works fine without JS.

Conclusion:
Image Locker is a simple but meaningful project. It shows how ideas from CS50 problem sets can be combined into something new. It uses Flask, Python, NumPy, and Pillow to build a working web app. It demonstrates encryption concepts in a visual way.

For me, the most important part was learning how to handle images, arrays, and files in Python, and how to connect them with a web interface. I also learned about user experience and how to display errors in a friendly way.

This project is not perfect, but it is a good starting point. It is something I can show as a demonstration of what I learned in CS50, and later I can upgrade it with steganography and better design.
