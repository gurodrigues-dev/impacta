/**

 * Função que recebe uma lista e retorna o maior elemento.

 Desenvolva usando o for
   @param {Array} lista 
 * @return {Number} o menor valor.
 */

function acharMaior(lista) {
    var maior = 0;
    for (var i = 0; i < lista.length; i++) {
        if (lista[i] > maior) {
            maior = lista[i];
        }
    }
    if (lista.length > 0) {
        return maior
    }
    else {
        return undefined
    }
}

/**
 * Função que formata uma lista de compras.
 * 
 * Considere, por exemplo a lista ["fandangos","morangos","laranjas","ovos"]
 * A sua versão formatada fica: "fandangos, morangos, laranjas e ovos"
 * 
 * Ou seja, separamos por virgulas, mas o ultimo tem um "e" antes
 * 
 * Mais exemplos
 * a lista ["morangos","laranjas"] fica "morangos e laranjas"
 * a lista de um único elemento ["laranjas"] fica "laranjas"
 * 
 * Lembre-se que para juntar duas strings é só usar o +
 * >>> "ba" + "nana" resulta "banana"


 * @param {Array} lista 
 * @return {String} a lista formatada
 */

function lista_de_compras(lista) {
    let i = 0;
    let string = "";
    while (i < lista.length) {
        const ultimo_elemento = lista.length - 1
        if (i > 0 && i != ultimo_elemento) {
            string = string + ", "
        }
        if (i == ultimo_elemento && i != 0) {
            string = string + " e "
        }
        string = string + lista[i];
        i = i + 1
    }
    return string

}


/**

 * Função que recebe uma lista e retorna o a maior distância entre dois elementos.

 Por exemplo, na lista [10,13,8,17,9], a maior distância é entre 17 e 8, resulta 9

 Desenvolva usando o for
   @param {Array} lista 
 * @return {Number} a maior distância.
 */

function acharMaiorDistancia(lista) {
    if (lista.length > 0) {
        var arr = lista
        var min = Math.min(...arr);
        var max = Math.max(...arr);

        var sub = max - min;
        return sub
    }
    else {
        return undefined;
    }


}

/**

 * Função que recebe uma lista e retorna a lista, com os elementos na ordem inversa.

 Por exemplo, na lista [10,13,8,17,9], o inverso resulta [9, 17, 8, 13, 10]

 Desenvolva usando o for
   @param {Array} lista 
 * @return {Array} a lista invertida
 */

function inverter(lista) {
    var array = lista
    var length = lista.length;
    var left = null;
    var right = null;
    for (left = 0, right = length - 1; left < right; left += 1, right -= 1) {
        var temporary = lista[left];
        lista[left] = lista[right];
        lista[right] = temporary;
    }
    return lista
}

// A próxima função tem a ver com baralho.

// A idéia é representar cada carta como uma string de 2 letras:
//     as cartas sao 'A' (ás) 2,3,4,5,...,10,'J','Q' e 'K'
//     os naipes sao 'o' (ouros), 'c' (copas), 'e' (espadas) e 'p' (paus)

// O J de ouros, por exemplo, é representado pela string 'Jo'. O ás de copas,
// pela string 'Ac'

// #faça uma função que cria um baralho completo, com todas as 52 cartas
// #ela nao recebe nada e retorna uma lista.
// #os naipes sao 'o' (ouros), 'c' (copas), 'e' (espadas) e 'p' (paus)
// #as cartas sao 'A' (ás) 2,3,4,5,...,10,'J','Q' e 'K'
// #O J de ouros, por exemplo, é representado pela string 'Jo'. 
// #Assim 'Jo' é um dos elementos que deve aparecer na lista

// Dica: para juntar duas strings, faça let nova='a'+'b'
// Dica: para transformar uma variável n de número em string, faça let nova = n.toString()

/**
 * Função que cria baralho

 Desenvolva usando o for
 * @return {Array} a lista com os as cartas
 */

function cria_baralho() {
    let novoBaralho = [];
    let numerosCartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'];
    let naipesCartas = ['o', 'c', 'e', 'p']

    for (let contador1 = 0; contador1 < naipesCartas.length; contador1++) {
        for (let contador2 = 0; contador2 < numerosCartas.length; contador2++) {
            novoBaralho.push
                (
                    numerosCartas[contador2] + naipesCartas[contador1]
                );
        }
    }

    return novoBaralho;
}

/**
 * Função que desamassa uma lista.
 * 
 * Considere a lista l=[1,[2,3],4] (uma lista com 3 elementos, sendo que l[1] é uma lista)
 * Por exemplo, ao receber a lista l, a função deve retornar [1,2,3,4]
 * 
 * Para verificar se uma variável contém uma lista: Array.isArray.
 * Se Array.isArray(a) for true, a é uma lista, se for false, não é.
 * (comentário "inutil": em js, falamos em Arrays, ou vetores, em vez de listas)

 * @param {Array} lista 
 * @return {Array} a lista "desamassada"
 */

function desamassa_lista(lista) {
    let Newlist = []

    for (let i = 0; i < lista.length; i++) {
        // Se for numero
        if (!Array.isArray(lista[i])) {
            Newlist.push(lista[i]);
        }
        else // Se for Array
        {
            let outraLista = desamassa_lista(lista[i]);

            for (let x = 0; x < outraLista.length; x++) {
                Newlist.push(outraLista[x]);
            }
        }
    }

    return Newlist
}

