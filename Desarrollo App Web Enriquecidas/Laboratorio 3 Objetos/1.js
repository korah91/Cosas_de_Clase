class Punto{
	constructor(x,y){
  	this.x = x;
    this.y = y;
  }
  
  suma(punto){
  	return new Punto(punto.x + this.x, punto.y + this.y);
  	
  }
  
}
console.log(new Punto(1, 2).suma(new Punto(2, 1)))

