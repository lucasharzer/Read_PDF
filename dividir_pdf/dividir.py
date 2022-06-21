import pikepdf
import dotenv
import os


dotenv.load_dotenv(dotenv.find_dotenv())
local_arquivo = str(os.getenv("ARQUIVO_PARA_DIVIDIR")).strip()

with pikepdf.open(local_arquivo) as pdf:
    num = len(pdf.pages)
    # página desejada: 312 (-1 pois começa com a página 0) 

    for n, page in enumerate(pdf.pages):
        if n == 311:
            np = pdf.new()
            np.pages.append(page)
            np.save("docm.PDF")

print("Arquivo dividido.")
