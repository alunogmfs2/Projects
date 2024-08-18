"use strict"

let tabuleiro = []

let colunas = 16
let linhas = 8
let espaco = false


for (let j = 0; j < linhas; j++) {
    let linha = []
    for (let i = 0; i < colunas; i++) {
        if (espaco === true) {
            linha.push("  ")
            espaco = false
        } else {
            linha.push("#")
            espaco = true
        }
        console.log(espaco)
    }
    tabuleiro.push(linha)
}

for (let i = 0; i < tabuleiro.length; i++) {
    let l = ""
    for (let j = 0; j < colunas; j++) {
        l += tabuleiro[i][j]
    }
    console.log(l)
}

