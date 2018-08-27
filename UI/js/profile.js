
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
// function editprofile(){
// 	let key='username';
// 	let value='kimbugwe';
// 	let url='/api/v1/profile';
// 	let profile=new Profile(url);
// 	profile.edit(key,value);
// 	get_profile();
// }
// //set onclick events to edit profile
// document.getElementById('name').setAttribute('onclick','editprofile();');
// document.getElementById('email').setAttribute('onclick','editprofile();');


get_profile();
