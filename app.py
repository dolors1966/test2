from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/prediccio", methods=["POST"])
def prediccio():
    dades = request.get_json()
    # Aquí hi va el model
    resultat = {"risc": "moderat"}  # simulació
    return jsonify(resultat)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
