function inputFocus(i) {
    if (i.value == i.defaultValue) { i.value = ""; i.style.color = "#000"; }
}
function inputBlur(i) {
    if (i.value == "") { i.value = i.defaultValue; i.style.color = "#888"; }
}
var checkLoginPass = function () {
    var login = document.getElementById("login").value;
    var pass = document.getElementById("password").value;
    if (login === "peter" && pass === "6761") {
        window.location.replace("http://entertainobc.github.io");
    }
    if (login === "connor" && pass === "6314") {
        window.location.replace("http://entertainobc.github.io");
    }
    if (login === "bryan" && pass === "6631") {
        window.location.replace("http://www.google.com");
    }
    else {
        //do something else;
    }
}