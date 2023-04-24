var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');

  // Modificaremos email-password.html para tener en cuenta este parámetro y hacer el sign out. 
  // Es decir, si la URL incluye este parámetro, se hace un sign out automáticamente.
});

module.exports = router;
