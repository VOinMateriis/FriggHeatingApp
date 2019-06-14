from flask import Flask, render_template, redirect, url_for, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/getTemperatures', methods=['POST'])
def temperatures():
	
	temperatures = request.form
	
	bed_temp = temperatures["bed"]
	nozzle_temp = temperatures["nozzle"]
	env_temp = temperatures["env"]
	
	print("Bed temperature: " + bed_temp + "°")
	print("Nozzle temperature: " + nozzle_temp + "°")
	print("Env temperature: " + env_temp + "°")
	
	return ''
	
if __name__ == '__main__':
	app.run(debug = True, host = '0.0.0.0')
