// from home import baseurl
// const baseurl = 'https://simondb.herokuapp.com';
// const Token = sessionStorage.getItem('Token');

function add_entry() {
	var mybody = JSON.stringify({
		'entry_content': document.getElementById('new_entrycontent').value,
		'entry_name': document.getElementById('new_entryname').value,
	});
	let myURL = baseurl + '/api/v1/entries/';
	let myheaders = {
		'Content-Type': 'application/json',
		'Accept': 'application/json',
		'Token': Token
	};
	var init = {
		method: 'POST',
		headers: myheaders,
		body: mybody
	};
	fetch(myURL, init)
		.then(function (response) {
			return response.json();
		})
		.then(function (response) {
			if (response.Message == 'entry created') {
				alert(response.Message);
				location.reload();
			}
			alert(response.Message);
		})
		.catch(error => {
			alert(error);
		});
	return false;
}
//close modal when clicked
close_newentrymodel();

function close_newentrymodel() {
	var entrymodal = document.getElementById('newentrymodal');
	var span = document.getElementsByClassName('close')[1];
	span.onclick = function () {
		entrymodal.style.display = 'none';
	};
	// When the user clicks anywhere outside of the modal, close it
	window.onclick = function (event) {
		if (event.target == entrymodal) {
			entrymodal.style.display = 'none';
		}
	};
}
