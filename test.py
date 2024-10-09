from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Set up MySQL database connection
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Kavish@0901",
  database="qc_db"
)

# Endpoint to log in a QC person
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    person_name = data['person_name']
    cursor = db.cursor()

    # Check if the QC person is already logged in
    query = "SELECT * FROM qc_persons WHERE person_name=%s"
    values = (person_name)
    cursor.execute(query, values)
    result = cursor.fetchone()

    if result:
        # Update the QC person's login time
        query = "UPDATE qc_persons SET login_time=NOW(), status='free' WHERE person_name=%s"
        cursor.execute(query, values)
        db.commit()
        cursor.close()
        return 'QC person logged in'

    else:
        # Add the QC person to the database with login time and status 'free'
        query = "INSERT INTO qc_persons (person_name, login_time, task_assigned, status) VALUES (%s, NOW(), NULL, 'free')"
        cursor.execute(query, values)
        db.commit()
        cursor.close()
        return 'QC person logged in'
@app.route('/logout', methods=['POST'])
def logout():
    data = request.get_json()
    person_name = data['person_name']
    cursor = db.cursor()
    # Update the QC person's status to 'free'
    query = "UPDATE qc_persons SET status='free' WHERE person_name=%s"
    values = (person_name,)
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    return 'QC person logged out'
@app.route('/assign_task', methods=['POST'])
def assign_task():
    cursor= db.cursor()
    query = "SELECT * FROM qc_persons WHERE status='free' AND task_assigned IS NULL ORDER BY login_time ASC LIMIT 1"
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
    # Update the task status to 'in progress' and assign it to the QC person
        task_id = request.get_json()['task_id']
        query = "UPDATE qc_tasks SET status='in progress', assigned_person=%s WHERE task_id=%s"
        values = (result[0], task_id)
        cursor.execute(query, values)

        # Update the QC person's status and task_assigned columns
        query = "UPDATE qc_persons SET status='busy', task_assigned=%s WHERE person_id=%s"
        values = (task_id, result[0])
        cursor.execute(query, values)

        db.commit()
        cursor.close()
        return 'Task assigned to QC person ' + result[1]

    else:
        cursor.close()
        return 'No available QC persons'
@app.route('/complete_task', methods=['POST'])
def complete_task():
    cursor = db.cursor()
    task_id = request.get_json()['task_id']
    # Mark the task as completed
    query = "UPDATE qc_tasks SET status='completed' WHERE task_id=%s"
    values = (task_id,)
    cursor.execute(query, values)

    # Query the database for the QC person who completed the task
    query = "SELECT assigned_person FROM qc_tasks WHERE task_id=%s"
    cursor.execute(query, values)
    result = cursor.fetchone()

    if result:
        # Update the QC person's status and task_assigned columns
        query = "UPDATE qc_persons SET status='free', task_assigned=NULL WHERE person_id=%s"
        values = (result[0],)
        cursor.execute(query, values)

        # Query the database for the next pending task
        query = "SELECT task_id FROM qc_tasks WHERE status='pending' ORDER BY create_time ASC LIMIT 1"
        cursor.execute(query)
        result = cursor.fetchone()

        if result:
            # Assign the next pending task to the QC person who completed the previous task
            query = "UPDATE qc_tasks SET status='in progress', assigned_person=%s WHERE task_id=%s"
            values = (result[0], task_id)
            cursor.execute(query, values)

            # Update the QC person's status and task_assigned columns
            query = "UPDATE qc_persons SET status='busy', task_assigned=%s WHERE person_id=%s"
            values = (result[0], result[1])
            cursor.execute(query, values)
            db.commit()
            cursor.close()
            return 'Task marked as completed and next task assigned to QC person ' + str(result[1])

        else:
            # Update the QC person's status and task_assigned columns
            query = "UPDATE qc_persons SET status='free', task_assigned=NULL WHERE person_id=%s"
            values = (result[0],)
            cursor.execute(query, values)

            db.commit()
            cursor.close()
            return 'Task marked as completed and no pending tasks'

    else:
        cursor.close()
        return 'Task not found'
if __name__ == 'main':
    app.run(debug=True)


       


