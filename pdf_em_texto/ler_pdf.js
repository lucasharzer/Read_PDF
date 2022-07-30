const fs = require("fs");
const pdf_parse = require("pdf-parse");

require("dotenv/config");


const arquivo = process.env.PATH_DOCUMENT;
const abrir_arquivo = fs.readFileSync(arquivo);

// Abrir o documento pdf
console.log("\nAbrindo documento .pdf ...")

pdf_parse(abrir_arquivo).then(function(data) {

    function extrair_texto() {
        const texto = data.text
        console.log(texto)
    }

    // Número de páginas:
    const numero_paginas = data.numpages
    console.log(`\n● Número de páginas: ${numero_paginas}`)

    // Informações:
    const informacoes = data.info
    
    for (const item in informacoes){
        console.log(`● ${item}: ${informacoes[item]}`)
    }

    // Versão:
    const versao = data.version
    console.log(`● Versão: ${versao}`)

    console.log("\nExtraindo texto ...\n")
    
    // Extrair texto
    setTimeout(extrair_texto, 11000)
});
