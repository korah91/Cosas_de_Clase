const almacen = [
    {tipo: "lavadora", valor: 5000},
    {tipo: "lavadora", valor: 650},
    {tipo: "vaso", valor: 10},
    {tipo: "armario", valor: 1200},
    {tipo: "lavadora", valor: 77}
]
const lavadoras = almacen.filter(producto => producto.tipo === "lavadora");

const totalValorLavadoras = lavadoras.reduce((acc, lavadora) => acc + lavadora.valor, 0);

console.log(lavadoras)
//let totalValorLavadoras = tu código aquí;
console.log (totalValorLavadoras); // se espera 5727
