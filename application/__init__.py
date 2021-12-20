from flask import Flask, render_template


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/name', methods=['POST'])
def get_name():
    return "This is the name route"


if __name__ == '__main__':
    app.run()
