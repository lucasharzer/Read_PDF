from pdf2image import convert_from_path
import dotenv
import os


dotenv.load_dotenv(dotenv.find_dotenv())
arquivo = os.getenv("ARQUIVO_PDF_IMAGEM")
path_poppler = os.getenv("PATH_POPPLER")
path_pasta = os.getenv("PASTA_PDF_IMAGEM")

paginas = convert_from_path(arquivo, 200, poppler_path=path_poppler)

cont = 0
for pagina in paginas:
    cont += 1
    pagina.save(f"{path_pasta}\\img{cont}.png", "PNG")

print(f"total de imagens geradas: {cont}")
