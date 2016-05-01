from flask import *
from functionsGoHere import *
from FileRetriever import *
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
		
	
	return resp

@app.route('/data', methods=['POST'])
def data():
    if request.method == 'POST':
		if request.form['submit'] == 'Download PPT':
			# si="""title"""
			# output = make_response(si)
			# output.headers["Content-Disposition"] = "attachment; filename=title.ppt"
			# output.headers["Content-type"] = "application/vnd.ms-powerpoint ppt"
			# return output
			return app.send_static_file('title.ppt')

if __name__ == '__main__':
    app.run(debug=True)
