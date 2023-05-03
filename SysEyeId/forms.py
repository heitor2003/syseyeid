from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from SysEyeId.models import Usuario


class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Fazer login")


class FormCriarConta(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    username = StringField("Nome de Usuario", validators=[DataRequired()])
    endereco = StringField("Endereço", validators=[DataRequired()])
    medico = IntegerField("Medico", validators=[DataRequired()])
    clinica = IntegerField("Clinica", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField("Confirmação de Senha", validators=[DataRequired(), EqualTo("senha")])
    botao_confirmacao = SubmitField("Criar conta")
    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            return ValidationError("Email já cadastrado")


class FormExame(FlaskForm):
    exame = FileField("Exame", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Enviar")

class FormContato(FlaskForm):
    username = StringField("Nome de Usuario", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    mensagem = StringField("Mensagem", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Enviar")