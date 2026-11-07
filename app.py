from flask import Flask, render_template
app = Flask(__name__)

@app.route ('/')
def home():
    return render_template('school.html')

@app.route ('/about')
def about():
    tasks = ["switching",'routing']
    return render_template('activity.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug = True, port = 70000)
