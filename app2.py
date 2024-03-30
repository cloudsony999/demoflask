from flask import Flask, render_template

app=Flask(__name__)


@app.route("/home/<name>/<int:age>")
def test(name,age):
    return render_template("home.html",name=name,age=age)


if __name__=='__main__':
    app.run(debug=True)