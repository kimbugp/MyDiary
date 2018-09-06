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
	let pic = document.getElementById('profpic');
	if (path != null) {
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
		if (event.target == modal) {
			modal.style.display = 'none';
		}
	};
}
const editpicmodal = document.getElementById('editpicmodal');

function add_pic_modal() {

	editpicmodal.style.display = 'block';
	document.getElementById('addpic').onsubmit = editpic;
	let span = document.getElementById('clpic');
	closebtn(span, editpicmodal);

}
document.getElementById('addpic').addEventListener('submit', editpic);

function editpic(event) {
	event.preventDefault();
	var input = document.querySelector('input[type="file"]')
	var data = new FormData()
	data.append('photo', input.files[0])
	let url = '/api/v1/profile/pic';
	let profile = new Profile(url);
	profile.pic(data);
	editpicmodal.style.display='none';
}
get_profile();