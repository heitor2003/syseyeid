from SysEyeId import database, app
from SysEyeId.models import Usuario, Exame

with app.app_context():
    database.create_all()