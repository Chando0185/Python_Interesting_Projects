from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "123456":
            return render_template("success.html")
        else:
            return "<h2 style='color:red'>Invalid Credentials</h2>"

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
