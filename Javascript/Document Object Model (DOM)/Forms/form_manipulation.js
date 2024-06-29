function handleSubmit (event) {
    event.preventDefault();
    const username = document.getElementById("username").value;
    alert("Hello " + username + "! Form submitted successfully");
    document.getElementById("myForm").reset();
}