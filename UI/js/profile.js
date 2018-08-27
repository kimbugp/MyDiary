
function get_profile() {
	let url = '/api/v1/profile';
	let profile=new Profile(url);
	profile.get();
}
function displayprofile(no,mail,username,name){
	let entries=document.getElementById('noentries');
	entries.innerText='No of Entries:'+no;

	let email=document.getElementById('useremail');
	email.innerText='Email:'+mail;

	let fullname=document.getElementById('fullname');
	fullname.innerText=name;

	let uname=document.getElementById('uname');
	uname.innerText='Username:'+username;

}
function editprofile(){
	let url='/api/v1/profile';
	let profile=new Profile(url);
	profile.edit();
}
get_profile();