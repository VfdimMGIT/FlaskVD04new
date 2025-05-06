
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog')
def blog():
    posts = [
        {'title': 'Первая запись', 'content': 'Содержание первой записи блога'},
        {'title': 'Вторая запись', 'content': 'Содержание второй записи блога'}
    ]
    return render_template('blog.html', posts=posts)

@app.route('/contacts')
def contacts():
    contact_info = {
        'email': 'contact@example.com',
        'phone': '+7 (123) 456-78-90',
        'address': 'г. Москва, ул. Примерная, д. 1'
    }
    return render_template('contacts.html', contacts=contact_info)

if __name__ == '__main__':
    app.run(debug=False)
