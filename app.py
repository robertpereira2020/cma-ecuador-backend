from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

comparables_df = pd.read_csv("comparables.csv")
comparables_df["precio_m2"] = comparables_df["precio"] / comparables_df["area"]

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    area = float(data.get("area", 0))
    promedio = comparables_df["precio_m2"].mean()
    valor_estimado = round(promedio * area, 2)
    return jsonify({
        "precio_m2_promedio": round(promedio, 2),
        "valor_sugerido": valor_estimado
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
