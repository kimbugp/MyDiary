// var baseurl = 'http://127.0.0.1:5000';
// function to post signup info
if (sessionStorage.getItem('Token')) {
	window.location.href = 'home.html';
}

function create_user() {
	var mybody = JSON.stringify({
		'username': document.getElementById('username').value,
		'name': document.getElementById('name').value,
		'email': document.getElementById('email').value,
		'password': document.getElementById('password').value
	});
	var myURL = baseurl + '/api/v1/auth/signup';
	var myheaders = {
		'Content-Type': 'application/json'
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
		.then(function (json) {
			loader(false);
			if (json.Message == 'User created') {
				login();
			} else {
				errormsg(json.Message);
				var notification = new Notification();	
				notification(json.Message);

			}
		})
		.catch(error => {
			loader(false);
			alert(error);
		});
	return false;
}

function login() {
	let mybody = JSON.stringify({
		'username': document.getElementById('username').value,
		'password': document.getElementById('password').value
	});
	var myURL = baseurl + '/api/v1/auth/login';
	var myheaders = {
		'Content-Type': 'application/json',
		'Accept': 'application/json'
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
		.then(function (json) {
			loader(false);
			if (json.Token) {
				sessionStorage.setItem('Token', json.Token);
				window.location.href = 'home.html';
			} else {
				errormsg(json.Message);
				var notification = new Notification();
				notification(json.Message);
			}
		})
		.catch(error => {
			loader(false);
			alert(error);
		});
	return false;
}
function confirmpsd(psw2){
	let psw=document.getElementById('password').value;
	if(psw!=psw2.value){
		// alert('match');
		psw2.setCustomValidity('password not matching');
	}
	else{
		psw2.setCustomValidity('');
	}
}