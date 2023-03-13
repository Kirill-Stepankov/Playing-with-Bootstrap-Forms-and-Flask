from . import app
from flask import render_template
from flask import request, redirect, url_for
from app.forms import LoginForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('after', login=form.username.data, email=form.email.data))
    return render_template('form.html', title='okaaay', form=form)


@app.route('/after')
def after():
    return render_template('after_submit.html', title='after_submit', login=request.args.get('login'),
                           email=request.args.get('email'))
