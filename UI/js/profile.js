function get_profile() {
	let url = '/api/v1/profile';
	let profile = new Profile(url);
	profile.get();
	document.getElementById('professionedit').onclick=show_edit_modal;
}

function displayprofile(no, mail, username, name,profession) {
	let entries = document.getElementById('noentries');
	entries.innerText = 'No of Entries:' + no;

	let email = document.getElementById('useremail');
	email.innerText = 'Email:' + mail;

	let fullname = document.getElementById('fullname');
	fullname.innerText = name;

	let uname = document.getElementById('uname');
	uname.innerText = 'Username:' + username;

	let prof = document.getElementById('profession');
	prof.innerText ='Profession:' +profession;

}
document.getElementById('edit_profile').addEventListener('submit',editprofile);
function editprofile(event) {
	event.preventDefault();
	let value=document.getElementsByName('profession')[0].value;
	let url = '/api/v1/profile';
	let profile = new Profile(url);
	profile.edit(value);
	editprofilemodal.style.display = 'none';
	get_profile();
}
document.getElementById('professionedit').addEventListener('click',show_edit_modal);
const editprofilemodal = document.getElementById('editprofilemodal');
function show_edit_modal() {
	editprofilemodal.style.display = 'block';
	document.getElementsByClassName('edit_profile')[0].onsubmit=editprofile;
	let span = document.getElementsByClassName('close')[0];
	span.onclick = function () {
		editprofilemodal.style.display = 'none';
	};
	window.onclick = function (event) {
		if (event.target == editprofilemodal) {
			editprofilemodal.style.display = 'none';
		}
	};

}
get_profile();