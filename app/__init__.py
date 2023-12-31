from flask import Flask
from .config  import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy    
from .mi_blueprint import mi_blueprint
from app.productos import productos
from flask_bootstrap import Bootstrap

# Inicializa el objeto flask
app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)

# Inicializa el objeto de SQLAlchemy
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Registra modulos(Blueprints)
app.register_blueprint(mi_blueprint)
app.register_blueprint(productos)

from .models import Cliente, Venta, Producto, Detalle

