from flask import Flask, render_template

task_manager = Flask(__name__)

@task_manager.route('/')
def home_page():
    return render_template('school.html')

@task_manager.route('/activity')
def tasks_page():
    tasks = ["SWITCHING", "ROUTING", "FIREWALL", "VPN", "IPV6"]
    return render_template('activity.html', tasks=tasks)

@task_manager.route('/try')
def profile_page():
    return render_template('try.html')


if __name__ == '__main__':
    task_manager.run(debug=True, port=5000)
