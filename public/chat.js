//Make connection
var socket = io.connect('http://localhost:4000');

// Query DOM
var message = document.getElementById('message'),
      handle = document.getElementById('handle'),
      language = document.getElementById('language');
      btn = document.getElementById('send'),
      output = document.getElementById('output');

// Emit events
btn.addEventListener('click', function(){
  socket.emit('chat', {
      message: message.value,
      handle: handle.value,
      language: language.value
  });
  message.value = "";
});

// Listen for events
socket.on('chat', function(data){
    //google translate message

    output.innerHTML += '<p><strong>' + data.handle + ': </strong>' + data.message + '</p>';
});