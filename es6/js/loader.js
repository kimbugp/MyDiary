function loader(state) {
	if (state == true) {
		document.getElementById('loader').style.display = 'block';
	} else if (state == false) {
		document.getElementById('loader').style.display = 'none';
	}
}