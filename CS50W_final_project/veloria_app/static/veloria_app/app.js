
// displaying the translation of a sentence 

document.addEventListener("DOMContentLoaded",function() {
    const transBlock = document.getElementById("translation-block");
    const transText = document.getElementById("translation-text");
    const sentences = document.querySelectorAll(".sentence");
    const closeBtn = document.getElementById("btn-close");
    const saveBtn = document.getElementById("btn-save");


    closeBtn.addEventListener("click", function() {
        transBlock.style.display = "none";
    });
    saveBtn.addEventListener("click",function() {
        const sentence_id = saveBtn.dataset.id;
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        // Sending data 
        fetch("/save/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken
            },
            body: JSON.stringify({
                sentence_id: sentence_id
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log("Saved: ",data);
            saveBtn.textContent = "✔ Saved";
            saveBtn.disabled = true;
            saveBtn.classList.add("btn-saved");
        })
        .catch(error => {
            console.error("Error saving: ",error)
        });

    });

    sentences.forEach(sentence => {
        sentence.addEventListener("click", () => {
            const sentenceId = sentence.dataset.id;
            transText.textContent = sentence.dataset.translation;

            fetch(`/check/?sentence_id=${sentenceId}`)
            .then(response => response.json())
            .then(data => {
                if(data.status === "already saved") {
                    saveBtn.textContent = "✔ Saved";
                    saveBtn.disabled = true;
                    saveBtn.classList.add("btn-saved");
                }
                else {
                    saveBtn.textContent = "Save";
                    saveBtn.disabled = false;
                    saveBtn.classList.remove("btn-saved");
                    saveBtn.dataset.id = sentenceId;
                }
            })
            .catch(error => console.error("Error checking: ",error));
            transBlock.style.display = "block";
            
        });
    });
    
});



// Rendering Stories

document.addEventListener("DOMContentLoaded", function() {
    const a1Btn = document.getElementById("A1-btn");
    const a2Btn = document.getElementById("A2-btn");
    const b1Btn = document.getElementById("B1-btn");
    const b2Btn = document.getElementById("B2-btn");
    const c1Btn = document.getElementById("C1-btn");

    const lvlBtns = [a1Btn, a2Btn, b1Btn, b2Btn, c1Btn];

    lvlBtns.forEach((btn, index) => {
        btn.addEventListener("click", function() {
            for (let i=1; i<=5; i++){
                const lvlDiv = document.getElementById(`level-div-${i}`);
                lvlDiv.style.display = "none";
            }
            const targetDivPosition = index + 1;
            const targetDiv = document.getElementById(`level-div-${targetDivPosition}`);
            targetDiv.style.display = "block"; 

        });
    });
});
