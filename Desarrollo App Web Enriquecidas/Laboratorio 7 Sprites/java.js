var x = 0;
var y = 0;

window.onload = function() {
    var lienzo = getLienzo("lienzo");
    
    var logo = new Image();
    logo.onload = function() {
        lienzo.drawImage(logo, 0, 0); // imagen y coordenadas de posicion
        crearCuadrado(lienzo,x,y);
        pintarTexto(lienzo,x,y); 
    };
    logo.src = "spritesheet.png";
    var miniLogo = new Image();
    miniLogo.onload = function() {
        lienzo.drawImage(miniLogo, 0, 0, 30, 40,logo.height+5,0,50,60); // imagen y coordenadas de posicion
    };
    miniLogo.src = "spritesheet.png";

    document.addEventListener('keydown', e =>{
		if(e.key == "ArrowUp")
		{
            if(y-10 >= 0){
                y = y - 10;
            }
        }
        else if(e.key == "ArrowDown"){
            if(y+50 <= logo.height){
                y = y + 10;
            }
        }
        else if(e.key == "ArrowRight"){7
            if(x+40 <= logo.width){
                x = x + 10;
            }
        }
        else if(e.key == "ArrowLeft"){
            if(x-10 >= 0){
                x = x - 10;
            } 
        }
        var canva = document.getElementById("lienzo");
        lienzo.clearRect(0,0,canva.width,canva.height);
        lienzo.drawImage(logo,0,0);
        lienzo.drawImage(miniLogo, x, y, 30, 40,logo.height+5,0,50,60);
        crearCuadrado(lienzo,x,y);
        pintarTexto(lienzo,x,y);
		}
	);

   
}

function getLienzo(x){
    var canvas = document.getElementById(x);
    if (canvas.getContext) {
        var lienzo = canvas.getContext("2d");   
        return lienzo;
    } else
        return false;
}

function crearCuadrado(lienzo,x,y){
    lienzo.beginPath();
    lienzo.moveTo(x,y);
    lienzo.lineTo(x,y);
    lienzo.lineTo(x,y+40); 
    lienzo.lineTo(x+30,y+40);
    lienzo.lineTo(x+30,y);
    lienzo.closePath(); // genera una linea recta desde nuestra ultima posicion a la primera posicion 
    lienzo.lineWidth = 2; // especificamos el ancho de las lineas
    lienzo.strokeStyle = "red";
    lienzo.stroke();
}

function pintarTexto(context,x,y){
    // definimos el estilo del texto
	context.font = "bold 12px sans-serif";
    
    // alineacion vertical: definimos donde se coloca el texto respecto a la posicion que indicamos en la funcion "fillText". Al indicar "top", el punto esta por encima del texto. Dibujamos un punto verde para indicar la posicion del punto en cuestion
    //context.fillStyle = "black";
    //context.textAlign = "right";
    //context.textBaseline = "bottom"; 
    context.fillText("( " + x + "," + y + ")", 430, 20); // lo ponemos cercano al limite pero no en este para poder visualizar el texto
}