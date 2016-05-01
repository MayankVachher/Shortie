from flask import *
from functionsGoHere import *
from FileRetriever import *
from ppt_creation import *
app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def hello_world():
	t = request.method
	resp = ""
	if t == "GET":
		resp = render_template("index.html", quer='', val='')
	else:
		val = request.form["query"]
		resp = render_template("index.html", quer=val, val=genB64here(val), ppt_ready = getPPTReadyButton())

		start_process(val)
		pptCreator()
		
	
	return resp

@app.route('/data', methods=['POST'])
def data():
    if request.method == 'POST':
		if request.form['submit'] == 'Download PPT':
			si="""title"""
			output = make_response(si)
			output.headers["Content-Disposition"] = "attachment; filename=title.ppt"
			output.headers["Content-type"] = "application/vnd.ms-powerpoint ppt"
			return output

if __name__ == '__main__':
    app.run(debug=True)
