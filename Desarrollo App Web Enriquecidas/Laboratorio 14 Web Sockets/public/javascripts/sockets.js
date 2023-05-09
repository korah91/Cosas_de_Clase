const serverURL = window.location.hostname + ":" +  window.location.port;

// Solo se va a acceder a sockets.js desde desktop

function setupSockets(){
    const socket = io.connect(serverURL, {secure: true});

    socket.emit('desktop-connect');

    socket.onopen = function(){
        console.log("Socket conectado!");
    }
    
    // Creo que si tomo gamma puedo ir de arriba a abajo
    socket.on('phone-move', function(beta) {
        if (beta<0){
            pulsarTecla('ArrowLeft')
        }
        if (beta>0){
            pulsarTecla('ArrowRight')
        }
    });
}
// Exporto la funcion
export { setupSockets };