$(function() {
  $('#main-navigation a').click(function() {
    $('#main-navigation a').removeClass('active-tab');
    $(this).addClass('active-tab');
    $('#partial-title').text($(this).text());
  });
  $('#partial-navigation a').click(function() {
    $('#partial-navigation a').removeClass('active-tab');
    $(this).addClass('active-tab');
  });
});