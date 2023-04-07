/* postits.js
 *
 */
var num_nota = 1
// Lleva la cuenta del numero de notas creadas
var num_notas = 0

window.onload = init;

function init() {
	var button = document.getElementById("add_button");
	button.onclick = createSticky;

	// cargar las notas postit de localStorage  
	// cada nota se guarda como un par así: postit_X = texto_de_la_nota
	// donde X es el número de la nota
	// por cada una de ellas, llamar al método
	// addStickyToDOM(texto_de_la_nota);

	var button_clear = document.getElementById("clear_button")
	button_clear.onclick = clearStickyNotes;

	recoverStickyNotes()
}

function createSticky() {
	var value = document.getElementById("note_text").value;
	
        // crear la nota con nombre postit_X, donde X es un número entero
	// (postit_1, postit_2, ...)  y guardarla en el localStorage
	
	// Se guarda el valor en localStorage
	localStorage.setItem("postit_" + num_nota, value)
	num_nota ++
	num_notas ++

	// Guardo el numero total de notas para luego poder saber cuantas sacar
	localStorage.setItem('num_notas', num_notas)
	addStickyToDOM(value);
}


function addStickyToDOM(value) {
	var stickies = document.getElementById("stickies");
	var postit = document.createElement("li");
	var span = document.createElement("span");
	span.setAttribute("class", "postit");
	span.innerHTML = value;
	postit.appendChild(span);
	stickies.appendChild(postit);
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
	
}


function recoverStickyNotes(){

	let num_notas_aux = localStorage.getItem('num_notas')
	for(var i = 0; i < num_notas_aux; i++){
		value = localStorage.getItem("postit_" + num_notas_aux)
		addStickyToDOM(value)
	}
}