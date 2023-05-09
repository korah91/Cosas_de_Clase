import {setupSockets} from "./sockets.js";



// Este es el js de Desktop
window.onload = function(){

    // Llamo a la funcion importada
    setupSockets()


    


    const canvas = document.getElementById('canvas');
    const context = canvas.getContext("2d");
    var x = 0;
    var y = 0;
    var img_w = 0; // anchura spritesheet
    var img_h = 0; // altura spritesheet
    var speed = 10; // velocidad de desplazamiento de la ventana
    var window_w = 25; // anchura de la ventana
    var window_h = 35; // altura de la ventana
    var offset_fixed_window = 10; // espacio entre el spritesheet y la ventana fija de la derecha

    // Este es el script del desktop

    var logo = new Image();
    logo.src = '/../img/spritesheet.png';
    
    logo.onload = function(){

        console.log(logo)

        context.drawImage(logo, 0, 0); // dibujar el spritesheet
        img_w = this.width;
        img_h = this.height;
        context.drawImage(logo, x, y, window_w, window_h, img_w+offset_fixed_window, 0, 2*window_w, 2*window_h); // dibujar la ventana fija donde se visualiza el contenido de la ventana
    };
    document.onkeydown = function pulsar(tecla){
        canvas.width=canvas.width; //Para que no se quede atascado en el borde. Borra tambien todo el contenido del canvas.
        context.lineWidth = "2";
        tecla.preventDefault();
        switch(tecla.code){

            case "ArrowLeft":
                if(x>0){
                    x=Math.max(0,x-speed);
                }
                // Si esta al limite vibra el telefono
                else{
                    socket.emit('crash');
                }
                break;//izquierda
            case "ArrowUp":
                if(y>0){
                    y=Math.max(0, y-speed);
                }
                // Si esta al limite vibra el telefono
                else{
                    socket.emit('crash');
                }
                break;  
            case "ArrowRight":
                //if(x+27<476)
                if(x+window_w<img_w){
                    x=Math.min(img_w-window_w-1, x+speed);
                }
                // Si esta al limite vibra el telefono
                if (x==450){
                    socket.emit('crash');
                }
                
                break;
            case "ArrowDown":
                if(y+window_h<img_h){
                    y=Math.min(img_h-window_h-1, y+speed);
                }
                // Si esta al limite vibra el telefono
                if (y == 444){
                    socket.emit('crash');
                }
                break;
        }     
        
        context.drawImage(logo, 0, 0); // dibujar el spritesheet
        context.rect(x, y, window_w, window_h); // dibujar la ventana en su nueva posicion
    
        context.drawImage(logo, x, y, window_w, window_h, img_w+offset_fixed_window, 0, 2*window_w, 2*window_h); // dibujar la ventana fija redimensionada

        context.strokeStyle = "red";
        context.fillText("("+x+","+y+")", 435, 10); // texto que muestra la posicion actual
        context.stroke();
    }
}

function pulsarTecla(tecla){
    // Primero simulamos que pisamos la tecla
    window.dispatchEvent(
        new KeyboardEvent('keydown',
            {key: tecla //ArrowLeft, ArrowDown...
        })
    );
    // Y luego que dejamos de pisarla (levantamos el dedo)
    window.dispatchEvent(
        new KeyboardEvent('keyup',
            {key: tecla
        })
    );
}