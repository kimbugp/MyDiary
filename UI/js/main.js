
const baseurl = 'https://simondb.herokuapp.com';
// const baseurl = 'http://127.0.0.1:5000';
const Token = sessionStorage.getItem('Token');
if(Token == null){
	window.location.href='index.html';
} 

function signout(){
	sessionStorage.removeItem('Token');
	window.location.href='index.html';
}
function clear(){
	document.getElementById('new_entrycontent').value='';
	document.getElementById('new_entryname').value='';
}