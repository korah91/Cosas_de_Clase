'use strict'; // detectara errores de programacion

var cacheVersion = 1; // variables que vamos a necesitar
var currentCache = {
    offline: 'offline-cache' + cacheVersion
};
const paginaOffline = 'offline-page.html'; // pagina que queremos cachear
const jsOffline = 'juego.js'

this.addEventListener('install', event => { // el evento “install” lo lanza el SW
    event.waitUntil( // bloqueamos la la instalacion hasta terminar de cachear elementos, si falla la instalacion fallara tambien
        caches.open(currentCache.offline).then(function(cache) {
            return cache.addAll([
                paginaOffline,
                jsOffline
            ]);
        })
    );
});


this.addEventListener('fetch', event => {
    // request.mode = navigate no esta soportado por todos los navegadores, incluimos una segunda opcion tras el ||
    if (event.request.mode === 'navigate' || (event.request.method === 'GET' && event.request.headers.get('accept').includes('text/html'))) {
            event.respondWith( // respuesta que daremos
                fetch(createCacheBustedRequest(event.request.url)).catch(error => {
                    // Return the offline page
                    return caches.match(paginaOffline);
                })
   
        );
    }
    else{ // si no es una peticion de una pagina HTML
        // si esta en cache (response) la devolvemos, si no usamos fetch (vamos a pedirlo online)
        event.respondWith(caches.match(event.request).then(function (response) { 
            return response || fetch(event.request);
        }));
    }
});



function createCacheBustedRequest(url){ 
    let request= new Request(url, {cache:'reload'});

    if ('cache' in request){ // si el navegador fuese moderno, con esto seria suficiente
        return request;
    }

    // para navegadores no-modernos, añadimos un parametro cachebust con la fecha actual como valor
    let bustedURL= new URL(url, self.location.href);
    bustedURL.search += (bustedURL.search ? '&' : '') + 'cachebust=' + Date.now();
    return request;
}


