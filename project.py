from flask import Flask, render_template, url_for

app = Flask(__name__)


# Temporary JSON structures for the history page input
quote_histories = [
    {
        'client_name': 'Sheila W Koga',
        'gallons_requested': '5000',
        'delivery_address': '1989 Scenic Way, Champaign, Illinois(IL), 61820',
        'delivery_date': '03-01-2021',
        'suggested_pice': '$2.05',
        'total_amount': '$10250',
        'quote_created': '02-23-2021'
    },
    {
        'client_name': 'William E Walker',
        'gallons_requested': '2500',
        'delivery_address': '263 Snowbird Lane, Omaha, Nebraska(NE), 68114',
        'delivery_date': '02-28-2021',
        'suggested_pice': '$1.95',
        'total_amount': '$4875',
        'quote_created': '02-21-2021'
    },
    {
        'client_name': 'Robert G Ferreira',
        'gallons_requested': '10500',
        'delivery_address': '673 Cross Street, Saginaw, Michigan(MI), 48601',
        'delivery_date': '04-23-2021',
        'suggested_pice': '$3.00',
        'total_amount': '$31500',
        'quote_created': '01-31-2021'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/history")
def display_history():
    return render_template('history.html', title='History', histories=quote_histories)


if __name__ == '__main__':
    app.run(debug=True)
