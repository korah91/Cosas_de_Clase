var contador = {
    cont: 0,
    sig: function(){
    	this.cont++;
      return this.cont-1;
    }
}
console.log(contador.sig()) // → 0
console.log(contador.sig()) // → 1
console.log(contador.sig()) // → 2