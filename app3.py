from flask import Flask, render_template

app=Flask(__name__)


@app.route("/language")
def test():
    langs=['C','C++','java','python','Go']
    return render_template("lang.html",langs=langs)


if __name__=='__main__':
    app.run(debug=True)