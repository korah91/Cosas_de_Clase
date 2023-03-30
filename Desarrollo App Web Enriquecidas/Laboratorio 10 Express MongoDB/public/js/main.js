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



function editUser(event){
    

    // Se cambia el boton a Edit
    document.getElementsByName("submit")[0].value = "Edit"

    

    var url = '/users/getUser/' + event.target.getAttribute('data-id');
    
    fetch(url).then( (response) => {
        return response.json()
    }).then( (respuesta) => {
        document.getElementsByClassName("first_name")[0].value = respuesta['first_name']
    } )


}
