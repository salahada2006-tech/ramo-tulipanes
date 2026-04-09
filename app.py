# app.py completo para el nuevo proyecto: Ramo Gigante de Tulipanes Mágicos

from flask import Flask
import os

app = Flask(__name__)

# Diseño definitivo del "Ramo Gigante de Tulipanes Mágicos y Brillantes"
html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Nuestro Ramo de Tulipanes Mágicos Brillantes 💖</title>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;600&display=swap" rel="stylesheet">

<style>
    body {
        margin: 0;
        height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        /* --- FONDO OSCURO CON ESTRELLITAS (Como en image_10.png) --- */
        background-color: #000;
        background-image: 
            radial-gradient(white, rgba(255,255,255,.2) 2px, transparent 3px),
            radial-gradient(white, rgba(255,255,255,.15) 1px, transparent 2px),
            radial-gradient(white, rgba(255,255,255,.1) 2px, transparent 3px);
        background-size: 550px 550px, 350px 350px, 250px 250px;
        background-position: 0 0, 40px 60px, 130px 270px;
        overflow: hidden;
    }

    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
        max-width: 600px; /* Ancho para el ramo gigante */
        position: relative;
    }

    /* --- EL RAMO GIGANTE - Contenedor Principal (Como en image_10.png) --- */
    .bouquet-container {
        position: relative;
        width: 450px; /* Copa de flores más ancha (antes 300) */
        height: 550px; /* Altura total (antes 400) */
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-end; /* Envoltorio abajo */
    }

    /* --- ENVOLTORIO Y MOÑO REALISTAS (SVG) --- */
    .bouquet-wrapper-svg {
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 100%;
        height: 100%;
        z-index: 2; /* Por encima de los tallos */
        opacity: 0;
        animation: fadeIn bouquets 2s ease-in forwards;
        animation-delay: 0.5s; /* Aparece primero */
    }
    /* Estilos para el envoltorio y moño SVG (Como en image_10.png) */
    .bouquet-wrapper-svg .paper { fill: #f5e0c0; } /* Café clarito */
    .bouquet-wrapper-svg .ribbon { fill: #f8c8b8; } /* Rosa clarito */
    .bouquet-wrapper-svg .line { fill: none; stroke: #a0522d; stroke-width: 1px; }

    /* COPA DE FLORES - Contenedor invisible al inicio (SOBRE EL ENVOLTORIO) */
    .bouquet-flowers {
        position: absolute;
        top: 20px; /* Arriba de las ramas (Copa) */
        width: 450px; /* Ancho de la copa (antes 300) */
        height: 450px; /* Altura de la copa (Círculo perfecto) */
        z-index: 1; /* Los tulipanes aparecen entre las ramas */
    }

    /* TULIPÁN INDIVIDUAL MÁGICO */
    .tulip-flower {
        position: absolute;
        width: 25px; /* Un poco más grandes (antes 20) */
        height: 35px; /* Más alto para la forma de tulipán */
        background: #ffff66; /* Amarillo vibrante */
        border-radius: 50% 50% 0 0; /* Forma de campana de tulipán */
        transform: scale(0);
        opacity: 0;
        animation: tulipGrow 1.5s ease-out forwards;
        
        /* --- ¡¡BRILLO MÁGICO!! (Como en image_10.png) --- */
        box-shadow: 0 0 15px rgba(255, 255, 102, 0.8), 
                    0 0 25px rgba(255, 255, 102, 0.5); 
    }
    
    /* Efecto de pétalos de tulipán */
    .tulip-flower::before, .tulip-flower::after {
        content: '';
        position: absolute;
        width: 25px;
        height: 35px;
        background: inherit;
        border-radius: inherit;
        top: 0;
        z-index: -1;
    }
    .tulip-flower::before { left: -5px; }
    .tulip-flower::after { left: 5px; }

    /* TEXTO CON MENSAJE ESPECIAL Y CONTADOR - ¡HACER RESALTAR EN FUCSIA! */
    .text-overlay {
        margin-top: -30px; /* Un poco más cerca del ramo */
        text-align: center;
        opacity: 0; /* Invisible al inicio */
        transition: opacity 2s ease-in; /* Transición suave */
        position: relative;
        width: 100%;
        font-family: 'Poppins', sans-serif;
        z-index: 10;
    }

    /* Clase para mostrar el texto al final */
    .text-overlay.visible {
        opacity: 1;
    }

    /* TÍTULO PRINCIPAL - ¡HACER RESALTAR EN FUCSIA! */
    .text-overlay h2 {
        font-family: 'Dancing Script', cursive; /* APLICAMOS FUENTE BONITA y LEGIBLE */
        font-size: 2.8rem;
        font-weight: 700; /* ¡¡NEGRILLA!! para resaltar */
        margin: 0;
        
        /* --- ¡¡TEXTO FUCSIA VIBRANTE!! --- */
        color: #ff007f; /* Color fucsia */
        text-shadow: 0 0 10px rgba(255, 0, 127, 0.5); /* Contorno fucsia suave */
    }

    /* MENSAJE ESPECIAL POÉTICO Y LEGIBLE */
    .special-message {
        font-family: 'Playfair Display', serif; /* FUENTE POÉTICA */
        font-style: italic;
        font-size: 1.2rem;
        color: #fff; /* Blanco para que resalte en oscuro */
        margin: 15px 0;
        line-height: 1.6;
        text-shadow: 0 0 8px rgba(0,0,0,0.5); /* Contorno suave */
    }

    /* CONTADOR - Con fuente legible */
    #time {
        font-size: 1.1rem;
        font-weight: 300;
        margin-top: 15px;
        font-family: 'Poppins', sans-serif;
        color: white;
    }

    /* ANIMACIONES */
    @keyframes fadeInBouquet {
        from { opacity: 0; transform: translate(-50%, 20px); }
        to { opacity: 1; transform: translate(-50%, 0); }
    }

    @keyframes tulipGrow {
        0% { transform: scale(0); opacity: 0; }
        15% { opacity: 1; }
        100% { transform: scale(1); opacity: 0.95; }
    }
</style>
</head>
<body>

<div class="container">
    <div class="bouquet-container">
        <svg class="bouquet-wrapper-svg" viewBox="0 0 600 600" preserveAspectRatio="xMidYMid meet">
            <path class="paper" d="M150,450 C120,400 100,350 110,300 C120,250 150,200 180,180 C210,160 250,150 280,160 C310,170 340,190 360,210 C380,230 400,260 410,300 C420,340 400,380 370,430 Z"/>
            <path class="paper" d="M370,430 L150,450 C180,480 220,500 260,510 C300,520 340,510 370,480 Z"/>
            
            <path class="trunk" d="M300,580 C290,500 280,480 270,450 S250,400 240,380 C230,360 210,340 180,330 S150,300 130,280 C110,260 90,230 100,200 C110,170 140,150 170,160 S200,190 220,210 C240,230 260,250 280,260 C300,270 320,260 340,250 C360,240 380,220 400,200 C420,180 440,160 470,170 C500,180 520,210 510,240 C500,270 480,290 460,310 S430,330 400,340 C370,350 350,370 340,390 C330,410 320,440 310,470 S305,520 300,580 Z M320,280 C330,270 340,260 350,250 S370,230 390,220 C410,210 430,190 450,200 S470,220 460,240 C450,260 430,280 410,290 S390,300 370,310 C350,320 330,300 320,280 Z M280,280 C270,270 260,260 250,250 S230,230 210,220 C190,210 170,190 150,200 S130,220 140,240 C150,260 170,280 190,290 S210,300 230,310 C250,320 270,300 280,280 Z"/>
            
            <path class="ribbon" d="M300,550 L270,520 L240,550 L270,580 Z"/>
            <path class="line" d="M300,550 L300,580"/>
            <path class="line" d="M300,580 C290,590 270,600 250,590 C230,580 220,560 230,540 L260,510 Z"/>
            <path class="line" d="M300,580 C310,590 330,600 350,590 C370,580 380,560 370,540 L340,510 Z"/>
            <path class="line" d="M150,450 C180,420 220,400 260,390 S340,400 370,430"/>
        </svg>
        <div class="bouquet-flowers" id="bouquet-flowers"></div>
    </div>
    
    <div class="text-overlay" id="text-overlay">
        <h2>Nuestra historia... 💖</h2>
        
        <div class="special-message">
            para el amor de mi vida:<br>
            si pudiera elegir un lugar, seria a tu lado.<br>
            Cuanto mas tiempo estoy contigo mas te amo.
        </div>
        
        <div id="time"></div>
    </div>
</div>

<script>
    const bouquetFlowers = document.getElementById('bouquet-flowers');
    const textOverlay = document.getElementById('text-overlay');

    // Configuración de la animación progresiva
    const TOTAL_TULIPS = 350; // --- ¡¡GIGANTE!! --- Tulipanes totales para formar el ramo (antes 300 corazones)
    const INTERVAL_MS = 100; // Un tulipán cada 100ms
    const TEXT_DELAY_MS = 32000; // Esperar 32 segundos antes de mostrar el texto

    let tulipsCreated = 0;

    function createTulip() {
        if (tulipsCreated >= TOTAL_TULIPS) {
            clearInterval(tulipInterval);
            return;
        }

        const tulip = document.createElement('div');
        tulip.classList.add('tulip-flower');
        
        // --- LÓGICA DE DISTRIBUCIÓN ESFÉRICA PERFECTA (COPA REDONDA de image_8) ---
        // Radio de la copa (mitad del diámetro de .bouquet-flowers, ANTES 150)
        const radiusCopa = 190; // Aumentado para el ramo gigante
        
        // Lógica de crecimiento ascendente (nace desde abajo)
        const currentProgress = tulipsCreated / TOTAL_TULIPS; // Valor de 0 a 1
        
        // 1. Calculamos la altura (Y) progresivamente, pero dentro de la esfera
        const baseY = 330; // Aumentado para ramo gigante (antes 280)
        const heightFactor = 2 * radiusCopa; // Diámetro
        const y_esfera = (baseY - radiusCopa) + radiusCopa - (heightFactor * currentProgress); 

        // 2. Calculamos el Radio X Máximo en esta altura Y (Fórmula de la Esfera)
        const yRelativaCentroEsfera = y_esfera - (baseY - radiusCopa); 
        const maxRadiusX = Math.sqrt(Math.pow(radiusCopa, 2) - Math.pow(yRelativaCentroEsfera, 2));

        // 3. Posicionamiento Aleatorio Circular pero acotado por maxRadiusX
        const angle = Math.random() * Math.PI * 2;
        
        // Radio real X se acota para no salir de la esfera
        const randomRadiusFactor = Math.random() * 0.95; // Llenamos más la copa (antes 0.9)
        const actualRadiusX = maxRadiusX * randomRadiusFactor;
        
        // Coordenadas Finales
        const x_final = (radiusCopa + 35) + Math.cos(angle) * actualRadiusX; // Centro X (mitad de la copa)
        const y_final = y_esfera;

        // --- APLICAMOS COORDENADAS ---
        tulip.style.left = `${x_final}px`;
        tulip.style.top = `${y_final}px`;
        
        // Tamaño aleatorio para naturalidad
        const size = Math.random() * 15 + 15; // Más variados y grandes (antes 10)
        tulip.style.width = `${size}px`;
        tulip.style.height = `${size + 10}px`; // Tulipanes alargados

        bouquetFlowers.appendChild(tulip);
        tulipsCreated++;
    }

    // --- INICIAMOS LA CREACIÓN PROGRESIVA DE TULIPANES (EL RAMO NACE) ---
    // Esperamos 2s para que se muestre el envoltorio realista
    setTimeout(() => {
        const tulipInterval = setInterval(createTulip, INTERVAL_MS);
    }, 2000);

    // --- LÓGICA DEL TEXTO DIFERIDO (LAS LETRAS SALEN AL FINAL) ---
    // Mostramos el texto después del retraso configurado
    setTimeout(() => {
        textOverlay.classList.add('visible');
    }, TEXT_DELAY_MS);

    // Contador de tiempo (sin cambios)
    const startDate = new Date("2025-01-01T00:00:00");
    function updateCounter() {
        const now = new Date();
        const diff = now - startDate;
        const d = Math.floor(diff / (1000 * 60 * 60 * 24));
        const h = Math.floor((diff / (1000 * 60 * 60)) % 24);
        const m = Math.floor((diff / (1000 * 60)) % 60);
        const s = Math.floor((diff / 1000) % 60);
        document.getElementById('time').innerHTML = 
            `Juntos hace: ${d}d ${h}h ${m}m ${s}s`;
    }
    setInterval(updateCounter, 1000);
    updateCounter(); // Primera actualización inmediata
</script>

</body>
</html>
"""

@app.route('/')
def home():
    return html_content

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
