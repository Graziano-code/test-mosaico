import sys

with open('raccolta-dae.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace first link
content = content.replace(
    '<a href="https://maps.google.com/" target="_blank" rel="noopener noreferrer" aria-label="Apri la posizione dell\'attività partner 1', 
    '<a href="https://maps.app.goo.gl/qfkLWxQBWZwdPKxP7" target="_blank" rel="noopener noreferrer" aria-label="Apri la posizione dell\'attività partner 1'
)

# Replace second link
content = content.replace(
    '<a href="https://maps.google.com/" target="_blank" rel="noopener noreferrer" aria-label="Apri la posizione dell\'attività partner 2', 
    '<a href="https://maps.app.goo.gl/Pdt167CvyR7FG9CN6" target="_blank" rel="noopener noreferrer" aria-label="Apri la posizione dell\'attività partner 2'
)

with open('raccolta-dae.html', 'w', encoding='utf-8') as f:
    f.write(content)
