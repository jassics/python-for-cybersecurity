from flask import Flask,render_template,redirect,request
from github.bot import GhBot

app = Flask(__name__)


"""Redirect to Home on startup"""
@app.route('/')
def entry():
    return redirect('/home')

"""Home page"""
@app.route("/home")
def home(params=None):
    params = {"output": "none"}
    return render_template("home.html",params=params)



"""Search Bar"""
@app.route("/home",methods = ['POST'])
def search(params=None):
    if request.method == 'POST':
        username = request.form.get('searchField')  # access the data inside 

        if username == '':
            params = {"status": "error","output": {}}
            return render_template("home.html",params=params)

        else:
            bot = GhBot()
            data_dict,status,msg = bot.serve(content=username)
            output = {
            "status": status,
            "message": msg,
            "data": data_dict
            }
            params = {"status": status,"output":output}
    return render_template("home.html",params=params)



if __name__=="__main__":
    app.run()