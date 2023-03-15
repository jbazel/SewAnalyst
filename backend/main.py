# main.py
from flask import render_template, request, flash, Flask, current_app as app
from library import main
from flaskwebgui import FlaskUI
import sys
import os


def resource_path(path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, path)


app = Flask(__name__, template_folder=resource_path("templates"), static_folder=resource_path("static"))


@app.route("/")
def home():
    try:
        print("routing to home, attempting to render template")
        return render_template('index.html')
    except Exception:
        print("render template error")


@app.route("/upload", methods=['POST', 'GET'])
def upload():
    try:
        if request.method == 'POST':
            try:
                f = request.files['csv file']
                file_name = f.filename
                print("uploading file", file_name)

                f.save(os.path.join(sys.executable.removesuffix("SewAnalyst"),("resources/" + file_name)))

                try:
                    main(file_name)
                    flash("your report has been successfully created")
                    return render_template('index.html')

                # exception here means that analysis failed
                except Exception as e:
                    print(e)
                    flash(
                        'there was an error in the analysis of your file, please refer to the log for more information')
                    return render_template('index.html')

            # exception here means the file was not uploaded
            except Exception as e:
                print(e)
                flash('there was an error in the upload of your file, please refer to the log for more information')
                return render_template('index.html')

    except Exception as e:
        print(e)
        return render_template('index.html')


if __name__ == "__main__":
    try:
        app.secret_key = 'session_key'
        app.config['SESSION_TYPE'] = 'filesystem'
        app.debug = False
        FlaskUI(app=app, server="flask").run()
    except Exception as e:
        print("Flask UI failed to start")
        print(e)
