# main.py
from flask import render_template, request, flash, Flask
from flask import current_app as app
from library import main
from flaskwebgui import FlaskUI

app = Flask(__name__)


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
                
                f.save("sewanalyst/resources/"+file_name)
                
                try:
                    main(file_name)
                    flash("your report has been successfully created")
                    return render_template('index.html')
                
                # exception here means that analysis failed
                except Exception as e:
                    print(e)
                    flash('there was an error in the analysis of your file, please refer to the log for more information') 
                    return render_template('index.html')
            
            # exception here means the file was not uploaded
            except Exception as e:
                print(e)
                flash('there was an error in the upload of your file, please refer to the log for more information')
                return render_template('index.html')

    except Exception as e:
        print(e)
        return render_template('index.html')


@app.route("/download")
def download():
    try:
        print("routing to download, attempting to render template")
        return render_template('download.html')
    except Exception:
        print("render template error")


if __name__ == "__main__":
    # processData("sampleData.csv")
    try:
        app.secret_key = 'session_key'
        app.config['SESSION_TYPE'] = 'filesystem'
        app.debug = True
        FlaskUI(app=app, server="flask").run()
    except Exception as e:
        print("Flask UI failed to start")
        print(e)
