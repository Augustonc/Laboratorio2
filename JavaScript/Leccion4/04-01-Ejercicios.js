//Ejercicio: Si el padre puede asistir al juego de su hijo

let vacaciones = false, diaDescanso = false;
if(vacaciones || diaDescanso){
    console.log("El padre puede asistir al juego")
}
else{
    console.log("El padre no puede asistir al juego")
}

//Operador ternario
//Ejercicio: número par e impar
let resultado2 = 3 > 2 ?"Verdadero" : "Falso";
console.log(resultado2)
let numero = 9;
resultado2 = numero % 2 == 0 ? "Es un número par" : "Es un numero impar";
console.log(resultado2)
//Convertir String a number
let miNumero = "18"; //Esto es una cadena
console.log(typeof miNumero);
let edad = Number(miNumero); //Esto es una funcion
console.log(typeof edad);

//Funcion isNaN
if(isNaN(edad)){ //No es un numero = is Not a Number(devuelve un resultado booleano)
    console.log("Esta variable no contiene solo numeros")
}
else{
    if( edad >= 18){
        console.log("Puede votar");
    }
else{
        console.log("No puede votar");
    }
}


let resultado3 = edad >= 18 ? "Puede votar" : "No puedo votar";
console.log(resultado3);

