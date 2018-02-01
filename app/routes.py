from app import app

# Just a base homepage to show it working without using Slack
@app.route("/")
@app.route("/index")
def index():
    return "Hello home page"
    # return render_template('index.html')