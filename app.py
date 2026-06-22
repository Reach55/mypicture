from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "My Picture Bot is running"

@app.route('/view/<photo_id>')
def view(photo_id):
    return render_template(
        'myimage.html',
        photo=f"/static/photos/{photo_id}.jpg"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)