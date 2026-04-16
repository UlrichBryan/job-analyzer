import pandas as pd
from database import get_connection

def jobs_by_city():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM jobs", conn)
    conn.close()
    
    return df["location"].value_counts().head(5)


# jobs by sector
def jobs_by_sector():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM jobs", conn)
    conn.close()

    def classify(title):
        title = title.lower()

        tech_keywords = ["python", "developer", "software", "data", "ai", "machine learning", "web", "backend", "frontend"]
        engineering_keywords = ["engineer", "mechanical", "civil", "electrical"]
        marketing_keywords = ["marketing", "seo", "sales", "business", "advertising"]
        finance_keywords = ["finance", "accounting", "bank", "audit"]
        design_keywords = ["design", "ui", "ux", "graphic"]

        if any(word in title for word in tech_keywords):
            return "Informatique"
        elif any(word in title for word in engineering_keywords):
            return "Ingénierie"
        elif any(word in title for word in marketing_keywords):
            return "Marketing"
        elif any(word in title for word in finance_keywords):
            return "Finance"
        elif any(word in title for word in design_keywords):
            return "Design"
        else:
            return "Autres"

    df["sector"] = df["title"].apply(classify)

    return df["sector"].value_counts(), df