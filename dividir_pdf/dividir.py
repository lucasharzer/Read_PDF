import pikepdf


with pikepdf.open("C:\\Users\\Lucas\\Documents\\GitHub\\Dividir_pdf\\doc.PDF") as pdf:
    num = len(pdf.pages)
    # página desejada: 312 (-1 pois começa com a página 0) 

    for n, page in enumerate(pdf.pages):
        if n == 311:
            np = pdf.new()
            np.pages.append(page)
            np.save("docm.PDF")

print("Arquivo dividido.")
