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
      if (x > img.width - canvasZoom.width) {
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
      
      // Se crea la lupa
      ctxZoom.fillStyle = "white"
      ctxZoom.fillRect(0,0, canvasZoom.width, canvasZoom.height);

      // drawImage(imagen, sourceX, sourceY, sourceWidth, sourceHeigth, destinationX, destinationY, destinationWidth, destinationHeight)
      // destinationWidth y Height redimensiona la imagen al doble de la original
      ctxZoom.drawImage(canvas, x, y, 50, 50, 0, 0, 100, 100);

      
      // Posicion en la que se utiliza la lupa
      canvasZoom.style.left = x - canvasZoom.width + "px"
      canvasZoom.style.top = y - canvasZoom.height + "px"
      
      
      console.log("("+canvasZoom.style.left + ", " +canvasZoom.style.top+")")
      canvasZoom.style.display = "block";

        
      ctx.fillRect(x)
    });
}    

