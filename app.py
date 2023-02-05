from flask import Flask, request, render_template, jsonify
import logging

logging.basicConfig(filename='logs/events.log')

# create logger
logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ch.setFormatter(formatter)

logger.addHandler(ch)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        logger.info('Starting')
        return render_template('index.html')
    except Exception as e:
        print(e)
        logger.error('error in index function')
        logger.error(e)


@app.route('/math', methods=['POST'])  # This will be called from UI
def math_operation():
    try:

        if (request.method=='POST'):
            
            operation=request.form['operation']
            num1=int(request.form['num1'])
            num2 = int(request.form['num2'])

            logger.info(f'the received operation and numbers are {operation}, {num1} and  {num2}')

            if(operation=='add'):
                r=num1+num2
                result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
            if (operation == 'subtract'):
                r = num1 - num2
                result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
            if (operation == 'multiply'):
                r = num1 * num2
                result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
            if (operation == 'divide'):
                r = num1 / num2
                result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
            logging.info(result)
            return render_template('results.html',result=result)

    except Exception as e:
        print(e)
        logger.error('error while processing, in calculator function')
        logger.error(e)


@app.route('/calculator', methods=['POST'])
def calculator():
    try:
        if request.method == 'POST':

            operation = request.json['operation']
            num1 = request.json['num1']
            num2 = request.json['num2']

            if operation == "add":
                result = num1 + num2
            elif operation == "mul":
                result = num1 * num2
            elif operation == "div":
                result = num1 / num2
            else:
                result = num1 - num2

            result =  f"the operation is {operation} and the result is {result}"
            return render_template('results.html',result=result)

    except Exception as e:
        print(e)
        logger.error('error while processing, in calculator function')
        logger.error(e)

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)