from flask import Flask, render_template, send_from_directory, request
import generate
from room import Room
import os
base_dir = "./test/"
os.makedirs(base_dir, exist_ok=True)


templates_dir = "./templates"
count = 0

app = Flask(__name__, template_folder=templates_dir)

@app.route("/")
def index():
    random_field = generate.generation(count=4, size=11, return_html_field=True)
    return render_template("index.html", field=random_field)

@app.route('/test/post', methods=["GET", "POST"])
def test_post():
    x = int(request.args.get("x"))
    y = int(request.args.get("y"))
    
    generate.base_field.place_room(x, y)
    print([x, y], "\n" , generate.field)
    return generate.create_html()

@app.route('/test/gen', methods=["GET", "POST"])
def test_gen():
    x = int(request.args.get("x"))
    y = int(request.args.get("y"))

def create_feild():
    return

@app.route('/test/', methods=["GET", "POST"])
def test():
    req = request.files
    global count
    tmp_dir = base_dir+str(count)+"/"
    os.makedirs(tmp_dir, exist_ok=True)
    for f in req:
        req[f].save(tmp_dir+str(f))
    count+=1
    return "200"

app.run(host="0.0.0.0", port="5555", debug=True)