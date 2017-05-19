function loader() {
		var body = $('body')[0];
		var loader = $('.preloader')[0];

		setTimeout(function() {
			loader.style.opacity = 0;
			loader.style.visibility = 'hidden';
			body.style.overflow = 'visible';
		},1000);
	};

	window.onload = function() {
	loader();
}

$('#showContacts').click(function() {
	$('body').toggleClass('show-contacts');
});