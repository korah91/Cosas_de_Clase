x = document.getElementById("tres")
x.innerHTML = "Tres"


h4 = document.createElement("h4")
h4.innerHTML = "article section h4"
p = document.createElement("p")
p.innerHTML = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam sodales urna non odio egestas tempor. Nunc vel vehicula ante. Etiam bibendum iaculis libero, eget molestie nisl pharetra in. In semper consequat est, eu porta velit mollis nec. Curabitur posuere enim eget turpis feugiat tempor. Etiam ullamcorper lorem dapibus velit suscipit ultrices. Proin in est sed erat facilisis pharetra."

// Creamos la seccion
seccion = document.createElement("section")

// Anadimos los hijos
seccion.appendChild(h4)
seccion.appendChild(p)

// Anadimos el section despues del primer footer
footer = document.getElementsByTagName("footer")[0]
footer.insertAdjacentElement("afterend", seccion)


//Ejercicio 3: Cambiar el ultimo footer
footer = document.getElementsByTagName("footer")[1]
footer.innerHTML = "Este es el nuevo footer."

// Ejercicio 4
wrapers = document.getElementsByClassName("wrapper")
    // Cojo el ultimo
wraper = wrapers[wrapers.length - 1]
wraper.innerHTML += "Nueva actualización"

// Ejercicio 5
aside = document.getElementsByTagName("aside")[0]
aside.style.color = "black"
aside.style.backgroundColor = "white"

// Ejercicio 6 
var img = document.createElement("img");
img.src = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Big_%26_Small_Pumkins.JPG/2560px-Big_%26_Small_Pumkins.JPG";
var src = document.getElementsByTagName("article")[0];
img.height = 300
img.width = 300
src.appendChild(img)

// Ejercicio 7
d = document.getElementsByClassName("footer-container")[0]
d.insertAdjacentHTML("beforebegin", '<img src="https://dialprix.es/blog/wp-content/uploads/calabaza.jpg" width="300" height="300" style="display:block; margin-left:auto; margin-right:auto;">')


