var modal = document.getElementById('myModal');

function get_request(url) {
	let myURL = baseurl + url;
	let myheaders = {
		'Content-Type': 'application/json',
		'Accept': 'application/json',
		'Token': Token
	};
	loader(true);
	let init = {
		method: 'GET',
		headers: myheaders
	};
	return fetchdata(myURL, init);
}
function show_data() {
	let url='/api/v1/entries';
	loader(true);
	get_request(url).then(response => {
		loader(false);
		let object = response.entries;
		let objectlength = object.length;
		entry_iterate(objectlength, object, click_events);
	});
}
function click_events() {
	return 'show_details(this.id);delete_one(this.id);edit_one(this.id)';
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
function delete_one(id) {
	let delbutton = document.getElementsByClassName('action')[1];
	delbutton.onclick = function () {
		let entry=new Entries(id);
		entry.delete();
	};
}

function show_details(id) {
	fetchoneentry(id).then(response =>{
		loader(false);
		let object = response.entries[0];
		let d = object.entry_date;
		let title = object.entry_name;
		let content = object.entry_content;
		modal.style.display = 'block';
		document.getElementById('entry_title').innerHTML = title;
		document.getElementById('entry_content').innerHTML = content;
		document.getElementById('date').innerHTML = d;
		// Get the modal
		// Get the <span> element that closes the modal
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
	});
	
}

function fetchoneentry(id) {
	let url='/api/v1/entries';
	let myURL = baseurl + url + '/' + id;
	let myheaders = {
		'Content-Type': 'application/json',
		'Accept': 'application/json',
		'Token': Token
	};
	loader(true);
	let init = {
		method: 'GET',
		headers: myheaders
	};
	return fetchdata(myURL, init);
}

function fetchdata(myURL, init) {
	return fetch(myURL, init)
		.then((response) => response.json())
		.then((responseData) => {
			return responseData;
		})
		.catch(error => {
			loader(false);
			alert(error);
		});
}

html_links();
