var express = require("express")
var router = express.Router();
var session = require('express-session')

const { check, validationResult } = require('express-validator');
var path = require("path"); // viene por defecto en Node

const mongojs = require('mongojs')
var ObjectId = mongojs.ObjectId;
const db = mongojs('clientespp', ['users'])

router.use(session({ secret: 'keyboard cat', cookie: { maxAge: 10000 }, resave: true, saveUninitialized:true}))

router.use(function (req, res, next) {
	// Pongo error como variable global
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
			res.render('users', {
				title: 'clientes',
				email: req.session.email,
				users: docs // cambiamos users por docs
			});
			usuarios = docs}
		});

    }
    else {
        res.write('<h1>Please login first.</h1>');
        res.end('<a href='+'/email-password.html'+'>Login</a>');
		console.log(req.session)
    




}
});

router.get('/logout',(req,res) => {
    req.session.destroy((err) => {
        if(err) {
            return console.log(err);
        }
        res.redirect('/email-password.html?logout');
    });
});

// Cuando le mando a login CREO la sesion
router.post('/login',(req,res) => {
	console.log("He recibido un POST a /login")
	console.log("email: ", req.body.email)
	req.session.email = req.body.email;
	res.end();
  });

module.exports = router;
