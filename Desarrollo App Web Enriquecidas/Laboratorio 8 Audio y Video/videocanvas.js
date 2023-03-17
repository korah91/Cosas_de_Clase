var efecto = null;
var clip = "video/demovideo1"; // nombre del vídeo, sin extensión
var rotar = false
var ang = 1;

window.onload = function() {

	var video = document.getElementById("video");
	var botonByN = document.getElementById("byn");
	botonByN.onclick = cambiarEfecto;
	var botonNormal = document.getElementById("normal");
	botonNormal.onclick = cambiarEfecto;
				
	video.addEventListener("play", procesarFrame, false);
	
	video.src = clip + getFormatExtension();
	video.load();
	video.play();
	


	// BOTON PAUSA
	var botonPause = document.getElementById("pause");
	botonPause.onclick = () => {
		if(video.paused) {
			video.play()
		}
		else{
			video.pause();
		}
	}

	// BOTON CIENCIAFICCION
	var botonCienciaFiccion = document.getElementById("cienciaFiccion");
	
	botonCienciaFiccion.onclick = cambiarEfecto;


	// BOTON ROTAR
	
	var botonRotate = document.getElementById("rotate");
	botonRotate.onclick = () => {
		rotar = true;
	}

	// BOTON AUDIO 
	var botonAudio = document.getElementById("audiobtn");
	botonAudio.onclick = () => {
		loadAudio("audio/soundtrack.mp3").then( audio => audio.play());
	}

	// BOTON PIP
	var botonPip = document.getElementById("pip");
	botonPip.onclick = () => {
		botonPip.disabled = true;
		try {
			video.requestPictureInPicture();
		} 
		catch (error) {
			console.log(error)
		} 
		finally {
			botonPip.disabled = false;
		}
		
	}

}

function cambiarEfecto(e){
	var id = e.target.getAttribute("id");
	if ( id == "byn" ){
		efecto = byn;
	} 
	else if ( id == "cienciaFiccion") {
		efecto = scifi;
	}
	else{
		efecto = null;
		rotar = false;
	}
}

function getFormatExtension() {
	var video = document.getElementById("video");
	if (video.canPlayType("video/mp4") != "") {
		return ".mp4";
	} 
	else if (video.canPlayType("video/ogg") != "") {
		return ".ogv";
	}
	else if (video.canPlayType("video/webm") != "") {
		return ".webm";
	} 
}


function procesarFrame(e) {
	var video = document.getElementById("video");

	if (video.paused || video.ended) {
		return;
	}

	var bufferCanvas = document.getElementById("buffer");
	var displayCanvas = document.getElementById("display");
	var buffer = bufferCanvas.getContext("2d");
	var display = displayCanvas.getContext("2d");


	
	if (rotar){
		console.log(ang)
		
		// Se guarda el estado del canvas para recuperarlo en restore
		buffer.save();
		// Clear the canvas
		//buffer.clearRect(0, 0, bufferCanvas.width, bufferCanvas.height);	
		// Move registration point to the center of the canvas
		buffer.translate(bufferCanvas.width/2, bufferCanvas.height/2);
			
		// Rotate 1 degree
		buffer.rotate(Math.PI / 180 * (ang += 1));
		ang+=1
		// Move registration point back to the top left corner of canvas
		buffer.translate(-bufferCanvas.width/2, -bufferCanvas.width/2);
		
		
	}

	
	
	buffer.drawImage(video, 0, 0, bufferCanvas.width, bufferCanvas.height);
	var frame = buffer.getImageData(0, 0, bufferCanvas.width, bufferCanvas.height);
	var length = frame.data.length / 4;

	for (var i = 0; i < length; i++) {
		var r = frame.data[i * 4 + 0];
		var g = frame.data[i * 4 + 1];
		var b = frame.data[i * 4 + 2];
		if (efecto){		
			efecto(i, r, g, b, frame.data);
		}
	}

	
	display.putImageData(frame, 0, 0)
	// Se restaura el estado del canvas
	buffer.restore();	

	setTimeout(procesarFrame, 0);
	// en los navegadores modernos, es mejor usar :
	// requestAnimationFrame(procesarFrame);

}

function byn(pos, r, g, b, data) {
	var gris = (r+g+b)/3;

	data[pos * 4 + 0] = gris;
	data[pos * 4 + 1] = gris;
	data[pos * 4 + 2] = gris;
}

function scifi(pos, r, g, b, data) {
	var offset = pos * 4;
	data[offset] = Math.round(255 - r);
	data[offset+1] = Math.round(255 - g) ;
	data[offset+2] = Math.round(255 - b) ;
}
	


// Funcion para cargar el audio
function loadAudio(url) {
	return new Promise(resolve => {
		const audio = new Audio(url);
		audio.addEventListener('loadeddata', () => {
			console.log("a")
			resolve(audio);
		});
	});
}

