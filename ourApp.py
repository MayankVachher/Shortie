from flask import *
from functionsGoHere import *
app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def hello_world():
	t = request.method
	resp = ""
	if t == "GET":
		resp = render_template("index.html", quer='', val='')
	else:
		val = request.form["query"]
		resp = render_template("index.html", quer=val, val=genB64here(val))
	return resp

if __name__ == '__main__':
    app.run(debug=True)