function add_entry() {
	let {
		name,
		body
	} = entry_div();
	let msg = document.getElementById('msg');
	if (!name.checkValidity()) {
		msg.innerHTML = name.title;
		return;
	} else if (!body.checkValidity()) {
		msg.innerHTML = body.title;
		return;
	}
	let entry = new Entries;
	entry.addentry();
}
close_newentrymodel();

function entry_div() {
	let body = document.getElementById('new_entrycontent');
	let name = document.getElementById('new_entryname');
	return {
		name,
		body
	};
}

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
		if (checkdate() == false) {
			alert('entry cannot be edited...A day has passed');
			return;
		}

		modal.style.display = 'none';
		let {
			name,
			body
		} = entry_div();
		//set the entry form to show previous data
		document.getElementsByClassName('modal')[1].style.display = 'block';
		body.value = document.getElementById('entry_content').innerHTML;
		name.value = document.getElementById(id).innerHTML;
		togglesavebuttons('edit');

	};
	let saveedit = document.getElementById('edit_entry');
	saveedit.onclick = function () {
		let entry = new Entries(id);
		entry.edit();
	};
}

function togglesavebuttons(x) {
	let savebtn = document.getElementById('save_new_entry');
	let editbtn = document.getElementById('edit_entry');
	let savetitle = document.getElementById('entry_titleheader');
	let edittitle = document.getElementById('edit_title');
	let none = 'none';
	let block = 'block';
	if (x == 'edit') {
		toggle(block, none);
	} else if (x == 'new') {
		toggle(none, block);
	}


	function toggle(x, y) {
		//change save button
		savebtn.style.display = y;
		editbtn.style.display = x;
		//change title of modal
		savetitle.style.display = y;
		edittitle.style.display = x;
	}
}
//function to check if day has passed
function checkdate() {
	let entry_date = document.getElementById('date').innerHTML;
	let en = Date.parse(new Date()) - Date.parse(entry_date);
	if (en > 86400000) {
		return false;
	}
	return 'Entry Edited';

}