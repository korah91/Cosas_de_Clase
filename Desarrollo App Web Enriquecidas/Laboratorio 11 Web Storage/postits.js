/* postits.js
 *
 */
var num_nota
// Lleva la cuenta del numero de notas creadas
var num_notas

window.onload = init;

function init() {
	var button = document.getElementById("add_button");
	button.onclick = createSticky;

	// cargar las notas postit de localStorage  
	// cada nota se guarda como un par así: postit_X = texto_de_la_nota
	// donde X es el número de la nota
	// por cada una de ellas, llamar al método
	// addStickyToDOM(texto_de_la_nota);

	// Si no hay notas se pone num_notas a 0
	num_notas = localStorage.getItem("num_notas")
	if (num_notas == 'null'){
		num_notas = 0
	}
	num_nota = 1

	var button_clear = document.getElementById("clear_button")
	button_clear.onclick = clearStickyNotes;

	recoverStickyNotes()
	actualizarEspacioUtilizado();
}

function createSticky() {
	var value = document.getElementById("note_text").value;
	
        // crear la nota con nombre postit_X, donde X es un número entero
	// (postit_1, postit_2, ...)  y guardarla en el localStorage
	
	num_notas ++
	addStickyToDOM(value);
	actualizarEspacioUtilizado();
}


function addStickyToDOM(value) {
	var stickies = document.getElementById("stickies");
	var postit = document.createElement("li");
	var span = document.createElement("span");
	span.setAttribute("class", "postit");
	span.innerHTML = value;
	postit.appendChild(span);
	stickies.appendChild(postit);

	// Se guarda el valor en localStorage
	localStorage.setItem("postit_" + num_nota, value)
	num_nota ++
	

	// Guardo el numero total de notas para luego poder saber cuantas sacar
	localStorage.setItem('num_notas', num_notas)
}

function clearStickyNotes() {
	// Crear un nuevo botón en la ventana de postit notes que al pulsarlo,
	// elimine las notas de pantalla y de localStorage
	// Algoritmo:	
	// obtener una referencia a la capa "stickies"
	// recorrer los hijos (childNodes) de esa referencia,
	// eliminándolos uno a uno (removeChild)
	
	var stickies = document.getElementById("stickies");

	// Se eliminan sus hijos
	while (stickies.firstChild){
		stickies.removeChild(stickies.firstChild)
	}

	localStorage.clear()
	num_notas = 0
	num_nota = 1
	actualizarEspacioUtilizado()
}


function recoverStickyNotes(){

	// Recupero el total de notas de antes
	let num_notas_aux = localStorage.getItem('num_notas')
	console.log("num_notas -> "+num_notas + " num_notas_aux -> "+num_notas_aux)

	// Recupero cada nota que habia antes
	for(let i = 1; i <= num_notas_aux; i++){
		value = localStorage.getItem("postit_" + i)
		console.log("Se recupera postit_" + i + ": " + value);
		num_nota = i
		addStickyToDOM(value)
	}
}

// Funcion que actualiza el div para que siempre muestre los kilobytes
function actualizarEspacioUtilizado(){
	div = document.getElementById("divEspacio");

	espacioTotal = 0
	
	// Conseguimos cada par almacenado en localStorage
	for(let i = 0; i < localStorage.length; i++){	
		let key = localStorage.key(i);
		let value = localStorage.getItem(key);

		// Un caracter ocupa 16 bits = 2 bytes. Queremos bytes
		espacioTotal += (key.length + value.length) * 2
	}
	div.innerHTML = 'Espacio utilizado:' + (espacioTotal / 1024).toFixed(2) + " KB"
}