from flask import Flask
import os

app = Flask(__name__)

html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nuestra Historia 🌻</title>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300&display=swap" rel="stylesheet">
    <style>
        body {
            margin: 0;
            height: 100vh;
            background-color: #000;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            font-family: 'Poppins', sans-serif;
        }

        /* Mensaje Original en Amarillo */
        .container {
            text-align: center;
            z-index: 10;
            position: relative;
            color: #ffff00; /* Amarillo */
        }

        h1 {
            font-family: 'Dancing Script', cursive;
            font-size: 3.5rem;
            margin-bottom: 10px;
            text-shadow: 0 0 10px rgba(255, 255, 0, 0.5);
        }

        .details {
            font-size: 1.2rem;
            line-height: 1.6;
        }

        #timer {
            font-weight: bold;
            margin-top: 15px;
        }

        /* Estilo de las flores originales */
        .flower {
            position: absolute;
            bottom: -100px;
            display: flex;
            flex-direction: column;
            align-items: center;
            animation: grow 2s ease-out forwards;
        }

        .stem {
            width: 4px;
            height: 150px;
            background: linear-gradient(to top, #1a4d1a, #2d862d);
            border-radius: 2px;
        }

        .head {
            position: relative;
            width: 40px;
            height: 40px;
        }

        .petal {
            position: absolute;
            width: 15px;
            height: 25px;
            background: #ffcc00;
            border-radius: 50%;
            left: 12px;
            top: 0;
            transform-origin: center bottom;
        }

        .center {
            position: absolute;
            width: 15px;
            height: 15px;
            background: #5c3d00;
            border-radius: 50%;
            top: 12px;
            left: 12px;
            z-index: 5;
        }

        /* Lluvia de corazones amarillos */
        .heart {
            position: absolute;
            color: #ffff00;
            font-size: 20px;
            user-select: none;
            pointer-events: none;
            animation: fall linear forwards;
        }

        @keyframes grow {
            to { transform: translateY(-100px); }
        }

        @keyframes fall {
            to { transform: translateY(110vh); }
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>Nuestra historia... ❤️</h1>
        <div class="details">
            para el amor de mi vida:<br>
            si pudiera elegir un lugar, seria a tu lado.<br>
            Cuanto mas tiempo estoy contigo mas te amo.
            <div id="timer">Cargando tiempo...</div>
        </div>
    </div>

    <div id="garden"></div>

    <script>
        // Lógica del contador original
        function updateTimer() {
            const startDate = new Date('2024-12-31T00:00:00'); // Ajusta tu fecha aquí
            const now = new Date();
            const diff = now - startDate;

            const days = Math.floor(diff / (1000 * 60 * 60 * 24));
            const hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
            const mins = Math.floor((diff / (1000 * 60)) % 60);
            const secs = Math.floor((diff / 1000) % 60);

            document.getElementById('timer').innerHTML = 
                `Juntos hace: ${days}d ${hours}h ${mins}m ${secs}s`;
        }
        setInterval(updateTimer, 1000);

        // Crear muchas flores (Jardín frondoso)
        const garden = document.getElementById('garden');
        for (let i = 0; i < 80; i++) {
            setTimeout(() => {
                const flower = document.createElement('div');
                flower.className = 'flower';
                flower.style.left = Math.random() * 100 + 'vw';
                flower.style.animationDelay = Math.random() * 2 + 's';
                
                const head = document.createElement('div');
                head.className = 'head';
                for (let j = 0; j < 6; j++) {
                    const petal = document.createElement('div');
                    petal.className = 'petal';
                    petal.style.transform = `rotate(${j * 60}deg)`;
                    head.appendChild(petal);
                }
                const center = document.createElement('div');
                center.className = 'center';
                head.appendChild(center);

                const stem = document.createElement('div');
                stem.className = 'stem';
                stem.style.height = (Math.random() * 100 + 100) + 'px';

                flower.appendChild(head);
                flower.appendChild(stem);
                garden.appendChild(flower);
            }, i * 150);
        }

        // Lluvia de corazones amarillos
        setInterval(() => {
            const heart = document.createElement('div');
            heart.className = 'heart';
            heart.innerHTML = '💛';
            heart.style.left = Math.random() * 100 + 'vw';
            heart.style.top = '-20px';
            heart.style.animationDuration = (Math.random() * 3 + 2) + 's';
            document.body.appendChild(heart);
            setTimeout(() => heart.remove(), 5000);
        }, 200);
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return html_content

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
