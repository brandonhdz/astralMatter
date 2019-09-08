
var toggled = false;

function activateMenuIcon() {
	toggled = !toggled;
	console.log(toggled);
	document.getElementById('menu_bar').classList.toggle("change");
   	document.getElementById('nav_mobile').classList.toggle("toggle_drop_down");
}