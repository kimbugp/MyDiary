function clear() {
	document.getElementById('new_entrycontent').value = '';
	document.getElementById('new_entryname').value = '';
}
show_data();
function show_data() {
	let url='/api/v1/entries';
	let entry=new Entries(null);
	entry.getall(url);
	let addbtn=document.getElementById('add');
	addbtn.onclick=function(){
		document.getElementsByClassName('modal')[1].style.display='block';
		clear();
		togglesavebuttons('new');
	};
}
function click_events() {
	return show_details(this.id),delete_one(this.id),edit_one(this.id);
}
function entry_iterate(objectlength, object) {
	for (let i = 0; i < objectlength; i++) {
		//make list of entry titles
		let title = object[i].entry_name;
		let id = object[i].entry_id;
		let record = document.createElement('li');
		record.setAttribute('id', id);
		record.appendChild(document.createTextNode(title));
		record.onclick=click_events;
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
