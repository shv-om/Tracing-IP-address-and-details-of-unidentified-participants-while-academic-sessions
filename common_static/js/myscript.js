
let mainNav = document.getElementById('navigation-menu');
let navBarToggle = document.getElementById('js-navigation-toggle');

let navigation = document.getElementById('navigation');


navBarToggle.addEventListener('click', function(){
  mainNav.classList.toggle('toggle-active');
  navigation.style.backgroundImage = "linear-gradient(260deg, rgb(0, 68, 42) 0%, rgb(119, 198, 168) 100%)";
});


// To toggle Navigation Bar

$('.dropdown').on('show.bs.dropdown', function () {
	$(this).find('.dropdown-menu').first().stop(true, true).slideDown();
});

$('.dropdown').on('hide.bs.dropdown', function () {
	$(this).find('.dropdown-menu').hide();
});
