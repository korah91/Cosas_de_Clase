var express = require("express")
const { check, validationResult } = require('express-validator');
var path = require("path"); // viene por defecto en Node

const mongojs = require('mongojs')
var ObjectId = mongojs.ObjectId;
const db = mongojs('clientespp', ['users'])


app = express();
app.listen(3000, function(){ // a la escucha en el puerto 3000
	console.log("Servidor lanzado en el puerto 3000");
});

// View Engine
app.set('view engine', 'ejs'); // motor de plantillas
app.set('views', path.join(__dirname, "views")); // carpeta donde guardar las vistas

    

var logger = function(res, req, next) { // next es el siguiente middleware o finalmente enrutamiento
	console.log("Logging…");
	next(); 
};
app.use(logger);

// declaracion y definicion de variables globales
app.use(function (req, res, next) {
    res.locals.errors = null;
    next();
});


/* Middleware que recoge los datos en crudo y los parsea a formato JSON, dejándolos en un atributo nuevo (request.body) */
app.use(express.json()); 

// Middleware que parsea datos que lleguen en la petición HTTP y los deje como un objeto JSON
app.use(express.urlencoded({extended: false})); 

// Middleware que carga ficheros estaticos de un directorio (public en este caso)
app.use(express.static(path.join(__dirname, "public")));


// Anadir usuario
app.post('/users/add', 
	[
	check("first_name", "El nombre es obligatorio").notEmpty(),
    check("last_name", "El apellido es obligatorio").notEmpty(),
    check("email", "El email es obligatorio").notEmpty()

	], 
	function(req, res){ // fijaos que usamos post
		const errors = validationResult(req); // obtenemos los posibles errores
		if (!errors.isEmpty()) { // en caso de que el array de errores contenga algun error
			console.log("Hay errores");
			res.render('index', {
				title:'clientes',
				users: users,
				errors: errors.array()
			});	
		} 
		else {
			// Obtenemos el usuario del formulario
			var newUser = {
				"first_name" : req.body.first_name,
				"last_name" : req.body.last_name,
				"email" : req.body.email,
			};
			// Se inserta el nuevo usuario
			db.users.insertOne(newUser, function(err, resp) {
				if(err) {
					console.log(err);
				} else {
					db.users.insertOne(newUser);
				}
				res.redirect('/');
			});
	
			console.log(newUser);
	
		console.log(req.body.first_name); // para probar inicialmente que la peticion llega
	}
});

// Se ejecuta cuando se manda DELETE a /users/delete
app.delete('/users/delete/:id', function(req, res) {
    db.users.remove({_id: ObjectId(req.params.id)}, function(err, result) {
	if(err) {
		console.log(err);
	}
	res.redirect(303, '/');
    });
});





// Enrutamiento
app.get("/", function(req, res) {  // peticion y respuesta como parametros
    // para rellenar la plantilla
	db.users.find(function(err, docs) {
   	 if(err) {
   		 console.log(err);
   	 } else {
   		 console.log(docs); // lo que mongodb nos devuelva
   		 // para rellenar la plantilla
   		 res.render('index', {
   		    title: 'clientes',
   		    users: docs // cambiamos users por docs
   		 });
	}
         });
});


