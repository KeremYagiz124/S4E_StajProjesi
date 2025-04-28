from flask import Flask, render_template, request
from ollamaClient import generate_code

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']    )
def index():
    title, code = None, None

    if request.method == 'POST':
        prompt = request.form.get('prompt')
        if prompt:
            title, code = generate_code(prompt)

    return render_template("index.html", title=title, code=code)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
