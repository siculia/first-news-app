from flask import Flask
from flask import render_template
app = Flask(__name__)  # Note the double underscores on each side!

@app.route("/")
def index():
    template = 'index.html'
    return render_template(template)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
