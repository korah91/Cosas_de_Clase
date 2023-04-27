var express = require("express")
var router = express();
var session = require('express-session')

const { check, validationResult } = require('express-validator');
var path = require("path"); // viene por defecto en Node

const mongojs = require('mongojs')
var ObjectId = mongojs.ObjectId;
const db = mongojs('clientespp', ['users'])
router.use(express.static(path.join(__dirname, "public")));

// View Engine
router.set('view engine', 'ejs'); // motor de plantillas
router.set('views', path.join(__dirname, "../views")); // carpeta donde guardar las vistas

// Middleware para el parseo de req.body
router.use(express.json()); // coge los datos en crudo y los pasa a json

// Que parsee datos que lleguen en la query HTTP y los deje como un objeto JSON
router.use(express.urlencoded({extended: false}));

// Declaracion y definicion de variables globales: en este caso errors
router.use(function (req, res, next) {
  res.locals.errors = null;
  next();
});

// Anadir usuario
router.post('/add', 
	[
	check("first_name", "El nombre es obligatorio").notEmpty(),
    check("last_name", "El apellido es obligatorio").notEmpty(),
    check("email", "El email es obligatorio").notEmpty()

	], 
	function(req, res){ // fijaos que usamos post
		const errors = validationResult(req); // obtenemos los posibles errores
		if (!errors.isEmpty()) { // en caso de que el array de errores contenga algun error
			console.log("Hay errores");
			res.render('users', {
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

// Se ejecuta cuando se manda GET a /users/getUser
router.get('/getUser/:id', function(req, res) {
	db.users.findOne({
		_id: ObjectId(req.params.id)
	}, function(err, result) {
		if(err){
			console.log(err);
		}
		res.send(result)
	})
})

// Se ejecuta cuando se manda UPDATE a /users/updateUser/
router.post('/updateUser/:id', [
	check("first_name", "El nombre es obligatorio").notEmpty(),
    check("last_name", "El apellido es obligatorio").notEmpty(),
    check("email", "El email es obligatorio").notEmpty()

	], 
	function(req, res){
		const errors = validationResult(req); // obtenemos los posibles errores
		if (!errors.isEmpty()) { // en caso de que el array de errores contenga algun error
			console.log(req.body)
			res.render('users', {
				title:'clientes',
				users: usuarios,
				errors: errors.array()
			});
		} 
		else {
			db.users.findAndModify({
				// Busca el cliente con el mismo id exacto
				query: 
					{ _id: ObjectId(req.params.id) },
				// Lo actualiza
				update: 
					{ $set: { 'first_name': req.body.first_name } }
				}, 
				function(err, result) {
					if(err){
						console.log(err)
					}
					
				}
			)
		}
		res.redirect(303, "/")
	
})

// Se ejecuta cuando se manda DELETE a /users/delete
router.delete('/delete/:id', function(req, res) {
    db.users.remove({_id: ObjectId(req.params.id)}, function(err, result) {
	if(err) {
		console.log(err);
	}
	res.redirect(303, '/');
    });
});

// Enrutamiento
router.get("/", function(req, res) {  // peticion y respuesta como parametros

	if(req.session.email) {
		// para rellenar la plantilla
		db.users.find(function(err, docs) {
		if(err) {
			console.log(err);
		} else {
			console.log(docs); // lo que mongodb nos devuelva
			// para rellenar la plantilla
			res.render('index2', {
				title: 'clientes',
				email: req.session.email,
				users: docs // cambiamos users por docs
			});
			usuarios = docs}
		});

    }
    else {
        res.write('<h1>Please login first.</h1>');
        res.end('<a href='+'/email-password.html?logout'+'>Login</a>');
		console.log(req.session)
  
}
});




module.exports = router;
