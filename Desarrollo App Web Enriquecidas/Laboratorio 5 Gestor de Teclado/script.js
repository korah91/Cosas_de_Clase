document.addEventListener('keydown', (event) => {
    switch (event.key) {
        case "ArrowDown":
            console.log("ArrowDown");
            event.preventDefault();
            break;
        case "ArrowUp":
            console.log("ArrowUp");
            event.preventDefault();
            break;
        case "ArrowLeft":
            console.log("ArrowLeft");
            event.preventDefault();
            break;
        case "ArrowRight":
            console.log("ArrowRight");
            event.preventDefault();
            break;
 
    }
});     
