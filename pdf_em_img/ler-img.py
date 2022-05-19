from PIL import Image
import pytesseract
import dotenv
import os


dotenv.load_dotenv(dotenv.find_dotenv())
path_tesseract = os.getenv("PATH_TESSERACT")
path_pasta = os.getenv("PASTA_PDF_IMAGEM")

pytesseract.pytesseract.tesseract_cmd = path_tesseract

texto1 = pytesseract.image_to_string(Image.open("{path_pasta}\\img1.png"))
linhas = texto1.split("\n")

print("-Primeiro documento:\n")
for linha in linhas:
    if "Cadastro da Req" in str(linha).strip():
        data_cadastro = str(linha[linha.find(":")+1:]).strip()
        print(data_cadastro)
    elif "Originaria n°" in str(linha).strip() and "o n°" in str(linha).strip():
        l = linha.split(" n° ")
        acao_originaria = str(l[1][:23]).strip()
        print(acao_originaria)

        acao_execucao = str(l[2][:25]).strip()
        print(acao_execucao)
    elif "Requerente / Credor:" in str(linha).strip():
        requerente_credor = str(linha[linha.find(":")+1:]).strip()
        print(requerente_credor)
    elif "Advogado/OAB:" in str(linha).strip():
        advogado_oab = str(linha[linha.find(":")+1:]).strip()
        print(advogado_oab)
    elif "Requerido / Devedor:" in str(linha).strip():
        requerido_devedor = str(linha[linha.find(":")+1:]).strip()
        print(requerido_devedor)
    elif "Natureza do Crédito:" in str(linha).strip():
        nc = str(linha[linha.find(":")+1:]).strip()
        nc2 = nc[nc.find(" ")+1:]
        natureza_credito = str(nc2[:nc2.find(" ")]).strip()
        print(natureza_credito)

texto3 = pytesseract.image_to_string(Image.open("{path_pasta}\\img2.png"))
linhas = texto3.split("\n")

pos = 0
pos_nr = 0
pos_nome = 0
pos_nome_honorario = 0
pos_vr = 0
print("\n-Segundo documento:\n")
for linha in linhas:
    pos += 1
    if len(linha) != 0:
        if "NOME COMPLETO" in str(linha).strip():
            if pos_nr == 0:
                pos_nome = pos+2
                pos_nr += 1
            else:
                pos_nome_honorario = pos+2
        if "VALOR TOTAL" in str(linha).strip():
            if pos_vr == 0:
                pos_vr += 1
                valor1 = str(linha[linha.find(":")+1:]).strip()
                print(valor1)
            else:
                v = str(linha[linha.find(":")+1:]).strip()
                valor2 = str(v[:v.find(" ")]).strip()
                print(valor2)
        if pos == pos_nome:
            l = linha.split("|")
            nome_completo = str(l[0]).strip()
            print(nome_completo)

            l1 = str(l[1]).strip()
            d = str(l1[l1.find(" ")+1:]).strip()
            documento = str(d[:d.find(" ")]).strip()
            print(documento)

            data_base = str(l1[-8:]).strip()
            print(data_base)
        if pos == pos_nome_honorario:
            l = linha.split("|")
            nome_honorario = str(l[0]).strip()
            print(nome_honorario)

            l1 = str(l[1]).strip()
            documento_honorario = str(l1[:l1.find(" ")]).strip()
            print(documento_honorario)

            data_base_honorario = str(l1[-8:]).strip()
            print(data_base_honorario)
