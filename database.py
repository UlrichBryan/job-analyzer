import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Git47-ZRoot",
        database="job_analyzer"
    )