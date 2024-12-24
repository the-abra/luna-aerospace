from flask import Flask, render_template, send_from_directory
import os, toml



app = Flask(__name__)
FONT_DIR = os.path.join(app.root_path, 'static', 'fonts')
MEDIA_DIR = os.path.join(app.root_path, 'static', 'assests')
config_file = "server.conf"

# Load the TOML file
with open(config_file, 'r') as file:
    config_data = toml.load(file)

title = config_data["Frontend"]["title"]

@app.route('/')
def root():
    try:
        return render_template("load.html", fetchpage="index"), 200
    except Exception:
        return render_template('404.html'), 404

@app.route('/<string:page_name>')
def rootplus(page_name):
    if os.path.isfile(f"./templates/{page_name}.html"):
        return render_template("load.html", fetchpage=page_name, title=title), 200
    else:
        return render_template('404.html'), 404
        

@app.route('/fetch/<string:page_name>')
def fetch(page_name):
    # Dynamically load the requested template
    if os.path.isfile(f"./templates/{page_name}.html"):
        return render_template(f'{page_name}.html'), 200
    else:
        return render_template('404.html'), 404

@app.route('/fonts/<path:filename>')
def serve_font(filename):
    try:
        return send_from_directory(FONT_DIR, filename, mimetype='font/woff')
    except Exception:
        return render_template('404.html'), 404

@app.route('/media/<path:filename>')
def serve_media(filename):
    try:
        return send_from_directory(MEDIA_DIR, filename, mimetype='font/woff')
    except Exception:
        return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(port=3000, debug=True)
