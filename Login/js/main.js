/* ======================================================================
  Author Custom JavaScript
====================================================================== */
// Loop through Array of Objects
var objPeople = [
	{ // Object @ 0 index
		username: "bryan",
		password: "dao"
	},
	{ // Object @ 1 index
		username: "peter",
		password: "dao"
	},


]

function GetInfo() {
	var username = document.getElementById('username').value
	var password = document.getElementById('password').value

	for(var i = 0; i < objPeople.length; i++) {
		// check is user input matches username and password of a current index of the objPeople array
		if(username == objPeople[i].username && password == objPeople[i].password) {
			console.log(username + " is logged in!!!")
			window.location.assign("https://entertainobc.github.io/Login/")
			// stop the function if this is found to be true
			return
		}
	}
	console.log("incorrect username or password")
}