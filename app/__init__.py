from app.core.helper import create_app
from app.core.db import db
from app.user.loginmanager import login_manager
from flask.ext.bcrypt import Bcrypt
from app.models.post import *
from app.models.user import *
from app.user.views import user_views
from app.post.views import post_views

# Development Config
config = 'config.dev'
# Production Config
# config = 'config.Prod'

app = create_app(config)
db.init_app(app)
login_manager.init_app(app)
bcrypt = Bcrypt(app)

# register blueprint
app.register_blueprint(user_views)
app.register_blueprint(post_views)
