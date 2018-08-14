var baseurl = 'https://simondb.herokuapp.com';
// function to post signup info
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
			if (json.Message == 'User created') {
				login();
			}
			document.getElementById('message').innerHTML = json.Message;
		})
		.catch(error => {
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
			if (json.Token) {
				sessionStorage.setItem('Token', json.Token);
				window.location.href = 'home.html';
			}
			document.getElementById('message').innerHTML = json.Message;

		})
		.catch(error => {
			alert(error);
		});
	return false;
}