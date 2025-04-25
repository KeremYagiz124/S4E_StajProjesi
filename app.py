from flask import Flask, render_template, request
from ollamaClient import generate_code

app = Flask(__name__)

# Anasayfa ve form sayfası
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

"""
# Formdan veri alacak route
@app.route('/submit', methods=['POST'])
def submit():
    # Formdan gelen veriler
    istek = request.form.get('istek')

    # Verileri konsola yazdır
    print(f"istek: {istek}")

    # Kullanıcıya bir cevap döndür
    return f'Teşekkürler, {istek}! Bilgileriniz alındı.'

if __name__ == '__main__':
    app.run(debug=True)
"""
