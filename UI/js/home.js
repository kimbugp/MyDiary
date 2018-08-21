var modal = document.getElementById('myModal');

function show_data() {
	let url='/api/v1/entries';
	loader(true);
	let entry=new Entries(null);
	entry.getall(url);
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
	let entry=new Entries(id);
	entry.getone();
}
html_links();