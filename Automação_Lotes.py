import fitz  # Biblioteca para ler e editar PDFs
import pytesseract  # Biblioteca para reconhecer texto em imagens, permite transformar imagens em texto (OCR)
import cv2  # OpenCV para processar imagens (editar imagens e cobrir textos, adicionar o retângulo preto)
import numpy as np  # Biblioteca para trabalhar com números e matrizes (útil para converter imagens)
import pandas as pd  # Biblioteca para ler arquivos Excel
import os  # Para interagir com arquivos e pastas no computador
from PIL import Image  # Biblioteca para manipular imagens

# O Tesseract é o programa que converte imagens em texto. Aqui, o código está dizendo onde o Tesseract está instalado no computador.
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\10680\Downloads\tesseract-ocr-w64-setup-5.5.0.20241111.exe"

# 🔹 Caminhos base
# Caminho do Excel com os fornecedores e lotes
excel_path = r"C:\Users\10680\EFACEC Power Solutions, SGPS, SA\Margarida Rosa Pimenta - Efacec Mobility 1ºPP\1. IANOS\3º EC Report M31-M39_M49-M51\Lotes.xlsx"

# Pasta onde estão os PDFs originais
input_folder = r"C:\Users\10680\EFACEC Power Solutions, SGPS, SA\Margarida Rosa Pimenta - Efacec Mobility 1ºPP\1. IANOS\3º EC Report M31-M39_M49-M51\3. Lotes"

# Pasta onde os PDFs editados serão salvos
output_base_folder = r"C:\Users\10680\EFACEC Power Solutions, SGPS, SA\Margarida Rosa Pimenta - Efacec Mobility 1ºPP\1. IANOS\3º EC Report M31-M39_M49-M51\2. Faturas"

#Carregar a tabela do Excel
df = pd.read_excel(excel_path, sheet_name="Lotes", usecols="B:F")

# Renomear colunas para fácil acesso
df.columns = ["UN", "Documento_Baan", "Pasta", "Parceiro", "Lote"]

#Criar um dicionário {Nome PDF: (Parceiro, Lote, Pasta, UN)}
lotes_dict = {
    str(row["Documento_Baan"]): (str(row["Parceiro"]), str(row["Lote"]), row["Pasta"], str(row["UN"]))
    for _, row in df.iterrows()
}

#Função para processar e redigir os PDFs
def redigir_pdf(pdf_path, parceiro_autorizado, output_path):
    doc = fitz.open(pdf_path)

    for page_num in range(len(doc)):  
        page = doc[page_num]
        pix = page.get_pixmap()
        
        # Convertendo a página para imagem
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img_cv = np.array(img)

        # OCR para extrair texto:  usa OCR para transformar a imagem da página em texto digital.
        extracted_text = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)

        for i, word in enumerate(extracted_text["text"]):
            # Detectar padrões na coluna "Ordens" e "Beneficiários"
            if word.startswith("BES") or (word.startswith("P") and word[1:].isdigit()):
                parceiro_numero = word.strip()

                # 🔹 Se o parceiro **NÃO** for o autorizado, ocultamos
                if parceiro_numero != parceiro_autorizado:
                    (x, y, w, h) = (extracted_text["left"][i], extracted_text["top"][i], 
                                    extracted_text["width"][i], extracted_text["height"][i])
                    cv2.rectangle(img_cv, (x, y), (x + w, y + h), (0, 0, 0), -1)  # Caixa preta

        # Converter de volta para PDF
        img_pil = Image.fromarray(img_cv)
        img_pil.save(f"temp_page_{page_num}.png")

        img_rect = fitz.open(f"temp_page_{page_num}.png")
        page.insert_image(page.rect, filename=f"temp_page_{page_num}.png")

    doc.save(output_path)
    doc.close()

# 🔹 Processar todos os PDFs na pasta "3. Lotes"
for pdf_file in os.listdir(input_folder):
    pdf_name, ext = os.path.splitext(pdf_file)
    if ext.lower() == ".pdf" and pdf_name in lotes_dict:
        parceiro, lote, pasta_destino = lotes_dict[pdf_name]
        
        input_pdf_path = os.path.join(input_folder, pdf_file)
         # Criar caminho correto dentro da UN
        un_folder = os.path.join(output_base_folder, un)  # Caminho para a UN
        output_folder = os.path.join(un_folder, pasta_destino)  # Caminho final

        # Criar pasta da UN e a pasta final se não existirem
        os.makedirs(output_folder, exist_ok=True)

        # Nome final do PDF
        output_pdf_path = os.path.join(output_folder, f"{pdf_name}_{lote}.pdf")

        print(f"🔹 Processando: {pdf_file} | Parceiro: {parceiro} | Lote: {lote} | UN: {un}")
        
        redigir_pdf(input_pdf_path, parceiro, output_pdf_path)

print("✅ Processamento concluído!")