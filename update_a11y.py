import re

with open('raccolta-dae.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update image alt text
content = content.replace('alt="Cuore Bizantino in Mosaico"', 'alt="Opera d\'arte a mosaico in stile bizantino raffigurante un cuore rosso e dorato su sfondo blu"')

# 2. Accessibility SVG
svg_old = '<svg class="heart-svg" viewBox="0 0 32 29.6" style="width: 80px; height: 80px; margin-bottom: 0.5rem; display: inline-block;">'
svg_new = '<svg class="heart-svg" viewBox="0 0 32 29.6" style="width: 80px; height: 80px; margin-bottom: 0.5rem; display: inline-block;" role="img" aria-labelledby="svg-title">\n                            <title id="svg-title">Progresso raccolta fondi: 850 euro su 3000</title>'
content = content.replace(svg_old, svg_new)

# 3. Decorative elements (emojis)
content = content.replace('<strong>🎯 Traguardo 1 (1.500€): La Sicurezza prima di tutto.</strong>', '<strong><span aria-hidden="true">🎯</span> Traguardo 1 (1.500€): La Sicurezza prima di tutto.</strong>')
content = content.replace('<strong>🌟 Traguardo 2 (3.000€): L\'Eredità Artistica.</strong>', '<strong><span aria-hidden="true">🌟</span> Traguardo 2 (3.000€): L\'Eredità Artistica.</strong>')

content = content.replace('<span style="position: absolute; left: 0; top: 0;">🏫</span>', '<span style="position: absolute; left: 0; top: 0;" aria-hidden="true">🏫</span>')
content = content.replace('<span style="position: absolute; left: 0; top: 0;">⛪</span>', '<span style="position: absolute; left: 0; top: 0;" aria-hidden="true">⛪</span>')
content = content.replace('<span style="position: absolute; left: 0; top: 0;">🏪</span>', '<span style="position: absolute; left: 0; top: 0;" aria-hidden="true">🏪</span>')

# 4. Buttons and Google maps links
links_old = """                    <ul style="margin-bottom: 2rem; padding-left: 1.5rem;">
                        <li style="margin-bottom: 0.5rem;">Attività Partner 1</li>
                        <li>Attività Partner 2</li>
                    </ul>"""
                    
links_new = """                    <ul style="margin-bottom: 2rem; padding-left: 1.5rem;">
                        <li style="margin-bottom: 0.5rem;"><a href="https://maps.google.com/" target="_blank" rel="noopener noreferrer" aria-label="Apri la posizione dell'attività partner 1 su Google Maps in una nuova scheda" style="text-decoration: underline; color: var(--c-blue);">Attività Partner 1</a></li>
                        <li><a href="https://maps.google.com/" target="_blank" rel="noopener noreferrer" aria-label="Apri la posizione dell'attività partner 2 su Google Maps in una nuova scheda" style="text-decoration: underline; color: var(--c-blue);">Attività Partner 2</a></li>
                    </ul>"""
                    
content = content.replace(links_old, links_new)

with open('raccolta-dae.html', 'w', encoding='utf-8') as f:
    f.write(content)

