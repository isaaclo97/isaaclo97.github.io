$(document).ready(function () {
	$("#sidebar").mCustomScrollbar({
		theme: "minimal"
	});

	$('#dismiss, .overlay').on('click', function () {
		$('#sidebar').removeClass('active');
		$('.overlay').removeClass('active');
	});

	$('#sidebarCollapse').on('click', function () {
		$('#sidebar').addClass('active');
		$('.overlay').addClass('active');
		$('.collapse.in').toggleClass('in');
		$('a[aria-expanded=true]').attr('aria-expanded', 'false');
	});
	
	$(document).keydown(function(e){
    if (e.keyCode == 39) { //right arrow
	  document.getElementById("GameNextMoves").click();
      return false;
    } else if (e.keyCode == 37) { //left arrow
      document.getElementById("GamePrevMoves").click();
      return false;
    } 
  });
});