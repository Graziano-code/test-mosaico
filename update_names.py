import sys

with open('raccolta-dae.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_list = """                    <ul style="margin-bottom: 2rem; padding-left: 1.5rem;">
                        <li style="margin-bottom: 0.5rem;"><a href="https://maps.app.goo.gl/qfkLWxQBWZwdPKxP7" target="_blank" rel="noopener noreferrer" aria-label="Apri la posizione dell'attività partner 1 su Google Maps in una nuova scheda" style="text-decoration: underline; color: var(--c-blue);">Attività Partner 1</a></li>
                        <li><a href="https://maps.app.goo.gl/Pdt167CvyR7FG9CN6" target="_blank" rel="noopener noreferrer" aria-label="Apri la posizione dell'attività partner 2 su Google Maps in una nuova scheda" style="text-decoration: underline; color: var(--c-blue);">Attività Partner 2</a></li>
                    </ul>"""

new_list = """                    <ul style="margin-bottom: 2rem; padding-left: 1.5rem;">
                        <li style="margin-bottom: 0.5rem;"><a href="https://maps.app.goo.gl/Pdt167CvyR7FG9CN6" target="_blank" rel="noopener noreferrer" aria-label="Apri la posizione di Ristorante Pizzeria La Piazzetta su Google Maps in una nuova scheda" style="text-decoration: underline; color: var(--c-blue);">Ristorante Pizzeria La Piazzetta</a></li>
                        <li><a href="https://maps.app.goo.gl/qfkLWxQBWZwdPKxP7" target="_blank" rel="noopener noreferrer" aria-label="Apri la posizione di Da Fabio Cafè su Google Maps in una nuova scheda" style="text-decoration: underline; color: var(--c-blue);">Da Fabio Cafè</a></li>
                    </ul>"""

content = content.replace(old_list, new_list)

with open('raccolta-dae.html', 'w', encoding='utf-8') as f:
    f.write(content)
