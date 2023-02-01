from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return page1()

@app.route('/letter1')
def page1():  # put application's code here
    return render_template('index.html')

@app.route('/letter2')
def page2():  # put application's code here
    return render_template('letter2.html')

@app.route('/letter3')
def page3():  # put application's code here
    return render_template('letter3.html')

@app.route('/letter4')
def page4():  # put application's code here
    return render_template('letter4.html')


if __name__ == '__main__':
    app.run()
