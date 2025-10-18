from flask import Flask, url_for, render_template
from routes.home import home_route
from routes.cliente import cliente_route

#inicializacao
app = Flask(__name__)

#registro de blueprints
app.register_blueprint(home_route)
app.register_blueprint(cliente_route, url_prefix='/clientes')


#exe
app.run(debug=True)

