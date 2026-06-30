from flask import Flask, request

app = Flask(__name__)

codes = [
"1234",
"VIP999",
"TEST"
]

@app.route("/check")
def check():

    key = request.args.get("key")

    if key in codes:
        return {"status":"ok"}

    return {"status":"bad"}

app.run(host="0.0.0.0", port=10000)
