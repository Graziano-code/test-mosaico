import sys

with open('raccolta-dae.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_text = "Inquadra il QR Code, dona in totale autonomia con Satispay, colora il tuo pezzetto sul foglio."
new_text = "Inquadra il QR Code, dona in totale autonomia con Satispay, colora il tuo tassello nella locandina."

content = content.replace(old_text, new_text)

with open('raccolta-dae.html', 'w', encoding='utf-8') as f:
    f.write(content)

