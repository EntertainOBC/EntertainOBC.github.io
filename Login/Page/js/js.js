$(document).ready(function() {

  var users = ["ESL_SC2", "OgamingSC2", "cretetion", "freecodecamp", "brianamarie132", "storbeck", "terakilobyte", "habathcx", "RobotCaleb", "thomasballinger", "noobs2ninjas", "beohoff", "brunofin", "comster404"];

  // Display the Twitch.TV stream status for each user
  for (var i = 0; i < users.length; i++) {
    showStatus(users[i]);
  }
  
  $('#all').click(function() {
    $('.online').show();
    $('.offline').show();
  });
  
  $("#on").click(function() {
      $('.offline').hide();
      $('.online').show();
  });

  $("#off").click(function() {
      $('.online').hide();
      $('.offline').show();
  });
});

function showStatus(username) {

  $.getJSON('https://api.twitch.tv/kraken/streams/' + username + '?callback?', function(data) {
    if (data.stream) {
      $('.media-list').append(
        '<li class="media online"><div class="media-left"><a href="' + data.stream.channel.url +
        '" target="_blank"><img class="media-object" src="' + data.stream.channel.logo +
        '" alt="?"></a></div><div class="media-body"><a href="' + data.stream.channel.url +
        '" target="_blank"><p class="media-heading">' + data.stream.channel.display_name +
        '</p></a><p class="media-status">' + data.stream.channel.status +
        '</p></li>');
    } else {
      $.getJSON(data._links.channel, function(channel) {
        if(channel.logo == null) {
          channel.logo = 'http://placehold.it/75?text=?';
        }
        $('.media-list').append(
          '<li class="media offline"><div class="media-left"><a href="' + channel.url +
          '" target="_blank"><img class="media-object" src="' + channel.logo +
          '" alt="?"></a></div><div class="media-body"><a href="' + channel.url +
          '" target="_blank"><p class="media-heading">' + channel.display_name +
          '</p></a><p class="media-status"><em>Offline</em></p></li>');
      });
    }
  }).fail(function() {
    $('.media-list').append(
      '<li class="media offline"><div class="media-left"><img class="media-object" src="http://placehold.it/75?text=?" alt="?"></div><div class="media-body"><p class="media-heading">' + username +
      '</p></a><p class="media-status"><em>Account closed</em></p></li>');
  });
}