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
    } else {
   	 return false;
    }
}



function editUser(event){
    
    document.getElementsByName("submit").value = "Edit"

    var url = '/users/edit/' + event.target.getAttribute('data-id');
    var consulta = new XMLHttpRequest();
    consulta.open("GET", url);
    consulta.onload = function() {
        if (consulta.status == 200) {
            window.location.replace('/')
        }
    };
    consulta.send();
    } else {
   	 return false;
    }
}
