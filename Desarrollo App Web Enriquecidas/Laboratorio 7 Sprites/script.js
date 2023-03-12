window.onload = function() {
    var canvas = document.getElementById("lienzo");
    var ctx = canvas.getContext("2d");
    
    // Lienzo en el que se mostrara el lienzo original redimensionado
    var canvasZoom = document.getElementById("lienzoZoom");
    var ctxZoom = canvasZoom.getContext("2d");

    x = 0
    y = 0


    var img = new Image();
    img.src = "./spritesheet.png"

    img.onload = function(){
      // Anado la imagen
      ctx.drawImage(img, 0, 0);
    }

    // Evento cuando se pulsa una flecha
    document.addEventListener("keydown", (e) => {
      switch (e.key) {
        case "ArrowDown":
            y = y+15
            break;
        case "ArrowUp":
            y = y-15
            break;
        case "ArrowLeft":
            x = x-15
            break;
        case "ArrowRight":
            x = x+15
            break;
      }
      
      // La lupa no se puede salir de los bordes de la imagen
      if (x > img.width - canvasZoom.width  + 27) {
        x = img.width - canvasZoom.width;
        console.log(x, img.width)
      }
      if (x < 0) {
        x = 0;
      }
      if (y > img.height - canvasZoom.height) {
        y = img.height - canvasZoom.height;
      }
      if (y < 0) {
        y = 0;
      }

      // Se vuelve a pintar el canvas
      ctx.clearRect(0, 0, canvas.width, canvas.height)
      ctx.drawImage(img, 0, 0)

      // Se crea la lupa
      ctxZoom.fillStyle = "white"
      ctxZoom.fillRect(0,0, canvasZoom.width, canvasZoom.height);

      // drawImage(imagen, sourceX, sourceY, sourceWidth, sourceHeigth, destinationX, destinationY, destinationWidth, destinationHeight)
      // destinationWidth y Height redimensiona la imagen al doble de la original
      ctxZoom.drawImage(canvas, x, y, 50, 50, 0, 0, 100,100);


      // Se dibuja el delimitador del recinto seleccionado
      ctx.beginPath()
      ctx.moveTo(x, y)
      ctx.lineTo(x, y)
      ctx.lineTo(x + canvasZoom.width, y)
      ctx.lineTo(x + canvasZoom.width, y + canvasZoom.height)
      ctx.lineTo(x, y + canvasZoom.height)      
      ctx.closePath()
      ctx.lineWidth = 3
      ctx.strokeStyle = "green"
      ctx.stroke();

      // Posicion en la que se utiliza la lupa
      canvasZoom.style.left = x  + "px"
      canvasZoom.style.top = y  + "px"
      
      
      console.log("("+canvasZoom.style.left + ", " +canvasZoom.style.top+")")
      canvasZoom.style.display = "block";

      
      //ctx.fillRect(x)
    });
}    

