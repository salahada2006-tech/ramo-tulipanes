# app.py final y estable: Jardín Frondoso🌻, Texto Amarillo🌻 y Lluvia Amarilla🌻

from Flask import Flask
import os

app = Flask(__name__)

# Diseño definitivo del "Jardín Mágico Frondoso y Estable"
html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Nuestro Jardín Mágico 🌻💖</title>
<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;600&display=swap" rel="stylesheet">

<style>
    body {
        margin: 0;
        height: 100vh;
        display: flex;
        flex-direction: column; /* Alineación vertical */
        align-items: center;
        justify-content: space-between; /* Espacio para el texto arriba y el jardín abajo */
        /* FONDO NEGRO CON ESTRELLITAS (Como en image_11.png) */
        background-color: #000;
        overflow: hidden;
        font-family: 'Poppins', sans-serif;
    }

    /* --- TEXTO CON MENSAJE ESPECIAL (AMARILLO VIBRANTE) --- */
    .text-overlay {
        margin-top: 15vh; /* Ajuste para que baje un poco del borde superior */
        text-align: center;
        opacity: 0; /* Invisible al inicio */
        transition: opacity 2s ease-in; /* Transición suave */
        position: relative;
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
        font-size: 3rem; /* Aumentado para resaltar */
        font-weight: 700; /* ¡¡NEGRILLA!! para resaltar */
        margin: 0;
        
        /* --- ¡¡TEXTO AMARILLO VIBRANTE!! (Como en image_11) --- */
        color: #ffff00; /* Color amarillo fuerte */
        text-shadow: 0 0 10px rgba(255, 255, 0, 0.5); /* Contorno amarillo suave */
    }

    /* MENSAJE ESPECIAL POÉTICO (AMARILLO VIBRANTE) */
    .special-message {
        font-family: 'Poppins', sans-serif;
        font-size: 1.1rem;
        font-weight: 300;
        
        /* --- ¡¡TEXTO AMARILLO VIBRANTE!! --- */
        color: #ffff00;
        
        margin: 15px 0;
        line-height: 1.6;
        text-shadow: 0 0 5px rgba(255, 255, 0, 0.3); /* Contorno amarillo suave */
    }

    /* CONTADOR - Con fuente legible AMARILLO VIBRANTE */
    #time {
        font-size: 1.1rem;
        font-weight: 300;
        margin-top: 15px;
        color: #ffff00; /* Amarillo fuerte */
    }

    /* --- EL JARDÍN - Contenedor Principal (Sencillo y Estable) --- */
    #garden {
        position: relative;
        width: 100%;
        height: 60vh; /* Altura del jardín ocupando la parte inferior */
        z-index: 1; /* Las flores aparecen entre el tronco */
    }

    /* --- FLOR INDIVIDUAL MÁGICA (🌻 Como pediste) --- */
    /* Usamos la lógica de image_15.png para que sea una flor normal */
    .flower-magic {
        position: absolute;
        bottom: 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        animation: flowerGrow 1.5s ease-out forwards;
        transform: scale(0);
        opacity: 0;
    }
    
    /* El Tallo */
    .stem {
        width: 3px;
        background: linear-gradient(to top, #1a4d1a, #2d862d);
        border-radius: 2px;
    }

    /* La Cabeza de la Flor (Pétalos y Centro🌻) */
    .flower-head {
        position: relative;
        width: 30px;
        height: 30px;
        margin-bottom: -5px;
    }

    .petal {
        position: absolute;
        width: 12px;
        height: 20px;
        background: #ffff66; /* Amarillo vibrante */
        border-radius: 50%;
        left: 9px;
        top: 0;
        transform-origin: center bottom;
        box-shadow: inset 0 0 5px rgba(0,0,0,0.1);
    }

    /* Centro de la flor🌻 */
    .center {
        position: absolute;
        width: 10px;
        height: 10px;
        background: #5c3d00;
        border-radius: 50%;
        top: 10px;
        left: 10px;
        z-index: 10;
    }

    /* --- LLUVIA DE CORAZONES AMARILLOS POR TODA LA PANTALLA --- */
    .heart-rain {
        position: absolute;
        color: #ffffcc; /* Amarillo suave brillante */
        font-size: 20px;
        user-select: none;
        pointer-events: none;
        animation: heartRainFall linear forwards;
        z-index: 3; /* Por encima del jardín, debajo del texto */
    }

    /* ANIMACIONES */
    @keyframes flowerGrow {
        from { transform: translateY(100px) scale(0); opacity: 0; }
        to { transform: translateY(0) scale(1); opacity: 0.95; }
    }

    @keyframes heartRainFall {
        to { transform: translateY(110vh); }
    }
</style>
</head>
<body>

<div class="text-overlay" id="text-overlay">
    <h2>Nuestra historia... 💖🌻</h2>
</div>

<div id="garden"></div>

<script>
    const garden = document.getElementById('garden');
    const textOverlay = document.getElementById('text-overlay');
    const flowerColors = ['#ffff66', '#ffff99', '#ffffcc', '#fff8dc']; // Variaciones de amarillo vibrante

    // Configuración de la animación progresiva
    const TOTAL_FLOWERS = 150; // --- ¡¡ FRONDOSIDAD GIGANTE !! --- Flores totales repartidas (antes 15)
    const INTERVAL_MS = 100; // Una flor cada 100ms
    const TEXT_DELAY_MS = 28000; // Esperar 28 segundos antes de mostrar el texto

    let flowersCreated = 0;

    function createMagicFlower() {
        if (flowersCreated >= TOTAL_FLOWERS) {
            clearInterval(flowerInterval);
            return;
        }

        const flower = document.createElement('div');
        flower.className = 'flower-magic';
        
        // --- LÓGICA DE DISTRIBUCIÓN FRONDOSA (Como pediste🌻🌻🌻) ---
        // Posicionamiento horizontal aleatorio por todo el ancho de la pantalla
        const randomX = Math.random() * (window.innerWidth - 60) + 30; // Evitamos los bordes
        
        // Altura aleatoria del tallo para naturalidad
        const stemHeight = Math.floor(Math.random() * 150) + 100;
        flower.style.left = randomX + 'px';
        flower.style.bottom = '50px'; // Un poco sobre el fondo

        // Cabeza de la flor
        const head = document.createElement('div');
        head.className = 'flower-head';

        // Crear 6 pétalos (flores normales sunflower-like)
        for (let i = 0; i < 6; i++) {
            const petal = document.createElement('div');
            petal.className = 'petal';
            petal.style.transform = `rotate(${i * 60}deg)`;
            petal.style.backgroundColor = flowerColors[Math.floor(Math.random() * flowerColors.length)];
            head.appendChild(petal);
        }

        const center = document.createElement('div');
        center.className = 'center';
        head.appendChild(center);

        // Tallo
        const stem = document.createElement('div');
        stem.className = 'stem';
        stem.style.height = stemHeight + 'px';

        flower.appendChild(head);
        flower.appendChild(stem);
        garden.appendChild(flower);
        flowersCreated++;
    }

    // --- LLUVIA DE CORAZONES AMARILLOS POR TODA LA PANTALLA ---
    setInterval(() => {
        const heart = document.createElement('div');
        heart.innerHTML = '❤️';
        heart.className = 'heart-rain';
        
        // Posicionamiento horizontal aleatorio por todo el ancho de la pantalla
        heart.style.left = Math.random() * 100 + 'vw';
        
        // Altura inicial arriba (fuera de la pantalla)
        heart.style.top = '-20px';
        
        // Velocidad aleatoria para naturalidad (caída entre 3 y 6 segundos)
        const fallDuration = Math.random() * 3 + 3;
        heart.style.animationDuration = `${fallDuration}s`;

        document.body.appendChild(heart);

        // Eliminamos el corazón cuando termina su caída para no saturar la memoria
        setTimeout(() => {
            heart.remove();
        }, fallDuration * 1000);
    }, 300); // Un corazón cada 300ms

    // --- INICIAMOS LA CREACIÓN PROGRESIVA DE FLORES (EL JARDÍN NACE) ---
    // Esperamos 1.5s para que se muestre primero el fondo estrellado
    setTimeout(() => {
        const flowerInterval = setInterval(createMagicFlower, INTERVAL_MS);
    }, 1500);

    // --- LÓGICA DEL TEXTO DIFERIDO (LAS LETRAS SALEN AL FINAL) ---
    // Mostramos el texto después del retraso configurado
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
