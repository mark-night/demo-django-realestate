const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// fade out messages after 3 seconds
setTimeout(function () {
  $('#messages').fadeOut(1000);
}, 3000);
