const express = require('express')
const app = express()
const http = require('http')


http.createServer(app).listen(80, () => { // fijaos que escuchamos en el puerto 80
    console.log('Listening...')
})


// permitimos crear en public carpetas que empiecen por ‘.’ con la opcion dotfiles
app.use(express.static(__dirname + '/public', { dotfiles: 'allow' } ))
