import requests
from bs4 import BeautifulSoup
from database import get_connection

url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

jobs = soup.find_all("div", class_="card-content")

conn = get_connection()
cursor = conn.cursor()

for job in jobs:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()
    
    # Valeurs par défaut
    job_type = "N/A"
    salary = "N/A"
    date_posted = "N/A"
    description = "N/A"
    link = "N/A"
    
    query = """
    INSERT INTO jobs (title, company, location, job_type, salary, date_posted, description, link)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    values = (title, company, location, job_type, salary, date_posted, description, link)
    
    cursor.execute(query, values)

conn.commit()
conn.close()

print(" Données insérées avec succès !")