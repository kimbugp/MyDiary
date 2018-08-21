
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
		let entry=new Entries(id);
		entry.edit();
	};
}

function togglesavebuttons(x) {
	let savebtn=document.getElementById('save_new_entry');
	let editbtn=document.getElementById('edit_entry');
	let savetitle=document.getElementById('entry_titleheader');
	let edittitle=document.getElementById('edit_title');
	let none='none';
	let block='block';
	if(x=='edit'){
		toggle(block,none);
	}
	else if(x=='new'){
		toggle(none,block);
	}
	

	function toggle(x,y) {
		//change save button
		savebtn.style.display = y;
		editbtn.style.display = x;
		//change title of modal
		savetitle.style.display = y;
		edittitle.style.display = x;
	}
}

