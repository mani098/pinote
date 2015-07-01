// $(window).load(function() {

// });
// $(document).ajaxComplete(function() {
// 	$("#pre-loader").delay(500).fadeOut();
// 	console.log("loaded");
//   // $( ".log" ).text( "Triggered ajaxComplete handler." );
// });

$(document).ready(function(){
    var main_wrap_height =  $(document).height() - $(".navbar-header").outerHeight() - $(".pinote-module").outerHeight() - 31;
    $(".main-wrap").css("min-height", main_wrap_height + "px");
});
