from flask import Flask, render_template, session, redirect, request # added render_template!
app = Flask(__name__)
app.secret_key="Counter is the key."                    


@app.route('/')
def index():
    if "num" not in session:
        session["num"] = 0
    else:
        session["num"] += 1
    return render_template("index.html")

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/add_two')
def add_two():
    session["num"] +=1
    return redirect('/')

@app.route('/process_count', methods = ['POST'])
def increment():
    numvalue = int(request.form['numvalue'])
    session['num'] += numvalue - 1
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)                   





