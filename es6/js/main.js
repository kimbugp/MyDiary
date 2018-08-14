
// var baseurl = 'https://simondb.herokuapp.com';
const Token = sessionStorage.getItem('Token');
if(Token == null){
	window.location.href='index.html';
} 

// function hello_world() {
// 	var myheaders = {
// 		'Content-Type': 'application/json'
// 	};
// 	var init = {
// 		method: 'get',
// 		headers: myheaders
// 	};
// 	fetch(baseurl, init)
// 		.then(res => res.json())
// 		.then(res => console.log(res));
// }

function signout(){
	sessionStorage.removeItem('Token');
	window.location.href='index.html';
}
function clear(){
	document.getElementById('new_entrycontent').value='';
	document.getElementById('new_entryname').value='';
}

//function to post signin info

// function to post an entry

//function to get all entries

// function to et individula entry

//function to delete an entry

//function to edit entry


//function to view profile