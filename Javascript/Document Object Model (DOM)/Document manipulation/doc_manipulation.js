function updateParagraph () {
    const paragraph = document.getElementById("message"); //referencing html document

    paragraph.innerHTML = "Updated paragraph content"; //this is changing the paragraph element

    const newParagraph = document.createElement("p");
    newParagraph.innerHTML = "This is a new paragraph"; //creating <p> tag that says "this is a new paragraph"

    document.getElementById('container').appendChild(newParagraph) //this is adding that new paragraph to the container at the very end
}

function changeImage() {
    const newImageSrc = "desert.jpg";
    document.getElementById("image").src = newImageSrc;
}

function changeImageBack () {
    const newImageSrc = "ocean.jpg";
    document.getElementById("image").src = newImageSrc
}