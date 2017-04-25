//Javascript

var panel = document.getElementById('panel');
var body = document.getElementById('body');
var menu = document.getElementById('show_Menu');

function show(){
	panel.style.transition = "all .4s linear";
	panel.style.marginLeft = "-20vw";
	body.style.background = "#fff";
	body.style.width = "100vw";

}

function show_Menu(){
	panel.style.width = "20vw";
	body.style.width = "80vw";
	panel.style.marginLeft = "0vw";
	panel.style.visibility = "visible";
	panel.style.transition = "all .4s linear";
}

/*Modify
//Javascript

var panel = document.getElementById('panel');
var body = document.getElementById('body');
var menu = document.getElementById('show_Menu');

function show(){
	panel.style.transition = "all .4s linear";
  body.style.transition = "all .4s linear";
	panel.style.marginLeft = "-20vw";
	body.style.background = "#fff";
	body.style.width = "100vw";
  body.style.margin = "0";

}

function show_Menu(){
	panel.style.width = "20vw";
	body.style.width = "80vw";
  body.style.marginLeft = "20vw";
	panel.style.marginLeft = "0vw";
	panel.style.visibility = "visible";
	panel.style.transition = "all .4s linear";
  body.style.transition = "all .4s linear";
}
*/