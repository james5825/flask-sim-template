from flask import Flask, render_template
from database.read_data_file import *
from ml.arg_a import *
from flask import request, Blueprint, render_template, abort, jsonify
from jinja2 import TemplateNotFound

app = Flask(__name__)

################################################################
# config backend
################################################################

'''
example of return string
http://127.0.0.1:5000/api1
'''
@app.route('/api1')
def api1():
    return "demo api 1"

'''
example of return dictionary
http://127.0.0.1:5000/api2
'''
@app.route('/api2')
def api2():
    dic = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    return jsonify(dic)

'''
example of return dataframe with to_json
http://127.0.0.1:5000/api5
'''
@app.route('/api5')
def api5():
    return read_csv_demo().to_json(orient='records')


'''
example of read and return json object
http://127.0.0.1:5000/api6
'''
@app.route('/api6')
def api6():
    dic_data = read_json_demo()
    return jsonify(dic_data)

'''
example of utilize ml
http://127.0.0.1:5000/api7
'''
@app.route('/api7',  methods=['GET'])
def api7():
    return some_ml_7()

'''
example of utilize ml
http://127.0.0.1:5000/api8?op1=tet1&op2=test2
'''
@app.route('/api8',  methods=['GET'])
def api8():
    op1 = request.args.get('op1')
    op2 = request.args.get('op2')
    return some_ml_8(op1, op2)

'''
example of utilize ml
http://127.0.0.1:5000/api9
postman>> POST>> Body>> raw>> JSON: {"op1":"str1", "op2": "str2"}
'''
@app.route('/api9',  methods=['POST'])
def api9():
    content = request.json
    return some_ml_8(content["op1"], content["op2"])

################################################################
# frontend view model tempalte
################################################################
@app.route('/page1')
def page1():
    try:
        return render_template(f'page1.html')
    except TemplateNotFound:
        abort(404)

@app.route('/page2')
def page2():
    try:
        return render_template(f'page2.html')
    except TemplateNotFound:
        abort(404)

# an auto mapping route to each page name, by default if no specified, it goes page5
@app.route('/<page_name>')
def show_page_wildcard_a(page_name):
    print(page_name)
    try:
        return render_template(f'{page_name}')
    except TemplateNotFound:
        abort(404)

################################################################
# index page
################################################################
@app.route("/")
def index():
    return render_template("index.html")

################################################################
# app run
################################################################
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
