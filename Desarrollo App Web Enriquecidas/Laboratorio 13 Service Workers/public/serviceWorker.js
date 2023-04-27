'use strict'; // detectara errores de programacion

var cacheVersion = 1; // variables que vamos a necesitar
var currentCache = {
    offline: 'offline-cache' + cacheVersion
};
const paginaOffline = 'index.html'; // pagina que queremos cachear
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
                // peticion al servidor, si hay conexion ira bien, si no (no hay conexion) devolvemos lo que tengamos cacheado
                fetch(event.request.url).catch(error => { 
                    return caches.match(offlineUrl); // devolvemos lo cacheado
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

