from flask import Flask, render_template, request
import db_manager

app = Flask(__name__)


@app.route('/')
def hello_world():
    conn = db_manager.get_db_connection()
    tasks = conn.execute('SELECT * FROM todos').fetchall()
    conn.close()
    return render_template("index.html",tasks = tasks)

@app.route('/create', methods=["GET","POST"])
def create():
    if request.method == "POST":
        task = request.form.get('task')

        if not task:
            return "Task is required", 400
    
        db_manager.creat_todo(task)
        return render_template("index.html",tasks = db_manager.get_todo())
    
    return render_template("create.html")

@app.route('/update', methods = ["GET", "PUT"])
def update(task, id_num):
    return render_template("index.html")

@app.route('/delete', methods = ["GET", "DELETE"])
def delete(id_num):
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)