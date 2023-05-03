const serverURL = window.location.hostname + ":" +  window.location.port;

// Solo se va a acceder a sockets.js desde desktop

function setupSockets(){
    const socket = io.connect(serverURL, {secure: true});

    socket.emit('phone-connect');

    socket.onopen = function(){
        console.log("Socket conectado!");
    }
    
    socket.send("movimiento válido");
    
    
}
