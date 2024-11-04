from flask import Flask,jsonify,request

app = Flask(__name__) 
@app.route('/hii', methods = ['GET']) 

def hii():
    data = "hello how can i hlep you"
    return data

@app.route('/cal_sal', methods = ['GET']) 
def mrg():
    data = "Provide me salary details"
    return data


if __name__ == '__main__':
    app.run(debug= True )