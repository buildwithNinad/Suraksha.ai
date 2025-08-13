from flask import Flask, jsonify
from fetcher import fetch_cves
from summarize import summarize_cves

app = Flask(__name__)

@app.route("/cves")
def cves():
    data = fetch_cves()
    summary = summarize_cves(str(data))
    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(debug=True)