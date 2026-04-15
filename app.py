from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Generate random number
secret_number = random.randint(1, 5)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    guess = ""

    if request.method == 'POST':
        guess = int(request.form['guess'])

        if guess == secret_number:
            result = "🎉 Correct! You Win!"
        else:
            result = f"❌ Wrong! The number was {secret_number}"

    return render_template('index.html', result=result, guess=guess)

if __name__ == '__main__':
    app.run(debug=True)