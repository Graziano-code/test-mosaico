import sys

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    header = []
    footer = []
    
    # Extract header up to the start of <main>
    in_main = False
    in_footer = False
    for line in lines:
        if '<main id="main-content">' in line:
            header.append(line)
            in_main = True
        elif '</main>' in line:
            in_main = False
            in_footer = True
            footer.append(line)
        elif not in_main and not in_footer:
            header.append(line)
        elif in_footer:
            footer.append(line)
            
    # Fix the active title in <head>
    header = [line.replace('<title>A Piccoli Passi APS - Associazione Genitori Polo d\'Infanzia Madre Teresa di Calcutta</title>', '<title>Raccolta Fondi DAE - A Piccoli Passi APS</title>') for line in header]

    dae_content = """
        <!-- HERO SECTION DAE -->
        <section class="hero-section" id="raccolta-dae" style="padding: 2.5rem 1rem 3rem; background: linear-gradient(180deg, rgba(244, 248, 241, 0.85) 0%, rgba(253, 251, 247, 1) 100%);">
            <div class="hero-container" style="max-width: 800px; margin: 0 auto; text-align: center;">
                <h1 class="hero-title" style="margin-bottom: 1.5rem;">
                    <span class="title-prefix" style="color: var(--c-forest); font-size: 1.5rem;">Un DAE per la nostra comunità</span>
                    <span class="word-oggi" style="color: var(--c-orange); font-size: 2.2rem; font-weight: 800;">Dona per la Salute</span>
                </h1>
                
                <div style="border-radius: var(--radius-lg); overflow: hidden; margin-bottom: 2rem; box-shadow: var(--shadow-lg);">
                    <img src="images/Cuore Bizantino in Mosaico.png" alt="Mosaico Bizantino" style="width: 100%; height: auto; max-height: 40vh; object-fit: cover;">
                </div>

                <p class="hero-description" style="font-size: 1.2rem; margin-bottom: 2rem;">
                    Aiutaci a raggiungere il nostro obiettivo per l'acquisto di un defibrillatore.
                </p>

                <div class="progress-container" style="display: flex; flex-direction: column; align-items: center; margin-bottom: 3rem;">
                    <svg class="heart-svg" viewBox="0 0 32 29.6" style="width: 150px; height: 150px;">
                        <path d="M23.6,0c-3.4,0-6.3,2.7-7.6,5.6C14.7,2.7,11.8,0,8.4,0C3.8,0,0,3.8,0,8.4c0,9.4,9.5,11.9,16,21.2
                            c6.1-9.3,16-12.1,16-21.2C32,3.8,28.2,0,23.6,0z" fill="#e0e7dc"/>
                        <clipPath id="fill-clip">
                            <rect id="clip-rect" x="0" y="29.6" width="32" height="0" />
                        </clipPath>
                        <path d="M23.6,0c-3.4,0-6.3,2.7-7.6,5.6C14.7,2.7,11.8,0,8.4,0C3.8,0,0,3.8,0,8.4c0,9.4,9.5,11.9,16,21.2
                            c6.1-9.3,16-12.1,16-21.2C32,3.8,28.2,0,23.6,0z" fill="var(--c-orange)" clip-path="url(#fill-clip)"/>
                    </svg>
                    <div class="stats" style="font-size: 1.5rem; font-weight: 700; color: var(--c-forest); margin-top: 1rem;">
                        <span id="current-amount">0</span>€ / <span id="total-amount">1500</span>€
                    </div>
                </div>

                <button class="btn btn-primary" id="generate-btn" style="font-size: 1.2rem; padding: 1rem 2rem;">
                    Ritira il tuo pezzetto digitale!
                </button>
                
                <canvas id="canvas" width="1080" height="1080" style="display:none;"></canvas>
            </div>
        </section>

        <script>
            // Simulate fetch data
            const currentGoal = 850;
            const totalGoal = 1500;
            
            document.getElementById('current-amount').textContent = currentGoal;
            document.getElementById('total-amount').textContent = totalGoal;

            // Calculate fill percentage
            const percentage = Math.min(currentGoal / totalGoal, 1);
            
            // Update SVG clip-path
            const clipRect = document.getElementById('clip-rect');
            const svgHeight = 29.6;
            const fillHeight = svgHeight * percentage;
            const fillY = svgHeight - fillHeight;
            
            clipRect.setAttribute('y', fillY);
            clipRect.setAttribute('height', fillHeight);

            // Canvas Generation
            document.getElementById('generate-btn').addEventListener('click', () => {
                const canvas = document.getElementById('canvas');
                const ctx = canvas.getContext('2d');
                const img = new Image();
                
                // Set crossorigin to anonymous if you were requesting it from another server, but for local file:// it doesn't help.
                // img.crossOrigin = 'Anonymous';
                
                // Handle loading state
                const btn = document.getElementById('generate-btn');
                const originalText = btn.textContent;
                btn.textContent = 'Generazione in corso...';
                btn.disabled = true;

                img.onload = () => {
                    try {
                        // Draw background
                        ctx.fillStyle = '#333';
                        ctx.fillRect(0, 0, canvas.width, canvas.height);
                        
                        // Draw image covering the canvas
                        const scale = Math.max(canvas.width / img.width, canvas.height / img.height);
                        const x = (canvas.width / 2) - (img.width / 2) * scale;
                        const y = (canvas.height / 2) - (img.height / 2) * scale;
                        ctx.drawImage(img, x, y, img.width * scale, img.height * scale);

                        // Draw dark semi-transparent overlay
                        ctx.fillStyle = 'rgba(0, 0, 0, 0.5)';
                        ctx.fillRect(0, 0, canvas.width, canvas.height);

                        // Draw text
                        ctx.fillStyle = '#ffffff';
                        ctx.textAlign = 'center';
                        ctx.textBaseline = 'middle';
                        
                        // Title
                        ctx.font = 'bold 60px "Titillium Web", sans-serif';
                        ctx.fillText('HO DONATO PER IL DAE!', canvas.width / 2, canvas.height / 2 - 40);
                        
                        // Subtitle
                        ctx.font = '40px "Titillium Web", sans-serif';
                        ctx.fillText('1€ in cultura, 1€ in salute!', canvas.width / 2, canvas.height / 2 + 40);

                        // Download the generated image
                        const dataURL = canvas.toDataURL('image/png');
                        const link = document.createElement('a');
                        link.download = 'pezzetto-digitale-dae.png';
                        link.href = dataURL;
                        link.click();

                        // Reset button state
                        btn.textContent = originalText;
                        btn.disabled = false;
                    } catch (e) {
                        console.error('Errore canvas CORS:', e);
                        alert('Impossibile generare la tessera in anteprima locale, ma funzionerà online!');
                        btn.textContent = originalText;
                        btn.disabled = false;
                    }
                };

                img.onerror = () => {
                    alert('Errore nel caricamento dell\\'immagine di sfondo.');
                    btn.textContent = originalText;
                    btn.disabled = false;
                };

                // Load the image
                img.src = 'images/Cuore Bizantino in Mosaico.png';
            });
        </script>
"""

    with open('raccolta-dae.html', 'w', encoding='utf-8') as f:
        f.writelines(header)
        f.write(dae_content)
        f.writelines(footer)

if __name__ == '__main__':
    main()
