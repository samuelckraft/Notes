document.getElementById('myButton').addEventListener('click', function () {
    alert("Button Clicked")
});

// .addEventListener(<event>, <function>)\


function clickHandler () {
    alert("Button Clicked");

    document.getElementById("removeButton").removeEventListener('click', clickHandler);
    alert("Event listener removed")
}

document.getElementById("removeButton").addEventListener("click", clickHandler)