import mysql.connector


def get_tasks():
    query = "SELECT id, todo, urgent FROM task_list ORDER BY urgent"
    conn = mysql.connector.connect(user='root', password='asdf12345', host='localhost', database='tasks')

    cursor = conn.cursor()
    cursor.execute(query)

    result = cursor.fetchall()

    cursor.close()
    conn.close()
    return result


def get_task(task_id):
    query = "SELECT id, todo, urgent FROM task_list WHERE id = %s ORDER BY urgent"
    conn = mysql.connector.connect(user='root', password='asdf12345', host='localhost', database='tasks')

    cursor = conn.cursor()
    cursor.execute(query, (task_id,))

    result = cursor.fetchone()

    cursor.close()
    conn.close()
    return result


def insert_task(description, priority):
    query = "INSERT INTO task_list(todo, urgent) VALUES (%s, %s)"
    conn = mysql.connector.connect(user='root', password='asdf12345', host='localhost', database='tasks')
    cursor = conn.cursor()
    try:
        cursor.execute(query, (description, priority))
        conn.commit()
    except Exception as e:
        print(str(e))
        conn.rollback()
    cursor.close()
    conn.close()


def update_task(text, priority, task_id):
    query = """UPDATE task_list SET todo=%s, urgent=%s WHERE id=%s"""
    conn = mysql.connector.connect(user='root', password='asdf12345', host='localhost', database='tasks')
    cursor = conn.cursor()

    try:
        cursor.execute(query, (text, priority, task_id))
        conn.commit()
    except Exception as e:
        print(str(e))
        conn.rollback()
    cursor.close()
    conn.close()


def delete_task(task_id):
    query = "DELETE FROM task_list WHERE id = %s"
    conn = mysql.connector.connect(user='root', password='asdf12345', host='localhost', database='tasks')
    cursor = conn.cursor()
    try:
        cursor.execute(query, (task_id,))
        conn.commit()
    except Exception as e:
        print(str(e))
        conn.rollback()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    result = get_tasks()
    print(result)