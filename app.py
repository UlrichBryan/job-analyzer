from flask import Flask, render_template, request, send_file
import pandas as pd
from io import BytesIO

app = Flask(__name__)

# CLASSIFICATION SECTEUR
def classify_sector(title):
    title = str(title).lower()

    tech = ["python", "developer", "software", "data", "ai", "web"]
    engineering = ["engineer", "mechanical", "civil"]
    marketing = ["marketing", "sales", "seo"]
    finance = ["finance", "accounting", "bank"]
    design = ["design", "ui", "ux"]

    if any(word in title for word in tech):
        return "Informatique"
    elif any(word in title for word in engineering):
        return "Ingénierie"
    elif any(word in title for word in marketing):
        return "Marketing"
    elif any(word in title for word in finance):
        return "Finance"
    elif any(word in title for word in design):
        return "Design"
    else:
        return "Autres"


@app.route("/", methods=["GET", "POST"])
def home():

    # Charger CSV
    df = pd.read_csv("data.csv")

    # Ajouter secteur
    df["sector"] = df["title"].apply(classify_sector)

    search = request.form.get("search", "")
    selected_sector = request.form.get("sector", "")
    action = request.form.get("action")

    # RECHERCHE
    if action == "search" and search:
        df = df[
            df["title"].str.contains(search, case=False, na=False) |
            df["company"].str.contains(search, case=False, na=False) |
            df["location"].str.contains(search, case=False, na=False)
        ]

    # FILTRE
    if action == "filter" and selected_sector:
        df = df[df["sector"] == selected_sector]

    # ANALYSE
    stats = df["location"].value_counts().head(5)
    sector_stats = df["sector"].value_counts()

    labels = list(stats.index)
    values = list(stats.values)

    sector_labels = list(sector_stats.index)
    sector_values = list(sector_stats.values)

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


# EXPORT EXCEL
@app.route("/export")
def export():
    df = pd.read_csv("data.csv")

    output = BytesIO()
    df.to_excel(output, index=False)
    output.seek(0)

    return send_file(output, download_name="jobs.xlsx", as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)