$('#menu-button').on('click', function() {
  $('#nav').slideToggle();
});
$( window ).resize(function() {
  if ($( window ).width() > 700) {
    $('#nav').show();
  }
});