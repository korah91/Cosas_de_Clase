var express = require('express');
var router = express.Router();
var admin = require("firebase-admin");

admin.initializeApp({
  credential: admin.credential.applicationDefault(),
});

/* GET home page. */
router.get('/', function(req, res, next) {

  res.render('index', { title : 'title'});
});

router.post('/getToken', (req, res) => {
  const idToken = req.body.idToken; // capturar parámetro

  // idToken comes from the client app
  // verificamos el idToken para ver si es válido
  admin.auth().verifyIdToken(idToken)
      .then(function (decodedToken) {
// si es válido, lo decodificamos
        let uid = decodedToken.uid;

// y obtenemos los datos asociados a ese usuario
        admin.auth().getUser(uid)
            .then(function(userRecord) {
              // See the UserRecord reference doc for the contents of userRecord.
              console.log('Successfully fetched user data:', userRecord.toJSON());
              req.session.email = userRecord.email;
              req.session.emailVerified = userRecord.emailVerified;
              res.send('{"status": "done"}');
            })
            .catch(function(error) {
              console.log('Error fetching user data:', error);
              res.send('{"status": "error"}');
            });

      }).catch(function (error) {
    // Handle error
    res.render('error', {error: error, message: "You must be signed-up"});
  });
});

// Cuando le mando a login CREO la sesion
router.post('/login',(req,res) => {
  console.log("He recibido un POST a /login")
  req.session.email = req.body.email;
  res.end('done');
});



module.exports = router;
