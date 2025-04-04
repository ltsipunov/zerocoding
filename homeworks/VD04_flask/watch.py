from flask import Flask, render_template_string
from datetime import datetime
import time

app = Flask(__name__)

@app.route('/')
def index():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    html = '''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Текущее время</title>
        <style>
            body {
                background-color: #e0f0ff;
                text-align: center;
                font-family: 'Arial', sans-serif;
                color: #357;
            }
            h1 {
                font-size: 48px;
                font-family: 'Digital', sans-serif; /* Стиль шрифта техно */
            }
            .timestamp {
                font-size: 36px;
                border:solid;
            }
        </style>
        <script>
            function updateTime() {
                fetch('/time')
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById('current-date').textContent = data.date;
                        document.getElementById('current-time').textContent = data.time;
                    });
            }
            setInterval(updateTime, 2000);
        </script>
    </head>
    <body>
        <h1>Текущее время</h1>
        <div class="timestamp">
                <div id="current-date"></div>
                <div id="current-time" align="center"></div>  
        </div>
    </body>
    </html>
    '''
    return render_template_string(html)

@app.route('/time')
def get_time():
    current_time = datetime.now().strftime('%H:%M:%S')
    current_date = datetime.now().strftime('%Y-%m-%d')
    return {'time': current_time, 'date': current_date}

if __name__ == '__main__':
    app.run(debug=True)