import pdfplumber
from time import sleep
import dotenv
import os


dotenv.load_dotenv(dotenv.find_dotenv())
arquivo = os.getenv("ARQUIVO_PDF_TEXTO ")

pdf = pdfplumber.open(arquivo)
numero_paginas = len(pdf.pages)

pagina = 0
while pagina < numero_paginas:
    print(f"\nPágina {pagina}:")
    texto = pdf.pages[pagina].extract_text()
    # print(texto)
    linhas = texto.split("\n")
    for linha in linhas:
        print(linha)
    pagina += 1
    sleep(2)

print("Fim das páginas.")
