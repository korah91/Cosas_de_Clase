// Consigo el boton
var btn_obtenerDatos = document.getElementById("btn_obtenerDatos");

btn_obtenerDatos.onclick =  () => {// Consigo el valor elegido en el combobox
    var e = document.getElementById('combobox').value;

    let url = "https://openlibrary.org/api/books?bibkeys=ISBN:" + e + "&jscmd=details&format=json"


    console.log(e);

    fetch(url, {method: 'GET'}).then(function(response) { 
        return response.json(); }).then(function(json) {
            let titulo = json["ISBN:" + e]["details"]["title"]
            let autores = []
            autores = json["ISBN:" + e]["details"]["authors"].map( autor => autor.name)
            thumbnail_url = json["ISBN:" + e]["thumbnail_url"]
            
            // Cambiamos la S por una L
            var arreglo = [...thumbnail_url];
            arreglo[ arreglo.length-5 ] = "M";
            thumbnail_url = arreglo.join("");
            
            // Creamos la imagen
            imagen = new Image()
            imagen.src = thumbnail_url

            console.log(json);
            
            // Rellenamos la tabla
            td1 = document.getElementById("td1")
            td1.innerHTML = titulo
            td2 = document.getElementById("td2")
            td2.innerHTML = autores
            td3 = document.getElementById("td3")
            td3.innerHTML = '<img src=' + thumbnail_url + ' >'

            console.log(thumbnail_url)
            
        });
}


