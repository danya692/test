from flask import Flask, render_template, session, request, redirect
import sqlite3

app = Flask(__name__)
app.secret_key = 'your-secret-key-123'

@app.route('/')
def index():
    name = session.get('user_name', "Даня")
    return render_template("index.html", name=name)

@app.route("/Hi/<name>")
def hi(name):
    return render_template("hi.html", name=name)

@app.route('/catalog')
def catalog():
    '''cars = [
        {"id": 1, "name": "Hyundai Sonata 2023", "price": "1 800 000 ₽", "year": 2023, "image": "sonata.jpg"},
        {"id": 2, "name": "Kia K5 2023", "price": "1 950 000 ₽", "year": 2023, "image": "k5.jpg"},
        {"id": 3, "name": "Genesis G80", "price": "3 200 000 ₽", "year": 2023, "image": "g80.jpg"},
        {"id": 4, "name": "Toyota Camry", "price": "2 300 000 ₽", "year": 2023, "image": "camry.jpg"},
        {"id": 5, "name": "Mitsubishi Lancer", "price": "1 650 000 ₽", "year": 2023, "image": "lancer.jpg"},
    ]'''


    # Создаем подключение к базе данных (файл my_database.db будет создан)
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Auto')
    cars = cursor.fetchall()
    print(cars)
    connection.close()
    return render_template("catalog.html", cars=cars)

@app.route('/career/')
def career():
    jobs = [
        {"title": "Менеджер по продажам", "salary": "от 80 000 ₽", "experience": "1-3 года"},
        {"title": "Логист", "salary": "от 70 000 ₽", "experience": "2+ года"},
    ]
    return render_template("career.html", jobs=jobs)

@app.route('/feedback/')
def feedback():
    return render_template("feedback.html")

@app.route("/company/")
def company():
    return render_template("company.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route('/set_name', methods=['POST'])
def set_name():
    name = request.form.get('name', '')
    if name:
        session['user_name'] = name
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

