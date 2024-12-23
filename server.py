from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<string:page_name>')
def root(page_name):
    if page_name == '':
        return render_template('load.html', fetchpage="index")
    else:
        return render_template('load.html', fetchpage=page_name)

@app.route('/fetch/<string:page_name>')
def fetch(page_name):
    # Dynamically load the requested template
    return render_template(f'{page_name}.html')

if __name__ == '__main__':
    app.run(port=3000, host='0.0.0.0')
