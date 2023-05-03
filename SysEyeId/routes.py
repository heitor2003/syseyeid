from flask import Flask, render_template, url_for, redirect
from SysEyeId import app, database, bcrypt
from flask_login import login_required, login_user, logout_user, current_user
from SysEyeId.forms import FormLogin, FormCriarConta, FormExame, FormContato
from SysEyeId.models import Usuario, Exame, Mensagem
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.route("/servicos")
def servicos():
    return render_template("servicos.html")


@app.route("/mensagem_enviada")
def mensagem_enviada():
    return render_template("mensagem_enviada.html")


@app.route("/contato", methods=["GET", "POST"])
def contato():
    formContato = FormContato()
    if formContato.validate_on_submit():
        mensagem = Mensagem(email=formContato.email.data, username=formContato.username.data,
                            mensagem=formContato.mensagem.data)
        database.session.add(mensagem)
        database.session.commit()
        return redirect(url_for("mensagem_enviada"))
    return render_template("contato.html", form=formContato)


@app.route("/login", methods=["GET", "POST"])
def login():
    formlogin = FormLogin()
    if formlogin.validate_on_submit():
        usuario = Usuario.query.filter_by(email=formlogin.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, formlogin.senha.data):
            login_user(usuario)
            return redirect(url_for("perfil", id_usuario=usuario.id))
    return render_template("login.html", form=formlogin)


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    formcadastro = FormCriarConta()
    if formcadastro.validate_on_submit():
        senha = bcrypt.generate_password_hash(formcadastro.senha.data)
        usuario = Usuario(username=formcadastro.username.data, email=formcadastro.email.data,
                          endereco=formcadastro.endereco.data, medico=formcadastro.medico.data,
                          clinica=formcadastro.clinica.data, senha=senha)

        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for("perfil", id_usuario=usuario.id))
    return render_template("cadastro.html", form=formcadastro)


@app.route("/perfil/<id_usuario>", methods=["GET", "POST"])
@login_required
def perfil(id_usuario):
    if int(id_usuario) == int(current_user.id):
        form_exame = FormExame()
        if form_exame.validate_on_submit():
            arquivo = form_exame.exame.data
            nome_seguro = secure_filename(arquivo.filename)
            caminho = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                   app.config["UPLOAD_FOLDER"], nome_seguro)
            arquivo.save(caminho)
            exame = Exame(imagem=nome_seguro, id_usuario=current_user.id)
            database.session.add(exame)
            database.session.commit()
        return render_template("perfil_usuario.html", usuario=current_user, form=form_exame)
    else:
        return render_template("sem_permissao.html", usuario=id_usuario, form=None)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template("index.html")


@app.route("/area_logada/")
@login_required
def area_logada():
    return render_template("area_logada.html")


if __name__ == "__main__":
    app.run(debug=True)

