from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():

    try:
        with open("stats.txt", "r") as f:
            attack_count = f.read()
    except:
        attack_count = "0"

    try:
        with open("top_attacker.txt", "r") as f:
            top_attacker = f.read()
    except:
        top_attacker = "None"

    return render_template_string(f"""
    <html>
    <head>
        <meta http-equiv="refresh" content="2">
        <style>
            body {{
                background: #0f172a;
                color: white;
                text-align: center;
                font-family: Arial;
            }}
            .card {{
                background: #1e293b;
                padding: 20px;
                margin: 20px;
                border-radius: 10px;
                display: inline-block;
            }}
        </style>
    </head>
    <body>
        <h1>🚨 NIDS Dashboard</h1>

        <div class="card">
            <h2>Total Attacks</h2>
            <p>{attack_count}</p>
        </div>

        <div class="card">
            <h2>Top Attacker</h2>
            <p>{top_attacker}</p>
        </div>

    </body>
    </html>
    """)

app.run(host='0.0.0.0', port=5000)
