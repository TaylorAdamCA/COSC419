



$(document).ready(function () {
var res = 20;

  var xhr = $.get("http://api.giphy.com/v1/gifs/random?api_key=tcj6KeeEq5yEHdQJ4z7tBi44m4C4p7FU");
  xhr.done(function(data) {

 console.log("success got data", data); 
  var gifs = data.data;
 // for (i in gifs) {
       $('.text-center').append("<img src='"+gifs.images.original.url+"'/>")
//}});

})});
