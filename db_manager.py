import sqlite3

def get_db_connection():
    conn = sqlite3.connect('todos.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 테이블 생성 (이미 존재하면 건너뜀)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            complete BOOLEAN NOT NULL DEFAULT 0
        )
    ''')
    
    conn.commit()
    conn.close()

def get_todo():
    conn = get_db_connection()
    cursor = conn.cursor()

    todos = cursor.execute("SELECT * FROM todos").fetchall()

    todos_list = []
    for row in todos:
        todos_list.append({
            'id' : row['id'],
            'task' : row['task'],
            'complete' : row['complete']
        })
    
    conn.close()
    return todos_list

def creat_todo(task):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO todos (task,complete) VALUES (?,?)', (task,False))
    conn.commit()
    todo_id = cursor.lastrowid
    conn.close()
    return todo_id

def update_todo(todo_id, task, complete):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE todos SET task = ?, complete = ? WHERE id = ?', (task, complete, todo_id))
    conn.commit()
    conn.close()

def delete_todo(todo_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM todos WHERE id = ?", (todo_id))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    creat_todo("clean")