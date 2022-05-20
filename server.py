from distutils.log import debug
from flask import Flask, render_template

app=Flask(__name__)
@app.route('/')
def hello_world():
    return render_template("index.html",x=8,y=8,color1="red",color2="yellow")

@app.route('/<int:width>')
def given_width(width):
    return render_template("index.html",x=width,y=8,color1="red",color2="yellow")

@app.route('/<int:width>/<int:height>')
def given_all(width,height):
    return render_template("index.html",x=width,y=height,color1="red",color2="yellow")
@app.route('/<int:width>/<int:height>/<string:color1>/<string:color2>')
def given_colors(width,height,color1,color2):
    return render_template("index.html",x=width,y=height,color1=color1,color2=color2) 


if __name__=="__main__":
    app.run(debug=True)