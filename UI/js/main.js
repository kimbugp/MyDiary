
const baseurl = 'https://simondb.herokuapp.com';
// const baseurl = 'http://127.0.0.1:5000';
const Token = sessionStorage.getItem('Token');
if(Token == null){
	window.location.href='index.html';
} 

function signout(){
	sessionStorage.removeItem('Token');
	window.location.href='index.html';
}
function clear(){
	document.getElementById('new_entrycontent').value='';
	document.getElementById('new_entryname').value='';
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
let myheaders = {
	'Content-Type': 'application/json',
	'Accept': 'application/json',
	'Token': Token
};
class Entries{
	constructor(id){
		this.id=id;
	}
	delete(){
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
	edit(){
		let myURL = baseurl + '/api/v1/entries/' + this.id;
		var mybody = JSON.stringify({
			'entry_content': document.getElementById('new_entrycontent').value,
			'entry_name': document.getElementById('new_entryname').value,
		});
		let init = {
			method: 'PUT',
			headers: myheaders,
			body: mybody
		};
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
				}
				else{
					var notification = new Notification(response.Message);
				}
			})
			.catch(error => {
				alert(error);
			});
		return false;
	
	}
	getone(){
		let url='/api/v1/entries';
		let myURL = baseurl + url + '/' + id;
		loader(true);
		let init = {
			method: 'GET',
			headers: myheaders
		};
	}
}