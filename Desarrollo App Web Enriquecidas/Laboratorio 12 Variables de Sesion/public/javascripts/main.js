window.onload = function() {
    let links = document.getElementsByClassName("deleteUser");
    for (let item of links) {
    	item.addEventListener("click", deleteUser);
    }
    
    // Ahora los botones de editar
    links = document.getElementsByClassName("editUser");
    for (let item of links) {
    	item.addEventListener("click", editUser);
    }

    // Boton para guardar cambios de un elemento
    //btn_edit = document.getElementsByName('submit')[0]
    //btn_edit.addEventListener('click', guardarCambios);
}

function deleteUser(event){
    var confirmation = confirm('Are You Sure?');
    if(confirmation){
        var url = '/users/delete/' + event.target.getAttribute('data-id');
        var consulta = new XMLHttpRequest();
        consulta.open("DELETE", url);
        consulta.onload = function() {
            if (consulta.status == 200) {
                window.location.replace('/')
            }
   	};
   	 consulta.send();
    } 
    
    else {
   	 return false;
    }
}

id_usuario = 0
// Se ejecuta cuando se pulsa Edit sobre un elemento
function editUser(event){
    

    

    var url = '/users/getUser/' + event.target.getAttribute('data-id');
    
    fetch(url).then( (response) => {
        return response.json()
    }).then( (respuesta) => {
        // Guardo el id para utilizarlo luego
        id_usuario = respuesta['_id']

        // Reemplazo el texto de los input
        document.getElementsByName("first_name")[0].value = respuesta['first_name']
        document.getElementsByName("last_name")[0].value = respuesta['last_name']
        document.getElementsByName("email")[0].value = respuesta['email']


        // Se cambia el boton a Edit
        document.getElementsByName("submit")[0].value = "Edit"
        document.getElementById('form').action = '/users/updateUser/'+id_usuario
    } )

    
}
/*
// Se usa para guardar los cambios
function guardarCambios(event) {
    if (event.target.value == 'Edit'){
        event.preventDefault();
        var usuario = {
            'first_name': document.getElementsByName("first_name")[0].value,
            'last_name': document.getElementsByName("last_name")[0].value,
            'email': document.getElementsByName("email")[0].value
        }

        var url = '/users/updateUser/' + id_usuario;
        
        console.log("Se ha pulsado el botón edit. Se manda el siguiente usuario a app.js "+url)

        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            // Hay que pasarlo a String primero. El JSON empieza con la key 'usuario', no empieza con
            // first_name, last_name o email
            body: JSON.stringify({
                'usuario': usuario
            })
        }).then(console.log(usuario))
        
    }
}
*/