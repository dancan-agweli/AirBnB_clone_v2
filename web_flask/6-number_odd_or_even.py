#!/usr/bin/python3
'''A Flask web application.
'''
from flask import Flask, render_template


app = Flask(__name__)
'''Flask application instance.'''
app.url_map.strict_slashes = False


@app.route('/')
def index():
    '''home page.'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''hbnb page.'''
    return 'HBNB'


@app.route('/c/<text>')
def c_page(text):
    '''The c page.'''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>')
@app.route('/python')
def python_page(text='is cool'):
    '''python page.'''
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number_page(n):
    '''number page.'''
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    '''The number_template page.'''
    ctxt = {
        'n': n
    }
    return render_template('5-number.html', **ctxt)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    '''The number_odd_or_even page.'''
    ctxt = {
        'n': n
    }
    return render_template('6-number_odd_or_even.html', **ctxt)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
