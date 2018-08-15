function loader(state) {
	if (state == true) {
		document.getElementById('loader').style.display = 'inline-block';
		var styleElem = document.head.appendChild(document.createElement('style'));
		styleElem.innerHTML = '#loader:after{display:"block"}';
        
	} else if (state == false) {
		document.getElementById('loader').style.display = 'none';
	}
}