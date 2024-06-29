function handleButtonClick () {
    alert("Button Clicked")
}

function handleMouseOver () {
    console.log("Mouse over element")
}

function handleMouseOut () {
    console.log("Mouse out of element")
}

function handleKeyDown (event) {
    console.log("Key pressed:", event.key) // The event output gives a ton of info, so the .element navigate to the value we want to display
}

function handleSubmit(event) {
    event.preventDefault();
    const username = event.target.elements.username.value;
    console.log("Form submitted with username:", username)
}

function handleChange(event) {
    console.log("Input value changed to:", event.target.value)
}

function handleFocus() {
    console.log("Input element focused")
}