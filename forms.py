from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length, Email, EqualTo

class FormCriarConta(FlaskForm):
    username = SubmitField('Nome do Usuario', validators=[DataRequired()])
    e-mail = SubmitField('E-mail',validators=[DataRequired(), Email()])
    Senha = PasswordField('Senha',validators=[DataRequired(), length(6 , 20)])
    confirmacao = PasswordField('Confirmar Senha',validators=[DataRequired(), EqualTo("senha")])
    botao_submit_criar_conta = SubmitField('Criar Conta')


class FormLogin(FlaskForm):
    e-mail = SubmitField('E-mail',validators=[DataRequired(), Email])
    Senha = PasswordField('Senha',validators=[DataRequired(), length(6 , 20)])
    botao_submit_login = SubmitField('Fazer Login')
