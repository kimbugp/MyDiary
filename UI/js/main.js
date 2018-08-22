const baseurl = 'https://simondb.herokuapp.com';
// const baseurl = 'http://127.0.0.1:5000';
const Token = sessionStorage.getItem('Token');
if (Token == null) {
	window.location.href = 'index.html';
}

function signout() {
	sessionStorage.removeItem('Token');
	window.location.href = 'index.html';
}

function clear() {
	document.getElementById('new_entrycontent').value = '';
	document.getElementById('new_entryname').value = '';
}

function html_links() {
	var links = document.getElementsByClassName('navbar');
	for (let i = 0; i < links.length; i++) {
		let text = links[i].textContent;
		links[i].textContent = '';
		let a = document.createElement('a');
		a.href = text.toLowerCase() + '.html';
		a.textContent = text;
		links[i].appendChild(a);
	}
}

class Entries {
	constructor(id) {
		this.id = id;
	}
	delete() {
		let myheaders = this.myheaders();
		let myURL = baseurl + '/api/v1/entries/' + this.id;
		let init = {
			method: 'DELETE',
			headers: myheaders
		};
		loader(true);
		fetch(myURL, init)
			.then(function (response) {
				return response.json();
			})
			.then(function (response) {
				loader(false);
				modal.style.display = 'none';
				var notification = new Notification(response.Message);
				location.reload();
			})
			.catch(error => {
				loader(false);
				alert(error);
			});
		return false;
	}
	myheaders() {
		return {
			'Content-Type': 'application/json',
			'Accept': 'application/json',
			'Token': Token
		};
	}

	edit() {
		let {
			myURL,
			init
		} = this.editheader();
		loader(true);
		fetch(myURL, init)
			.then(function (response) {
				return response.json();
			})
			.then(function (response) {
				loader(false);
				modal.style.display = 'none';
				if (response.Message == 'entry edited') {
					location.reload();
				} else {
					var notification = new Notification(response.message);
				}
			})
			.catch(error => {
				alert(error);
			});
		return false;

	}
	editheader() {
		let myheaders = this.myheaders();
		let myURL = baseurl + '/api/v1/entries/' + this.id;
		var mybody = this.mybody();
		let init = {
			method: 'PUT',
			headers: myheaders,
			body: mybody
		};
		return {
			myURL,
			init
		};
	}

	getone() {
		let {
			myURL,
			init
		} = this.getoneheader();
		return fetch(myURL, init)
			.then(function (response) {
				return response.json();
			})
			.then(function (response) {
				loader(false);
				let object = response.entries[0];
				let d = object.entry_date;
				let title = object.entry_name;
				let content = object.entry_content;
				modal.style.display = 'block';
				document.getElementById('entry_title').innerHTML = title;
				document.getElementById('entry_content').innerHTML = content;
				document.getElementById('date').innerHTML = d;
				// Get the modal Get the <span> element that closes the modal
				let span = document.getElementsByClassName('close')[0];
				span.onclick = function () {
					modal.style.display = 'none';
				};
				// When the user clicks anywhere outside of the modal, close it
				window.onclick = function (event) {
					if (event.target == modal) {
						modal.style.display = 'none';
					}
				};
			})
			.catch(error => {
				alert(error);
			});
	}
	getoneheader() {
		let myheaders = this.myheaders();
		let url = '/api/v1/entries';
		let myURL = baseurl + url + '/' + this.id;
		loader(true);
		let init = {
			method: 'GET',
			headers: myheaders
		};
		return {
			myURL,
			init
		};
	}

	getall(url) {
		let myheaders = this.myheaders();
		this.url = url;
		let myURL = baseurl + this.url;
		loader(true);
		let init = {
			method: 'GET',
			headers: myheaders
		};
		return fetch(myURL, init)
			.then(function (response) {
				return response.json();
			})
			.then(function (response) {
				loader(false);
				let object = response.entries;
				let objectlength = object.length;
				entry_iterate(objectlength, object, click_events);

			})
			.catch(error => {
				loader(false);
				alert(error);
			});
	}
	addentry() {
		var {
			myURL,
			init
		} = this.newentryheader();
		loader(true);
		fetch(myURL, init)
			.then(function (response) {
				return response.json();
			})
			.then(function (response) {
				loader(true);
				if (response.Message == 'entry created') {
					location.reload();
				} else {
					loader(false);
					var notification = new Notification(response.message);
				}
			})
			.catch(error => {
				loader(false);
				alert(error);
			});
		return false;
	}

	newentryheader() {
		let myheaders = this.myheaders();
		var mybody = this.mybody();
		let myURL = baseurl + '/api/v1/entries';
		var init = {
			method: 'POST',
			headers: myheaders,
			body: mybody
		};
		return {
			myURL,
			init
		};
	}

	mybody() {
		return JSON.stringify({
			'entry_content': document.getElementById('new_entrycontent').value,
			'entry_name': document.getElementById('new_entryname').value,
		});
	}
}
class Profile {
	constructor(url) {
		this.url = url;
		this.headers = new Entries(null);
	}
	getprofile() {
		let myheaders = this.headers.myheaders();
		let myURL = baseurl + this.url;
		loader(true);
		let init = {
			method: 'GET',
			headers: myheaders
		};
		return fetch(myURL, init)
			.then(function (response) {
				return response.json();
			})
			.then(function (response) {
				loader(false);
				let no = response[0].count;
				let mail = response[0].email;
				let uname = response[0].username;
				let name = response[0].name;
				displayprofile(no, mail, uname, name);
			})
			.catch(error => {
				loader(false);
				alert(error);
			});
	}
}