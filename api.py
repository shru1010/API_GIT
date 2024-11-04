from flask import Flask,jsonify,request

app = Flask(__name__) 
@app.route('/hii', methods = ['GET']) 

def hii():
    data = "hello how can i hlep you"
    return data

@app.route('/sal', methods = ['GET']) 
def sal():
    salary = 30000
    return salary


if __name__ == '__main__':
    app.run(debug= True )