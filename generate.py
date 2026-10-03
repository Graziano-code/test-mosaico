import sys

def update_files():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    new_nav_item = '<li><a href="raccolta-dae.html" class="nav-dona" aria-label="Sostieni il Progetto DAE">Sostieni il Progetto DAE</a></li>\n                    <li><a href="#unisciti"'
    content = content.replace('<li><a href="#unisciti"', new_nav_item)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

    header = content.split('<main id="main-content">')[0] + '<main id="main-content">\n'
    footer = '\n    </main>' + content.split('</main>')[1]

    header = header.replace('<title>A Piccoli Passi APS - Associazione Genitori Polo d\'Infanzia Madre Teresa di Calcutta</title>', '<title>Raccolta Fondi DAE - A Piccoli Passi APS</title>')

    dae_content = """
        <!-- HERO SECTION DAE -->
        <section class="hero-section" id="raccolta-dae" style="padding: 2.5rem 1rem 3rem; background: linear-gradient(180deg, rgba(244, 248, 241, 0.85) 0%, rgba(253, 251, 247, 1) 100%);">
            <div class="hero-container" style="max-width: 800px; margin: 0 auto; text-align: center;">
                
                <div style="border-radius: var(--radius-lg); overflow: hidden; margin-bottom: 2rem; box-shadow: var(--shadow-lg);">
                    <img src="images/Cuore Bizantino in Mosaico.png" alt="Cuore Bizantino in Mosaico" style="width: 100%; height: auto; max-height: 40vh; object-fit: cover;">
                </div>

                <div class="progress-container" style="display: flex; flex-direction: column; align-items: center; margin-bottom: 2rem;">
                    <svg class="heart-svg" viewBox="0 0 32 29.6" style="width: 120px; height: 120px; margin-bottom: 1rem;">
                        <path d="M23.6,0c-3.4,0-6.3,2.7-7.6,5.6C14.7,2.7,11.8,0,8.4,0C3.8,0,0,3.8,0,8.4c0,9.4,9.5,11.9,16,21.2
                            c6.1-9.3,16-12.1,16-21.2C32,3.8,28.2,0,23.6,0z" fill="#e0e7dc"/>
                        <clipPath id="fill-clip">
                            <rect id="clip-rect" x="0" y="29.6" width="32" height="0" />
                        </clipPath>
                        <path d="M23.6,0c-3.4,0-6.3,2.7-7.6,5.6C14.7,2.7,11.8,0,8.4,0C3.8,0,0,3.8,0,8.4c0,9.4,9.5,11.9,16,21.2
                            c6.1-9.3,16-12.1,16-21.2C32,3.8,28.2,0,23.6,0z" fill="var(--c-orange)" clip-path="url(#fill-clip)"/>
                    </svg>
                    <div class="stats" style="font-size: 1.5rem; font-weight: 700; color: var(--c-forest);">
                        <span id="current-amount">0</span>€ / <span id="total-amount">3000</span>€
                    </div>
                </div>

                <h1 class="hero-title" style="margin-bottom: 1rem;">
                    <span class="title-prefix" style="color: var(--c-forest); font-size: 1.6rem; display: block;">Un Mosaico per il DAE:</span>
                    <span class="word-oggi" style="color: var(--c-orange); font-size: 2rem; font-weight: 800;">1€ in cultura, 1€ in salute!</span>
                </h1>
                
                <p class="hero-description" style="font-size: 1.2rem; margin-bottom: 3rem; font-weight: 600;">
                    Aiutaci a rendere il Polo d'Infanzia "Madre Teresa di Calcutta" cardioprotetto e a lasciare un segno artistico indelebile nella nostra comunità.
                </p>

                <div style="text-align: left; background: #fff; padding: 2rem; border-radius: var(--radius-md); box-shadow: var(--shadow-sm); margin-bottom: 2rem;">
                    <h2 style="color: var(--c-forest); font-size: 1.5rem; margin-bottom: 1rem;">I Nostri Due Traguardi</h2>
                    <p style="margin-bottom: 1.5rem;">
                        Il nostro progetto è un grande mosaico composto da 1500 tessere. Ogni 2€ raccolti, si colora una tessera. L'offerta è completamente libera: dona quello che puoi, ogni centesimo conta!
                    </p>
                    
                    <div style="margin-bottom: 1rem; padding: 1rem; background: var(--c-surface-soft); border-left: 4px solid var(--c-leaf); border-radius: 4px;">
                        <strong>🎯 Traguardo 1 (1.500€): La Sicurezza prima di tutto.</strong><br> Acquisteremo un Defibrillatore Semiautomatico (DAE) per la scuola e finanzieremo i corsi di abilitazione BLSD per le nostre maestre.
                    </div>
                    
                    <div style="margin-bottom: 2rem; padding: 1rem; background: var(--c-surface-soft); border-left: 4px solid var(--c-yellow); border-radius: 4px;">
                        <strong>🌟 Traguardo 2 (3.000€): L'Eredità Artistica.</strong><br> Se la generosità supererà le aspettative, commissioneremo a un vero artista ravennate la realizzazione fisica del Cuore in mosaico (1500 tessere) che verrà installato e donato permanentemente alla scuola!
                    </div>

                    <h2 style="color: var(--c-forest); font-size: 1.5rem; margin-bottom: 1rem;">Come partecipare (Il Mosaico Diffuso)</h2>
                    <p style="margin-bottom: 1.5rem;">
                        Abbiamo trasformato la raccolta fondi in un gioco diffuso che coinvolge tutto il territorio. Ecco come puoi partecipare e lasciare il tuo segno:
                    </p>

                    <ul style="list-style: none; padding-left: 0; margin-bottom: 2rem;">
                        <li style="margin-bottom: 1rem; padding-left: 1.5rem; position: relative;">
                            <span style="position: absolute; left: 0; top: 0;">🏫</span>
                            <strong>A Scuola (Il Tabellone Master):</strong> All'ingresso del Polo d'Infanzia troverai il grande tabellone principale. Qui è possibile donare in contanti o con Satispay. Man mano che le donazioni si sommano, i bambini coloreranno fisicamente le tessere corrispondenti! (Il tabellone viene aggiornato dal lunedì al venerdì: ogni tessera colorata rappresenta una soglia di 2€ raggiunta).
                        </li>
                        <li style="margin-bottom: 1rem; padding-left: 1.5rem; position: relative;">
                            <span style="position: absolute; left: 0; top: 0;">⛪</span>
                            <strong>In Chiesa:</strong> È disponibile un punto di raccolta tradizionale in contanti.
                        </li>
                        <li style="margin-bottom: 1rem; padding-left: 1.5rem; position: relative;">
                            <span style="position: absolute; left: 0; top: 0;">🏪</span>
                            <strong>Nelle Attività Aderenti (Solo Satispay):</strong> Cerca le nostre locandine A4 nelle attività commerciali del territorio che ci supportano. Inquadra il QR Code, dona in totale autonomia con Satispay, colora il tuo pezzetto sul foglio. Se vuoi sostenerci puoi fare una foto alla locandina e taggaci su Instagram e Facebook per spargere la voce.
                        </li>
                    </ul>

                    <h2 style="color: var(--c-forest); font-size: 1.5rem; margin-bottom: 1rem;">Le Attività Commerciali che ci sostengono</h2>
                    <ul style="margin-bottom: 2rem; padding-left: 1.5rem;">
                        <li style="margin-bottom: 0.5rem;">Attività Partner 1</li>
                        <li>Attività Partner 2</li>
                    </ul>
                </div>

                <div style="display: flex; flex-direction: column; gap: 1rem; align-items: center;">
                    <button class="btn btn-primary" id="generate-btn" style="width: 100%; max-width: 500px; padding: 1rem; font-size: 1.1rem; border-radius: var(--radius-md);">
                        Hai già donato? Ritira il tuo pezzetto digitale!
                    </button>
                    
                    <a href="#" class="btn btn-secondary" style="width: 100%; max-width: 500px; padding: 1rem; font-size: 1.1rem; border-radius: var(--radius-md); text-align: center;">
                        Hai donato con Satispay o Bonifico?<br>Richiedi la ricevuta per le detrazioni fiscali
                    </a>
                </div>
                
                <canvas id="canvas" width="1080" height="1080" style="display:none;"></canvas>
            </div>
        </section>

        <script>
            const currentGoal = 850;
            const totalGoal = 3000;
            
            document.getElementById('current-amount').textContent = currentGoal;
            document.getElementById('total-amount').textContent = totalGoal;

            const percentage = Math.min(currentGoal / totalGoal, 1);
            
            const clipRect = document.getElementById('clip-rect');
            const svgHeight = 29.6;
            const fillHeight = svgHeight * percentage;
            const fillY = svgHeight - fillHeight;
            
            clipRect.setAttribute('y', fillY);
            clipRect.setAttribute('height', fillHeight);

            document.getElementById('generate-btn').addEventListener('click', () => {
                const canvas = document.getElementById('canvas');
                const ctx = canvas.getContext('2d');
                const img = new Image();
                
                const btn = document.getElementById('generate-btn');
                const originalText = btn.textContent;
                btn.textContent = 'Generazione in corso...';
                btn.disabled = true;

                img.onload = () => {
                    try {
                        ctx.fillStyle = '#333';
                        ctx.fillRect(0, 0, canvas.width, canvas.height);
                        
                        const scale = Math.max(canvas.width / img.width, canvas.height / img.height);
                        const x = (canvas.width / 2) - (img.width / 2) * scale;
                        const y = (canvas.height / 2) - (img.height / 2) * scale;
                        ctx.drawImage(img, x, y, img.width * scale, img.height * scale);

                        ctx.fillStyle = 'rgba(0, 0, 0, 0.5)';
                        ctx.fillRect(0, 0, canvas.width, canvas.height);

                        ctx.fillStyle = '#ffffff';
                        ctx.textAlign = 'center';
                        ctx.textBaseline = 'middle';
                        
                        ctx.font = 'bold 60px "Titillium Web", sans-serif';
                        ctx.fillText('HO DONATO PER IL DAE!', canvas.width / 2, canvas.height / 2 - 40);
                        
                        ctx.font = '40px "Titillium Web", sans-serif';
                        ctx.fillText('1€ in cultura, 1€ in salute!', canvas.width / 2, canvas.height / 2 + 40);

                        const dataURL = canvas.toDataURL('image/png');
                        const link = document.createElement('a');
                        link.download = 'pezzetto-digitale-dae.png';
                        link.href = dataURL;
                        link.click();

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

                img.src = 'images/Cuore Bizantino in Mosaico.png';
            });
        </script>
"""

    with open('raccolta-dae.html', 'w', encoding='utf-8') as f:
        f.write(header)
        f.write(dae_content)
        f.write(footer)

update_files()
