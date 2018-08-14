function add_entry(id) {
	var mybody = JSON.stringify({
		'username': document.getElementById('username').value,
		'name': document.getElementById('name').value,
		'email': document.getElementById('email').value,
		'password': document.getElementById('password').value
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
			location.reload();
		})
		.catch(error => {
			alert(error);
		});
	return false;
}