function loader(state) {
	if (state == true) {
		document.getElementById('loader').style.display = 'inline-block';
		var styleElem = document.head.appendChild(document.createElement('style'));
		styleElem.innerHTML = '#loader:after{display:"block"}';
        
	} else if (state == false) {
		document.getElementById('loader').style.display = 'none';
	}
}


// function errorbox(){
// 	let errorbox=document.getElementById('errormsg');
// 	var errorheader=document.createElement('div')
// 	errorheader.className('entry_name')
// 	<div id="myModal" class="entry_name">
//         <!-- Modal content -->
//         <div class="modal-content">
//             <div class="entry_name">
//                 <span class="close">&times;</span>
//                 <h2 id='entry_title'>title</h2>
//             </div>
//             <div class="modal-body">
//                 <p id='entry_content'>Some text in the Modal Body</p>
//             </div>
//             <div class="entry_date">
//                 <span class="action">&#x270E;</span>
//                 <span class="action">&#x1F5D1;</span>
//                 <h3 id='date'>entry_date</h3>
//             </div>
//         </div>

//     </div>
// }