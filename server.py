from flask import (
    Flask,
    render_template
)

import connexion


# create the application instance
app = connexion.App(__name__, specification_dir='./')

# read the swagger yml file to configure endpoin
app.add_api('swagger.yml')


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
