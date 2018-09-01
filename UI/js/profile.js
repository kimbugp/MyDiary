function get_profile() {
	let url = '/api/v1/profile';
	let profile = new Profile(url);
	profile.get();
	document.getElementById('professionedit').onclick = show_edit_modal;
	document.getElementById('picture').onclick = add_pic_modal;
}

function displayprofile(no, mail, username, name, profession, path) {
	let entries = document.getElementById('noentries');
	entries.innerText = 'No of Entries:' + no;

	let email = document.getElementById('useremail');
	email.innerText = 'Email:' + mail;

	let fullname = document.getElementById('fullname');
	fullname.innerText = name;

	let uname = document.getElementById('uname');
	uname.innerText = 'Username:' + username;
	let prof = document.getElementById('profession');
	if (profession != null) {
		prof.innerText = 'Profession:' + profession;
	} else {
		prof.innerText = 'Profession: Add Profession';
	}
	let pic = document.getElementById('procpic');
	if (pic != null) {
		pic.setAttribute('src', path);
	}
}
document.getElementById('edit_profile').addEventListener('submit', editprofile);
const editprofilemodal = document.getElementById('editprofilemodal');

function editprofile(event) {
	event.preventDefault();
	let value = document.getElementsByName('profession')[0].value;
	let url = '/api/v1/profile';
	let profile = new Profile(url);
	profile.edit(value);
	editprofilemodal.style.display = 'none';
	get_profile();
}

function show_edit_modal() {
	editprofilemodal.style.display = 'block';
	document.getElementsByClassName('edit_profile')[0].onsubmit = editprofile;
	let span = document.getElementsByClassName('close')[0];
	closebtn(span, editprofilemodal);

}

function closebtn(span, modal) {
	span.onclick = function () {
		modal.style.display = 'none';
	};
	window.onclick = function (event) {
		if (event.target == editprofilemodal) {
			modal.style.display = 'none';
		}
	};
}
const editpicmodal = document.getElementById('editpicmodal');

function add_pic_modal() {

	editpicmodal.style.display = 'block';
	document.getElementById('addpic').onsubmit = function () {
		var formData = new FormData();
		var fileField = document.getElementById('picfile').value;
		formData.append('title', 'new');
		formData.append('photo', fileField.files);

		let url = '/api/v1/profile/pic';
		let profile = new Profile(url);
		profile.pic(formData);
	};
	let span = document.getElementById('clpic');
	closebtn(span, editpicmodal);

}
get_profile();