$(document).ready(function() {
 var path = window.location.pathname;
 var links = ['home', 'welcome', 'login', 'register'];
$('.nav-item').each(function(i) {
 console.log(path);
 if (path.includes(links[i])) $(this).addClass('active');
 else if (this.className.includes('active')) $(this).removeClass('active');
});
});
