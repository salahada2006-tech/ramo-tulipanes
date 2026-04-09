from flask import Flask
import os

app = Flask(__name__)

html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flores para ti</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background-color: #000;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-family: 'Arial', sans-serif;
        }

        /* Contenedor del jardín */
        #garden {
            position: relative;
            width: 100%;
            height: 100%;
        }

        /* Estilo de la Flor */
        .flower {
            position: absolute;
            bottom: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            animation: grow 3s ease-out forwards;
        }

        /* El Tallo */
        .stem {
            width: 4px;
            background: linear-gradient(to top, #1a4d1a, #2d862d);
            border-radius: 2px;
        }

        /* Las Hojas */
        .leaf {
            position: absolute;
            width: 20px;
            height: 10px;
            background: #2d862d;
            border-radius: 20px 0;
            top: 50%;
        }
        .leaf.right {
            left: 4px;
            transform: rotate(30deg);
        }
        .leaf.left {
            right: 4px;
            transform: rotate(-210deg);
        }

        /* La Cabeza de la Flor (Pétalos) */
        .flower-head {
            position: relative;
            width: 50px;
            height: 50px;
            margin-bottom: -10px;
        }

        .petal {
            position: absolute;
            width: 20px;
            height: 35px;
            background: #ffdb58; /* Amarillo */
            border-radius: 50%;
            left: 15px;
            top: 0;
            transform-origin: center bottom;
            box-shadow: inset 0 0 10px rgba(0,0,0,0.1);
        }

        /* Centro de la flor */
        .center {
            position: absolute;
            width: 18px;
            height: 18px;
            background: #5c3d00;
            border-radius: 50%;
            top: 18px;
            left: 16px;
            z-index: 10;
        }

        /* Mensaje */
        .message {
            position: absolute;
            top: 20%;
            width: 100%;
            text-align: center;
            color: #fff;
            font-size: 2rem;
            text-shadow: 0 0 10px #ffdb58;
            opacity: 0;
            animation: fadeIn 5s ease-in forwards 2s;
        }

        @keyframes grow {
            from { transform: translateY(100vh) scale(0.5); }
            to { transform: translateY(0) scale(1); }
        }

        @keyframes fadeIn {
            to { opacity: 1; }
        }
    </style>
</head>
<body>

<div id="garden">
    <div class="message">Nuestra historia... 💖</div>
</div>

<script>
    const garden = document.getElementById('garden');
    const flowerColors = ['#ffdb58', '#fdfd96', '#fff44f', '#ffea00'];

    function createFlower(x) {
        const flower = document.createElement('div');
        flower.className = 'flower';
        
        // Altura aleatoria del tallo
        const stemHeight = Math.floor(Math.random() * 150) + 100;
        flower.style.left = x + 'px';
        flower.style.bottom = '50px';

        // Cabeza de la flor
        const head = document.createElement('div');
        head.className = 'flower-head';

        // Crear 6 pétalos
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

        // Hojas
        const leafL = document.createElement('div');
        leafL.className = 'leaf left';
        const leafR = document.createElement('div');
        leafR.className = 'leaf right';
        stem.appendChild(leafL);
        stem.appendChild(leafR);

        flower.appendChild(head);
        flower.appendChild(stem);
        garden.appendChild(flower);
    }

    // Crear varias flores normales repartidas
    for (let i = 0; i < 15; i++) {
        const randomX = Math.random() * (window.innerWidth - 100) + 50;
        setTimeout(() => createFlower(randomX), i * 300);
    }
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
