from flask import Flask,jsonify,request

app = Flask(__name__) 
#hi hi hi

@app.route('/hii', methods = ['GET']) 
def hii():
    data = "hello how can i hlep you"
    return data


@app.route('/inc', methods = ['GET']) 
def incentive():
    data = 500
    return data

if __name__ == '__main__':
    app.run(debug= True )
