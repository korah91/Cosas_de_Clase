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