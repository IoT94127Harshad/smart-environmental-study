from flask import Flask, render_template, jsonify
import mysql.connector

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="env_monitoring"
    )

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
        SELECT temperature, humidity, gas, timestamp
        FROM sensor_data
        ORDER BY timestamp ASC
    """)
    rows = cursor.fetchall()
    db.close()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(debug=True)