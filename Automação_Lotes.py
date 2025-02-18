import fitz  # PyMuPDF para manipular PDFs
import pytesseract  # Tesseract OCR para extrair texto de imagens
import cv2  # OpenCV para processar imagens
import numpy as np  # Numpy para operações com arrays
import pandas as pd  # Pandas para ler Excel
import os  # Para manipular arquivos e pastas
from PIL import Image  # Pillow para converter imagens
import re  # Expressões regulares para extrair nomes de lotes
import shutil  # Para mover arquivos

# 📌 Configurar Tesseract OCR (ajuste conforme a instalação)
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\10680\OneDrive - EFACEC Power Solutions, SGPS, SA\Desktop\TESSERACT\tesseract.exe"

# 📂 Caminhos
excel_path = r"C:\Users\10680\EFACEC Power Solutions, SGPS, SA\Margarida Rosa Pimenta - Efacec Mobility 1ºPP\1. IANOS\3º EC Report M31-M39_M49-M51\Lotes.xlsx"
input_folder = r"C:\Users\10680\EFACEC Power Solutions, SGPS, SA\Margarida Rosa Pimenta - Efacec Mobility 1ºPP\1. IANOS\3º EC Report M31-M39_M49-M51\3. Lotes"
output_base_folder = r"C:\Users\10680\EFACEC Power Solutions, SGPS, SA\Margarida Rosa Pimenta - Efacec Mobility 1ºPP\1. IANOS\3º EC Report M31-M39_M49-M51\2. Faturas"


# 🔍 Carregar Excel com os lotes
df = pd.read_excel(excel_path, sheet_name="Lotes", usecols="B:G", header=1)
lotes_dict = {str(row["Documento Lote"]): os.path.join(output_base_folder, str(row["Pasta"])) for _, row in df.iterrows()}

# Criar pastas de saída se não existirem
for pasta in lotes_dict.values():
    os.makedirs(pasta, exist_ok=True)

# 📂 Processar cada PDF
pdf_files = [f for f in os.listdir(input_folder) if f.endswith(".pdf")]

for pdf in pdf_files:
    match = re.match(r"(L\d{4,5})", pdf)
    if match:
        lote = match.group(1)
        if lote in lotes_dict:
            destino = os.path.join(lotes_dict[lote], pdf)
            pdf_path = os.path.join(input_folder, pdf)

            # 🏷️ Abrir o PDF
            doc = fitz.open(pdf_path)
            images = []

            for page_num, page in enumerate(doc):
                # 📷 Converter página em imagem
                pix = page.get_pixmap()
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                img = np.array(img)

                # 📝 Extrair texto e posições usando Tesseract
                h, w, _ = img.shape
                data = pytesseract.image_to_data(img, lang="por", output_type=pytesseract.Output.DICT)

                # 🔳 Cobrir palavras detectadas
                for i in range(len(data["text"])):
                    if int(data["conf"][i]) > 50:  # Confiança mínima de 50%
                        x, y, w, h = data["left"][i], data["top"][i], data["width"][i], data["height"][i]
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), -1)

                images.append(img)

            # 📝 Criar novo PDF com as imagens editadas
            censored_pdf = fitz.open()
            for img in images:
                img_pil = Image.fromarray(img).convert("RGB")
                img_bytes = img_pil.tobytes("jpeg", "RGB")
                new_page = censored_pdf.new_page(width=img_pil.width, height=img_pil.height)
                new_page.insert_image(new_page.rect, stream=img_bytes)

            censored_pdf.save(destino)
            censored_pdf.close()
            doc.close()

            print(f"✅ PDF '{pdf}' censurado e movido para '{lotes_dict[lote]}'")
        else:
            print(f"⚠️ Documento Lote '{lote}' não encontrado no Excel! PDF '{pdf}' ignorado.")
    else:
        print(f"⚠️ Nome de arquivo '{pdf}' não segue o padrão esperado. Ignorado.")

print("✅ Processamento concluído!")