/**
 * A Piccoli Passi APS - Menu di Navigazione Mobile (Vanilla JS)
 * Gestione accessibile dell'apertura/chiusura del menu a tendina hamburger.
 * Zero dipendenze esterne, conforme WCAG / WAI-ARIA.
 */
document.addEventListener('DOMContentLoaded', () => {
    const navToggle = document.getElementById('navToggle');
    const mainNav = document.getElementById('mainNav');

    if (!navToggle || !mainNav) return;

    // Toggle apertura / chiusura
    function toggleMenu(forceState) {
        const isOpen = typeof forceState === 'boolean' 
            ? forceState 
            : !mainNav.classList.contains('is-open');

        mainNav.classList.toggle('is-open', isOpen);
        navToggle.classList.toggle('is-active', isOpen);
        navToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
        navToggle.setAttribute('aria-label', isOpen ? 'Chiudi menu di navigazione' : 'Apri menu di navigazione');
    }

    // Click sul pulsante hamburger
    navToggle.addEventListener('click', (e) => {
        e.stopPropagation();
        toggleMenu();
    });

    // Chiudi il menu quando si seleziona una voce (fondamentale per le ancore interne)
    mainNav.querySelectorAll('a').forEach((link) => {
        link.addEventListener('click', () => {
            if (mainNav.classList.contains('is-open')) {
                toggleMenu(false);
            }
        });
    });

    // Chiudi toccando all'esterno della barra di navigazione
    document.addEventListener('click', (e) => {
        if (mainNav.classList.contains('is-open') && !navToggle.contains(e.target) && !mainNav.contains(e.target)) {
            toggleMenu(false);
        }
    });

    // Chiudi con il tasto Escape da tastiera
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && mainNav.classList.contains('is-open')) {
            toggleMenu(false);
            navToggle.focus();
        }
    });

    // Se si ridimensiona la finestra a schermo intero (desktop), chiudi lo stato mobile
    window.addEventListener('resize', () => {
        if (window.innerWidth >= 900 && mainNav.classList.contains('is-open')) {
            toggleMenu(false);
        }
    });
});
