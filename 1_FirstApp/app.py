from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/") # host:port/
def home(): 
    return "Hi Hello, This is the First Flask Application"

@app.route('/demopage1') # host:port/demopage1
def demo1():
    return "<h1>This is Demo Page 1<h1/>"

@app.route('/demopage2') # host:port/demopage2
def demo2():
    return "<h2>This is Demo Page 2<h2/>"
    
@app.route('/justfun') # host:port/justfun ---> it will ridirect to the page which we mention in url_for("pageFunction")
def demo_redirect():
    return redirect(url_for('home'))


if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)