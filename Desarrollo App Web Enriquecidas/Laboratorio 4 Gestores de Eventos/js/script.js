function inicializarGestores()
{
	var imagen = document.getElementById("imagen");
	imagen.onclick = function()
	{
		alert("Has pulsado la imagen");
		clearInterval(timeout);
	}

	var usuario = document.getElementById("usuario");
	usuario.value = 'tu@email';

	usuario.onblur = function(){
		if (usuario.value == ''){
			usuario.value = "tu@email";
		}
	}

	usuario.onfocus = function(){
		if (usuario.value == 'tu@email'){
			usuario.value = '';
		}
	}

	var item = document.getElementById("combobox");
	item.addEventListener("change",gestorCombo);

	function gestorCombo(){
		console.log(item.value);
		console.log(item.options[item.selectedIndex].text);
		console.log(item.selectedIndex);
	} 

	var formulario = document.getElementById('formulario');
	formulario.onsubmit = function(){
		console.log("click en submit");
		return false;
	}

}



files_original = ["fresas.jpg", "limon.jpg", "mandarinas.jpg", "manzanas.jpg", "melon.jpg", "sesamo.jpg"]
files = []

function cambio()
{
	// Si se ha terminado el bucle vuelvo a leer las imagenes desde la primera
	if(files.length == 0){
		// Copio el array
		files = files_original.slice()
	}

	// Cojo la primera y la elimino del array
	imagen_a_leer = files.shift()

	var imagen = document.getElementById("imagen");
	console.log(imagen_a_leer)

	imagen.style.backgroundImage = "url(../imagenes/" + imagen_a_leer + ")"
}



console.log(files_original)
// Creo el timeout
const timeout = setInterval(cambio, 1000);



window.onload = inicializarGestores;
