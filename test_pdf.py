# TEST PDF EXTRACTION

from pdf_loader import load_pdf

text = load_pdf("sample.pdf")

print(text[:1000])