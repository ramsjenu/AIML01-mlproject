from flask import Flask,request,render_template

app = Flask(__name__, template_folder="templates", static_folder="static")

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        return render_template('index.html')
    

if __name__=="__main__":
    app.run()      
