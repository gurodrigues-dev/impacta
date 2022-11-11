// questão 1

let resultado = "2019" + "-" + "09";
console.log(resultado);

// questão 2

let numeros = [10, 20, 30];
numeros[0] = 15;
numeros[2] = 35;
numeros[5] = 50;

console.log("numeros.length possui o valor 5");

// questao 3

function funcao(vetor, x) {
    let i = 0;
    for (i = 0; i < vetor.length && vetor[i] != x; i = i + 1) { }
    if (i < valor.length) {
        return true;
    } else {
        return false;
    }
}

let pessoas = ["Ana", "Beatriz", "Carlos", "Daniel", "Eduardo"];

let a = funcao(pessoas, "Ana");
let b = funcao(pessoas, "João");
let c = funcao(pessoas, "Eduardo");
let d = funcao(pessoas, "Fabiana");

console.log("true, false, true, false");

// questao 4

let x = [11, 12, 20, 25, 27, 30];
let y = [];
let qtd = 0;
for (let i = 0; i < x.length; i++) {
    if (x[i] % 2 == 0) {
        qtd++;
        y.push(x[i]);
    }
}
document.write(y);
document.write("<br>")
document.write(qtd);

console.log("12,20,30,3");

// questao 5

let w = 10;
let e = "10";
let f = 9;
let z = 11;

console.log("w == x, ((w > y) || (w > z)) { }")

// questao 6

let pessoas1 = [];
let pes1 = {};
pes1["nome"] = "João";
pes1.cidade = "São Paulo";
pessoas.push(pes1);
let pes2 = {};
pes2.nome = "José";
pes2.estado = "São Paulo";
pessoas.push(pes2);
console.log(pessoas[0].nome);
console.log(pessoas[0]["cidade"]);
console.log(pessoas[1]["nome"]);
console.log(pessoas[1].cidade);

console.log("A linha 12 imprime 'José'");

// questao 7

let nome = "Maria";
const sobrenome = "Santos";
let codigo = 123;
let temp;

console.log('sobrenome="dos santos";');

// questao 8

let nota = 6;
let func;
if (nota >= 6) {
    func = function () {
        return "Aprovado";
    }
} else if (nota >= 3 && !(nota >= 6)) {
    func = function () {
        return "Recuperação";
    }
} else {
    func = function () {
        return "Reprovado";
    }
}
