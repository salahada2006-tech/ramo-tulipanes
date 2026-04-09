# app.py final y frondoso: Jardín de Nuestra Historia con Lluvia de Corazones y Texto Amarillo

from flask import Flask
import os

app = Flask(__name__)

# Diseño definitivo del "Jardín Mágico Frondoso"
html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Nuestro Jardín Mágico 💖🌻</title>
<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;600&display=swap" rel="stylesheet">

<style>
    body {
        margin: 0;
        height: 100vh;
        display: flex;
        flex-direction: column; /* Alineación vertical para el texto arriba y el jardín abajo */
        align-items: center;
        justify-content: space-between; /* Espacio para el texto y las flores */
        /* --- FONDO NEGRO CON ESTRELLITAS (Como en image_11.png) --- */
        background-color: #000;
        background-image: 
            radial-gradient(white, rgba(255,255,255,.2) 2px, transparent 3px),
            radial-gradient(white, rgba(255,255,255,.15) 1px, transparent 2px),
            radial-gradient(white, rgba(255,255,255,.1) 2px, transparent 3px);
        background-size: 550px 550px, 350px 350px, 250px 250px;
        background-position: 0 0, 40px 60px, 130px 270px;
        overflow: hidden;
    }

    /* --- TEXTO CON MENSAJE ESPECIAL (AMARILLO VIBRANTE) --- */
    .text-overlay {
        margin-top: 15vh; /* Ajuste para que baje un poco del borde superior */
        text-align: center;
        opacity: 0; /* Invisible al inicio */
        transition: opacity 2s ease-in; /* Transición suave */
        font-family: 'Poppins', sans-serif;
        z-index: 10; /* Por encima de todo */
        width: 100%;
    }

    /* Clase para mostrar el texto al final */
    .text-overlay.visible {
        opacity: 1;
    }

    /* TÍTULO PRINCIPAL - ¡HACER RESALTAR! */
    .text-overlay h2 {
        font-family: 'Dancing Script', cursive; /* APLICAMOS FUENTE BONITA y LEGIBLE */
        font-size: 4rem; /* --- ¡¡GIGANTE!! --- Aumentado mucho para resaltar */
        font-weight: 700; /* ¡¡NEGRILLA!! para resaltar */
        margin: 0;
        
        /* --- ¡¡TEXTO AMARILLO VIBRANTE!! (Como en image_11) --- */
        color: #ffff00; /* Color amarillo fuerte */
        text-shadow: 0 0 10px rgba(255, 255, 0, 0.5); /* Contorno amarillo suave */
    }

    /* MENSAJE ESPECIAL POÉTICO (AMARILLO VIBRANTE) */
    .special-message {
        font-family: 'Playfair Display', serif; /* FUENTE POÉTICA */
        font-style: italic;
        font-size: 1.4rem; /* Más grande para legibilidad */
        color: #ffffcc; /* Amarillo muy suave */
        margin: 15px 0;
        line-height: 1.6;
        text-shadow: 0 0 8px rgba(255, 255, 0, 0.3); /* Contorno suave */
    }

    /* EL JARDÍN - Contenedor Principal (Como en image_11.png) */
    /* Mantenemos la lógica de image_8.png para que sea un corazón perfecto */
    .garden-container {
        position: relative;
        width: 600px; /* Ancho para la copa de image_11, ANTES 300 */
        height: 600px; /* Altura total (antes 400) */
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-end; /* Tronco abajo */
    }

    /* TRONCO/TALLOS REALISTAS (SVG) */
    .bouquet-wrapper-svg {
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 100%;
        height: 100%;
        z-index: 2; /* Por encima de los tallos */
        opacity: 0;
        animation: fadeIn 2s ease-in forwards;
        animation-delay: 0.5s; /* Aparece primero */
    }
    /* Estilos para el envoltorio de image_10.png */
    .paper { fill: #f5e0c0; } /* Café clarito */
    .ribbon { fill: #f8c8b8; } /* Rosa clarito */
    .line { fill: none; stroke: #a0522d; stroke-width: 1px; }

    /* COPA DEL JARDÍN - Contenedor invisible al inicio (SOBRE EL ENVOLTORIO) */
    .garden-flowers {
        position: absolute;
        top: 20px; /* Arriba de las ramas (Copa) */
        width: 600px; /* Ancho de la copa */
        height: 600px; /* Altura de la copa (Círculo perfecto) */
        z-index: 1; /* Las flores aparecen entre las ramas */
    }

    /* FLOR INDIVIDUAL MÁGICA (🌻🌻🌻 Como pediste) */
    .flower-magic {
        position: absolute;
        width: 25px; /* Un poco más grandes (antes 20) */
        height: 35px; /* Más alto para la forma de flor */
        background: #ffff66; /* Amarillo vibrante */
        border-radius: 50% 50% 0 0; /* Forma de flor de tulipán/girasol */
        transform: scale(0);
        opacity: 0;
        animation: flowerGrow 1.5s ease-out forwards;
        
        /* --- ¡¡BRILLO MÁGICO!! (Como en image_10.png) --- */
        box-shadow: 0 0 15px rgba(255, 255, 102, 0.8), 
                    0 0 25px rgba(255, 255, 102, 0.5); 
    }
    
    /* Efecto de pétalos */
    .flower-magic::before, .flower-magic::after {
        content: '';
        position: absolute;
        width: 25px;
        height: 35px;
        background: inherit;
        border-radius: inherit;
        top: 0;
        z-index: -1;
    }
    .flower-magic::before { left: -5px; }
    .flower-magic::after { left: 5px; }

    /* --- LLUVIA DE CORAZONES POR TODA LA PANTALLA - Recuperada --- */
    .heart-rain {
        position: absolute;
        width: 12px;
        height: 12px;
        background: #ff0055; /* Color rojo vibrante */
        transform: rotate(-45deg);
        opacity: 0.8;
        animation: heartRainFall linear forwards;
        z-index: 3;
    }

    .heart-rain::before, .heart-rain::after {
        content: '';
        position: absolute;
        width: 12px;
        height: 12px;
        background: inherit;
        border-radius: 50%;
    }

    .heart-rain::before { top: -6px; left: 0; }
    .heart-rain::after { left: 6px; top: 0; }

    /* ANIMACIONES */
    @keyframes fadeIn {
        from { opacity: 0; transform: translate(-50%, 20px); }
        to { opacity: 1; transform: translate(-50%, 0); }
    }

    @keyframes flowerGrow {
        0% { transform: scale(0); opacity: 0; }
        15% { opacity: 1; }
        100% { transform: scale(1); opacity: 0.95; }
    }

    @keyframes heartRainFall {
        0% { transform: translateY(-50px) rotate(-45deg); opacity: 0.8; }
        100% { transform: translateY(110vh) rotate(-45deg); opacity: 0; }
    }
</style>
</head>
<body>

<div class="text-overlay" id="text-overlay">
    <h2>Nuestra historia... 💖</h2>
</div>

<div class="container">
    <div class="garden-container">
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
        <div class="garden-flowers" id="garden-flowers"></div>
    </div>
</div>

<script>
    const gardenFlowers = document.getElementById('garden-flowers');
    const textOverlay = document.getElementById('text-overlay');
    const colors = ['#ffff66', '#ffff99', '#ffffcc', '#fff8dc']; // Variaciones de amarillo vibrante

    // Configuración de la animación progresiva
    const TOTAL_FLOWERS = 150; // --- ¡¡ FRONDOSIDAD GIGANTE !! --- Flores totales para formar el jardín (antes 15)
    const INTERVAL_MS = 100; // Una flor cada 100ms
    const TEXT_DELAY_MS = 2000; // Esperar solo 2s antes de mostrar el texto (Rápido)

    let flowersCreated = 0;

    function createMagicFlower() {
        if (flowersCreated >= TOTAL_FLOWERS) {
            clearInterval(flowerInterval);
            return;
        }

        const flower = document.createElement('div');
        flower.classList.add('flower-magic');
        
        // --- LÓGICA DE DISTRIBUCIÓN ESFÉRICA PERFECTA (COPA REDONDA de image_8) ---
        // Radio de la copa (mitad del diámetro de .garden-flowers)
        const radiusCopa = 280; // Aumentado para el jardín frondoso, ANTES 150
        
        // Lógica de crecimiento ascendente (nace desde abajo)
        const currentProgress = flowersCreated / TOTAL_FLOWERS; // Valor de 0 a 1
        
        // 1. Calculamos la altura (Y) progresivamente, pero dentro de la esfera
        const baseY = 580; // Aumentado para jardín frondoso (antes 280)
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
        const x_final = (radiusCopa + 20) + Math.cos(angle) * actualRadiusX; // Centro X (mitad de la copa)
        const y_final = y_esfera;

        // --- APLICAMOS COORDENADAS ---
        flower.style.left = `${x_final}px`;
        flower.style.top = `${y_final}px`;
        flower.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        
        // Tamaño aleatorio para naturalidad
        const size = Math.random() * 10 + 15; // Más variados y grandes
        flower.style.width = `${size}px`;
        flower.style.height = `${size + 10}px`; // Flores alargadas

        gardenFlowers.appendChild(flower);
        flowersCreated++;
    }

    // --- LLUVIA DE CORAZONES POR TODA LA PANTALLA - Recuperada ---
    function createRainHeart() {
        const heart = document.createElement('div');
        heart.classList.add('heart-rain');
        
        // Posicionamiento horizontal aleatorio por todo el ancho de la pantalla
        heart.style.left = Math.random() * 100 + 'vw';
        
        // Color aleatorio
        heart.style.backgroundColor = '#ff0055'; // Rojo vibrante
        
        // Velocidad aleatoria para naturalidad (caída entre 3 y 6 segundos)
        const fallDuration = Math.random() * 3 + 3;
        heart.style.animationDuration = `${fallDuration}s`;

        document.body.appendChild(heart);

        // Eliminamos el corazón cuando termina su caída para no saturar la memoria
        setTimeout(() => {
            heart.remove();
        }, fallDuration * 1000);
    }

    // --- INICIAMOS LA CREACIÓN PROGRESIVA DE FLORES (EL JARDÍN NACE) ---
    // Esperamos 1s para que el envoltorio se muestre primero
    setTimeout(() => {
        const flowerInterval = setInterval(createMagicFlower, INTERVAL_MS);
    }, 1000);

    // --- INICIAMOS LA LLUVIA DE CORAZONES ---
    setInterval(createRainHeart, 400);

    // --- LÓGICA DEL TEXTO DIFERIDO (¡¡RÁPIDO!!) ---
    // Mostramos el texto tras el retraso configurado (rápido)
    setTimeout(() => {
        textOverlay.classList.add('visible');
    }, TEXT_DELAY_MS);
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
