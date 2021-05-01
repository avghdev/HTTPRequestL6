from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    """Renders a sample page."""
    return render_template("index.html")

@app.route("/factorial/<number>")
def factorial(number):
    fact = 1
    for i in range(1, int(number)+1):
        fact = fact * i
    return str(fact)

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
