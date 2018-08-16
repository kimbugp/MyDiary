function loader(state) {
	if (state == true) {
		document.getElementById('loader').style.display = 'inline-block';
		var styleElem = document.head.appendChild(document.createElement('style'));
		styleElem.innerHTML = '#loader:after{display:"block"}';
        
	} else if (state == false) {
		document.getElementById('loader').style.display = 'none';
	}
}

function errormsg(x){
	let errordiv=document.getElementById('errormsg');
	errordiv.style.display='block';
	errordiv.innerHTML=x;
}
// // function errorbox(){
// 	let errorbox=document.getElementById('errormsg');

// 	//error header
// 	let title=document.createElement('h2');
// 	title.setAttribute('id','entry_title');
// 	title.innerHTML='Error message';
// 	let errorheader=document.createElement('div');
// 	errorheader.setAttribute('id','errorheader');
// 	errorheader.appendChild(title);

// 	//create error body
// 	let body=document.createElement('div');
// 	var errordata=document.createElement('p');
// 	errordata.setAttribute('id','errordata');
// 	body.setAttribute('id','errorbody');
// 	body.appendChild(errordata);

// 	//create error footer
// 	let footer=document.createElement('div');
// 	var footerdata=document.createElement('p');
// 	footerdata.setAttribute('id','footerdata');
// 	footer.setAttribute('id','errorfooter');
// 	footer.appendChild(footerdata);

// 	//append title body and footer to box
// 	errorbox.appendChild(errorheader);
// 	errorbox.appendChild(body);
// 	errorbox.appendChild(footer);
// }