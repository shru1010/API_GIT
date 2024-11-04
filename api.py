from flask import Flask,jsonify,request

app = Flask(__name__) 
@app.route('/hii', methods = ['GET']) 

def hii():
    data = "hello how can i hlep you"
    return data

if __name__ == '__main__':
    app.run(debug= True )