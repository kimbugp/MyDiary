
function get_profile() {
	let url = '/api/v1/profile';
	get_request(url).then(response =>{
		loader(false);
		let no=response[0].count;
		let mail=response[0].email;
		let uname=response[0].username;
		let name=response[0].name;
		displayprofile(no,mail,uname,name);
	});
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