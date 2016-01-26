from flask.ext.login import LoginManager
from .models import User

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

login_manager.login_view = 'user.login'
login_manager.login_message = 'Login untuk mengakses link ini'
