window.onload = function() {
    var canvas = document.getElementById("lienzo");
    var ctx = canvas.getContext("2d");
    
    var img = new Image();
    img.src = "spritesheet.png"
    // Anado la imagen
    lienzo.appendChild(img)
    ctx.drawImage(img, 10, 10);
  }; 

