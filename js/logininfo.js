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
        window.location.replace("http://entertainobc.github.io/USERWEB/userkey=3937221/user=peter/index.html");
    }
    if (login === "bryan" && pass === "6631") {
        window.location.replace("http://entertainobc.github.io/USERWEB/userkey=3937221/user=bryan/index.html");
    }
    else {
        //do something else;
    }
}