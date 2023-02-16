

class ArrayOrdenado{
	constructor(comparador){
  	this.comparador = comparador;
    this.contenido = [];
  }
  findPos(elt){
    return this.contenido.findIndex(x => x === elt);
  }
  insert(elt){
  	this.contenido.splice(this.findPos(elt), 0, elt)
  }
}


var ordenado = new ArrayOrdenado((a, b) => a - b );
ordenado.insert(5);
ordenado.insert(1);
ordenado.insert(2);
ordenado.insert(4);
ordenado.insert(3);
console.log("array:", ordenado.contenido);
// array: [1, 2, 3, 4, 5]