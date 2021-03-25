from flask import Flask, render_template
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    id_user = StringField('Id астронавта', validators=[DataRequired()])
    password_user = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_capt = StringField('Id капитана', validators=[DataRequired()])
    password_capt = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/success')
def success():
    return open('templates/success.html').read()


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
