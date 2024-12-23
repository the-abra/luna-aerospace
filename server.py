from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route('/')
def root():
    try:
        return render_template("index.html")
    except Exception:
        return render_template('404.html'), 404

@app.route('/<string:page_name>')
def rootplus(page_name):
    if os.path.isfile(f"./templates/{page_name}.html"):
        return render_template("load.html", pagefetch=page_name)
    else:
        return render_template('404.html'), 404
        

@app.route('/fetch/<string:page_name>')
def fetch(page_name):
    # Dynamically load the requested template
    return render_template(f'{page_name}.html')

if __name__ == '__main__':
    app.run(port=3000, debug=True)
