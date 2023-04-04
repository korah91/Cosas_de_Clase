window.onload = () => {
    // Conseguimos el dropbox

    var dropbox = document.getElementById("dropbox");
    var fileselect = document.getElementById("fileselect");

    // entras en esa capa arrastrando algo
    dropbox.addEventListener("dragenter", dragOver, false); 
    // sales de esa capa, Se elimina el hover
    dropbox.addEventListener("dragexit", dragOver, false); 
    // te mueves arrastrando algo en la capa
    dropbox.addEventListener("dragover", dragOver, false); 

    // sueltas los ficheros
    dropbox.addEventListener("drop", gestorFicheros, false); 
    // misma funcion para gestionar el evento pero este usando el boton para subir ficheros
    fileselect.addEventListener("change", gestorFicheros, false); 
    document.getElementById("enviar").addEventListener("click", validarFormulario);
}

function dragOver(evt) {
    // evita que el evento se propague a capas que contienen la capa actual de forma sucesiva
    evt.stopPropagation(); 
    // deshabilitar el comportamiento por defecto
    evt.preventDefault();
    // modifica la clase del elemento objetivo del evento, si arrastramos ficheros por encima le aplicamos la clase hover a ese elemento
    evt.target.className = (evt.type == "dragover" ? "hover" : "");
}

function gestorFicheros(e) {
    // cancelar evento y cambiar estilo destino
    dragOver(e);
    // obtener ficheros (FileList) del input (izquierda) o del drag&drop (derecha)
    var files;
    if (e.target === fileselect) {
        files = e.target.files;
    } else {
        files = e.dataTransfer.files;
    }
    // procesar todos los objetos File
    for (var i = 0, f; f = files[i]; i++) {
        parsearFichero(f);
    }
}

function parsearFichero(file) {
    document.getElementById('mensajes').innerHTML +=
    "<p>Datos del fichero: <strong>" + file.name +
    "</strong> Tipo: <strong>" + file.type +
    "</strong> Tamaño: <strong>" + file.size +
    "</strong> Bytes</p>";
}
    


// Cuando se pulsa el botón Enviar

function validarFormulario() {
    //evento.preventDefault();
    var nombre = document.getElementById("nombre").value;
    var nomCorrecto = false;
    var telfCorrecto = false;
    var correoCorrecto = false;
    var libCorrecto = false;
    var cantCorrecto = false;
    //console.log(nombre);
    //Campo de nombre obligatorio
    if(nombre.length == 0) {
        document.getElementById("nomAlerta").innerHTML="El campo del nombre es obligatorio";
        nomCorrecto=false;
    }
    else{
        document.getElementById("nomAlerta").innerHTML=" ";
        nomCorrecto=true;
    }
    //Campo del telefono
    var telefono = document.getElementById("telf").value;
    var regexTelf = /\d{3}-?\d{3}-?\d{3}-?/;
    if(!regexTelf.test(telefono)) {
        document.getElementById("tlfAlerta").innerHTML="El campo de teléfono debe contener el patrón 123(-)456(-)789";
        telfCorrecto=false;
    }
    else{
        document.getElementById("tlfAlerta").innerHTML=" ";
        telfCorrecto=true;
    }
    //Campo del correo
    var correo = document.getElementById("correo").value;
    var regexCorreo = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/;
    if(!regexCorreo.test(correo)) {
        document.getElementById("correoAlerta").innerHTML="El campo del e-mail es incorrecto. Debe tener el siguiente formato: hola@gmail.com";
        correoCorrecto=false;
    }
    else{
        document.getElementById("correoAlerta").innerHTML=" ";
        correoCorrecto=true;
    }

    //Campo del libro
    var libros = document.querySelector("#libros").value;
    if(libros.length==0) {
        document.getElementById("librosAlerta").innerHTML="- El campo del Libro es obligatorio";
        libCorrecto=false;
    }
    else{
        document.getElementById("librosAlerta").innerHTML=" ";
        libCorrecto=true;
    }
    
    var cantidad = document.getElementById("cantidad").value;
    if(cantidad < 1 || cantidad > 5) {
        document.getElementById("cantidadAlerta").innerHTML="- La cantidad debe ser un número del 1 al 5";
        cantCorrecto=false;
    }
    else{
        document.getElementById("cantidadAlerta").innerHTML=" ";
        cantCorrecto=true;
    }

    if (nomCorrecto && cantCorrecto && libCorrecto && correoCorrecto && telfCorrecto){
        console.log("Formulario enviado correctamente");
    }
}
