from flask import Flask,jsonify,request

app = Flask(__name__) 
@app.route('/hii', methods = ['GET']) 

def hii():
    data = "hello how can i hlep you"
    return data

<<<<<<< HEAD
@app.route('/sal', methods = ['GET']) 
def sal():
    salary = 30000
    return salary

=======

@app.route('/inc', methods = ['GET']) 

def incentive():
    data = 500
    return data
>>>>>>> incentive

if __name__ == '__main__':
    app.run(debug= True )