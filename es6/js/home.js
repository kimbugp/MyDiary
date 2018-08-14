const baseurl = 'https://simondb.herokuapp.com';
const Token = sessionStorage.getItem('Token');
var modal = document.getElementById('myModal');

function get_entries() {
	let myURL = baseurl + '/api/v1/entries';
	let myheaders = {
		'Content-Type': 'application/json',
		'Accept': 'application/json',
		'Token': Token
	};
	let init = {
		method: 'GET',
		headers: myheaders
	};
	return fetch(myURL, init)
		.then((response) => response.json())
		.then((responseData) => {
			return responseData;
		})
		.catch(error => {
			alert(error);
		});
}
// get_entries().then(response => console.log(response));
function show_data() {
	get_entries().then(response => {
		let object = response.entries;
		let objectlength = object.length;
		entry_iterate(objectlength, object, click_events);
	});


	function click_events() {
		return 'show_details(this.id);delete_one(this.id)';
	}
}

//set the html links
html_links();

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

function entry_iterate(objectlength, object, click_events) {
	for (let i = 0; i < objectlength; i++) {
		//make list of entry titles
		let title = object[i].entry_name;
		let id = object[i].entry_id;
		let record = document.createElement('li');
		record.setAttribute('id', id);
		record.appendChild(document.createTextNode(title));
		record.setAttribute('onclick', click_events());
		document.getElementById('myUL').appendChild(record);
	}
}

function delete_entry(entry_id) {
	let myURL = baseurl + '/api/v1/entries/' + entry_id;
	let myheaders = {
		'Content-Type': 'application/json',
		'Accept': 'application/json',
		'Token': Token
	};
	let init = {
		method: 'DELETE',
		headers: myheaders
	};
	fetch(myURL, init)
		.then(function (response) {
			return response.json();
		})
		.then(function (response) {
			modal.style.display = 'none';
			alert(response.Message);
			location.reload();
		})
		.catch(error => {
			alert(error);
		});
	return false;
}

function delete_one(id) {
	let delbutton = document.getElementsByClassName('action')[1];
	delbutton.onclick = function () {
		delete_entry(id);

	};
}


function show_details(id) {
	get_entry();

	function get_entry() {
		get_entries().then(response => {
			let object = response.entries;
			display(object);
			// Get the modal
			// Get the <span> element that closes the modal
			let span = document.getElementsByClassName('close')[0];
			span.onclick = function () {
				modal.style.display = 'none';
			};
			// edit  functionality
			let button = document.getElementsByClassName('action')[0];
			button.onclick = function () {
				// console.log('edited');
			};
			// When the user clicks anywhere outside of the modal, close it
			window.onclick = function (event) {
				if (event.target == modal) {
					modal.style.display = 'none';
				}
			};
		});
	}

	function display(object) {
		for (let i = 0; i < object.length; i++) {
			if (object[i].entry_id == id) {
				let d = object[i].entry_date;
				let title = object[i].entry_name;
				let content = object[i].entry_content;
				modal.style.display = 'block';
				document.getElementById('entry_title').innerHTML = title;
				document.getElementById('entry_content').innerHTML = content;
				document.getElementById('date').innerHTML = d;
			}
		}
	}
}

function add_entry(id){
	

}
show_data();