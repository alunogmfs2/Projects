"use strict"

let um = " "
let dois = " "
let tres = " "
let quatro = " "
let cinco = " "
let seis = " "
let sete = " "
let oito = " "
let nove = " "

const desenharTabuleiro = function () {
    console.log(`  ${um}  |  ${dois}  |  ${tres}  `)
    console.log(`-----------------`)
    console.log(`  ${quatro}  |  ${cinco}  |  ${seis}  `)
    console.log(`-----------------`)
    console.log(`  ${sete}  |  ${oito}  |  ${nove}  `)
}

const perguntarPosicao = function () {
    while (true) {
        let pos = prompt("Digite a Posicao [0 - 9]: ")
        if(pos > 9 || pos < 0){
            console.log("Posicao invalida!")
        } else {
            break
        }
    }
}

const programa = function () {
    desenharTabuleiro()
    perguntarPosicao()
}

programa()