from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<page_name>')
def root(page_name):
    if page_name == "nothing":
       return render_template('load.html', fetchpage="index")
       
    else:
        try:
            return render_template(f'{page_name}.html')
        except Exception:
            return render_template('404.html'), 404
        

@app.route('/fetch/<page_name>')
def fetch(page_name):
    # Dynamically load the requested template
    return render_template(f'{page_name}.html')

if __name__ == '__main__':
    app.run(port=3000, debug=True)
