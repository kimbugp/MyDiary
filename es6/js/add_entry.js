
function add_entry() {
	var mybody = JSON.stringify({
		'entry_content': document.getElementById('new_entrycontent').value,
		'entry_name': document.getElementById('new_entryname').value,
	});
	let myURL = baseurl + '/api/v1/entries';
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
	loader(true);
	fetch(myURL, init)
		.then(function (response) {
			return response.json();
		})
		.then(function (response) {
			loader(true);
			if (response.Message == 'entry created') {
				location.reload();
			}
			else{
				loader(false);
				var notification = new Notification(response.Message);
			}
		})
		.catch(error => {
			loader(false);
			alert(error);
		});
	return false;
}
close_newentrymodel();

function close_newentrymodel() {
	//close modal when clicked
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

function edit_entry(entry_id) {
	let myURL = baseurl + '/api/v1/entries/' + entry_id;
	var mybody = JSON.stringify({
		'entry_content': document.getElementById('new_entrycontent').value,
		'entry_name': document.getElementById('new_entryname').value,
	});
	let myheaders = {
		'Content-Type': 'application/json',
		'Accept': 'application/json',
		'Token': Token
	};
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

function edit_one(id) {
	let editbutton = document.getElementsByClassName('action')[0];
	editbutton.onclick = function () {
		modal.style.display = 'none';
		//set the entry form to show previous data
		document.getElementsByClassName('modal')[1].style.display = 'block';
		document.getElementById('new_entrycontent').value = document.getElementById('entry_content').innerHTML;
		document.getElementById('new_entryname').value = document.getElementById(id).innerHTML;
		togglesavebuttons('edit');

	};
	let saveedit = document.getElementById('edit_entry');
	saveedit.onclick = function () {
		edit_entry(id);
		

	};
}

function togglesavebuttons(x) {
	if(x=='edit'){
		//change save button 
		document.getElementById('save_new_entry').style.display = 'none';
		document.getElementById('edit_entry').style.display = 'block';
		//change title of modal
		document.getElementById('entry_titleheader').style.display = 'none';
		document.getElementById('edit_title').style.display = 'block';
	}
	else if(x=='new'){
		//change save button 
		document.getElementById('save_new_entry').style.display = 'block';
		document.getElementById('edit_entry').style.display = 'none';
		//change title of modal
		document.getElementById('entry_titleheader').style.display = 'block';
		document.getElementById('edit_title').style.display = 'none';
	}
	
}

