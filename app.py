from flask import Flask, render_template, request, send_file
import pandas as pd
from io import BytesIO

app = Flask(__name__)


def classify_sector(title):
    title = str(title).lower()

    if any(x in title for x in ["python", "developer", "software", "data", "web"]):
        return "Informatique"
    elif any(x in title for x in ["engineer", "civil", "mechanical"]):
        return "Ingénierie"
    elif any(x in title for x in ["marketing", "sales"]):
        return "Marketing"
    elif any(x in title for x in ["finance", "accounting"]):
        return "Finance"
    elif any(x in title for x in ["design", "ui", "ux"]):
        return "Design"
    else:
        return "Autres"



def load_data():
    try:
        # tentative normale
        df = pd.read_csv("data.csv", sep=",", encoding="utf-8")
    except:
        try:
            # si séparateur ;
            df = pd.read_csv("data.csv", sep=";", encoding="latin1")
        except Exception as e:
            print("❌ ERREUR CSV :", e)
            # fallback (évite crash total)
            df = pd.DataFrame(columns=[
                "id","title","company","location",
                "job_type","salary","date_posted","description","link"
            ])

    
    for col in ["title", "company", "location"]:
        if col not in df.columns:
            df[col] = ""

    return df


@app.route("/", methods=["GET", "POST"])
def home():

    df = load_data()

    
    df["sector"] = df["title"].apply(classify_sector)

    search = request.form.get("search", "")
    selected_sector = request.form.get("sector", "")
    action = request.form.get("action")

    
    if action == "search" and search:
        df = df[
            df["title"].str.contains(search, case=False, na=False) |
            df["company"].str.contains(search, case=False, na=False) |
            df["location"].str.contains(search, case=False, na=False)
        ]

    
    if action == "filter" and selected_sector:
        df = df[df["sector"] == selected_sector]

    
    stats = df["location"].value_counts().head(5)
    sector_stats = df["sector"].value_counts()

    labels = list(stats.index)
    values = [int(x) for x in stats.values]

    sector_labels = list(sector_stats.index)
    sector_values = [int(x) for x in sector_stats.values]

    return render_template(
        "index.html",
        jobs=df.values.tolist(),
        stats=stats,
        labels=labels,
        values=values,
        sector_labels=sector_labels,
        sector_values=sector_values,
        search=search
    )



@app.route("/export")
def export():
    df = load_data()

    output = BytesIO()
    df.to_excel(output, index=False)
    output.seek(0)

    return send_file(output, download_name="jobs.xlsx", as_attachment=True)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)