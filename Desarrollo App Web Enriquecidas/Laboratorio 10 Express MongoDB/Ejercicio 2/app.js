var express = require("express")
const { check, validationResult } = require('express-validator');
var path = require("path"); // viene por defecto en Node
const { exit } = require("process");

const multer  = require('multer')
const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, 'public/imgs')
    },
    filename: (req, file, cb) => {
        //console.log(file)
        cb(null, Date.now() + path.extname(file.originalname))
    },
    limits: '2MB'

});

const upload = multer({ storage: storage })



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
app.post('/upload/files', upload.array('fileselect',12),
	function(req, res){
		// Obtenemos el usuario del formulario
        var objetoJSON = {
            'exito': true,
            'nombre': req.body.nombre,
            'telefono': req.body.telefono,
            'email': req.body.email,
            'libros': req.body.libros,
            'cantidad': req.body.cantidad,
            'lista_imagenes': req.files
            
        }   
        //console.log("Se ha recibido en servidor")
        //console.log(req.files)
        //const file = req.file



        res.send(objetoJSON)

        /*
        res.render('index', {
            user: newUsuario
        })
        */
	}
);


app.get('/', function(req, res){
    res.render('index')
}
);





