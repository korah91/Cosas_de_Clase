window.onload = function() {
    var canvas = document.getElementById("lienzo");
    var ctx = canvas.getContext("2d");
    
    // Lienzo en el que se mostrara el lienzo original redimensionado
    var canvasZoom = document.getElementById("lienzoZoom");
    var ctxZoom = canvasZoom.getContext("2d");

    var img = new Image();
    img.src = "./spritesheet.png"

    img.onload = function(){
      // Anado la imagen
      ctx.drawImage(img, 0, 0);
    }

    canvas.addEventListener("mousemove", (e) => {
      ctxZoom.fillStyle = "white"
      ctxZoom.fillRect(0,0, canvasZoom.width, canvasZoom.height);

      // drawImage(imagen, sourceX, sourceY, sourceWidth, sourceHeigth, destinationX, destinationY, destinationWidth, destinationHeight)
      // destinationWidth y Height redimensiona la imagen al doble de la original
      ctxZoom.drawImage(canvas, e.x, e.y, 50, 50, 0, 0, 100, 100);

      canvasZoom.style.top = e.pageY + 10 + "px"
      canvasZoom.style.left = e.pageX + 10 + "px"
      
      console.log("x: "+canvasZoom.style.top + ", y: " +canvasZoom.style.left)
      canvasZoom.style.display = "block";
    })
    
    canvas.addEventListener("mouseout", (e) => {
      canvasZoom.style.display = "none";
    })
  }; 

