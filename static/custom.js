// Got this idea from Giulio G. at https://stackoverflow.com/questions/49530497/how-do-i-make-bootstrap-navbar-change-active-state
$(document).ready(function() {
 var path = window.location.pathname;
 var links = ['home', 'welcome', 'login', 'register'];
$('.nav-item').each(function(i) {
 if (path.includes(links[i])) $(this).addClass('active');
 else if (this.className.includes('active')) $(this).removeClass('active');
});
});
