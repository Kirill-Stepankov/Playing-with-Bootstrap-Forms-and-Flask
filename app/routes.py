from . import app
from flask import render_template
from flask import request, redirect, url_for


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if not (request.form['login'] and request.form['email']):
            return render_template('form.html', title='okaaay')
        return redirect(url_for('after', login=request.form['login'], email=request.form['email']))
    return render_template('form.html', title='okaaay')


@app.route('/after')
def after():
    return render_template('after_submit.html', title='after_submit', login=request.args.get('login'), email=request.args.get('email'))
