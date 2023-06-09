from flask import Flask, render_template, send_from_directory, request
import generate

templates_dir = "./templates"

app = Flask(__name__, template_folder=templates_dir)

@app.route("/")
def index():
    count = int(request.args.get('count')) if request.args.get('count') else 10
    size = int(request.args.get('size')) if request.args.get('size') else 11
    random_field = generate.generation(gen_count=count, size=size, return_html_field=True)
    return render_template("index.html", field=random_field)

@app.route('/test/post', methods=["GET", "POST"])
def test_post():
    x = int(request.args.get("x"))
    y = int(request.args.get("y"))
    
    generate.base_field.place_room(x, y)
    print([x, y], "\n" , generate.field)
    return generate.create_html()

app.run(host="0.0.0.0", port="5555", debug=True)