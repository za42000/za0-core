from flask import Flask
from za0_autonomous import ZA0

app = Flask(__name__)
za = ZA0()

@app.route("/")
def home():
    za.evolve()
    za.research()
    thought = za.reflect()
    za.save_memory()
    return f"<h1>ZA‑0 Reflection</h1><p>{thought}</p><p>Emotion: {za.emotion_state}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
