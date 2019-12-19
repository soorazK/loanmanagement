var loginform =$(".delform");
$('#loginb').click(function () {
	$('#right').empty();
	$('#right').append(loginform);
	// body...
});


// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
btn.onclick = function() {
$('.delform').remove();

    $(modal).slideDown();
  
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    $(modal).slideUp();
	$('#right').append(loginform);

}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    // modal.style.display = "none";
    $(modal).slideUp();
	$('#right').append(loginform);

  }
}


// show and hide the dropdown menu
$('#dropdownmenu').click(function()
{   
    $("#dropdown-content").toggle(500);  

});
// hide dropdown content when user click option
    $('#dropdown-content').click(function () {
	$('#dropdown-content').slideUp();
	// body...
});
