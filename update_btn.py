import sys

with open('raccolta-dae.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_html = """                    <h2 style="color: var(--c-forest); font-size: 1.5rem; margin-bottom: 1rem;">Le Attività Commerciali che ci sostengono</h2>
                    <ul style="margin-bottom: 2rem; padding-left: 1.5rem;">"""

new_html = """                    <h2 style="color: var(--c-forest); font-size: 1.5rem; margin-bottom: 1rem;">Le Attività Commerciali che ci sostengono</h2>
                    <a href="images/locandina-stampa.jpeg" download="Locandina_Mosaico_DAE.jpg" style="display: inline-block; margin-top: 10px; margin-bottom: 20px; padding: 10px 16px; font-size: 15px; font-weight: bold; color: #2e7d32; border: 2px solid #2e7d32; border-radius: 8px; text-decoration: none; text-align: center; background-color: transparent; transition: all 0.3s ease;">📥 Sei un'attività? Scarica la locandina e unisciti a noi!</a>
                    <ul style="margin-bottom: 2rem; padding-left: 1.5rem;">"""

content = content.replace(old_html, new_html)

with open('raccolta-dae.html', 'w', encoding='utf-8') as f:
    f.write(content)
