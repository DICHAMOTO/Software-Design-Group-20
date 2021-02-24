from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Tina Suzuki',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018',
        'requested_gallons': '30',
        'address': '2244 Bake Ave, Houston TX'
    },
    {
        'author': 'Joe Sasaki',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018',
        'requested_gallons': '50',
        'address': '2244 Bake Ave, Houston TX'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route('/fuelquote')
def fuelquote():
    return render_template('fuelquote.html', title='Fuel Quote', post=posts[1])



if __name__ == '__main__':
    app.run(debug=True)