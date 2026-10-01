from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/order", methods=["POST"])
def order():
    data = request.json

    print("New Order:")
    print(data)

    return jsonify({
        "success": True,
        "message": "Order received successfully!"
    })


if __name__ == "__main__":
    app.run(debug=True)