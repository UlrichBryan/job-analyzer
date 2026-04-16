from flask import Flask, render_template, request, send_file
import pandas as pd
from io import BytesIO
from database import get_connection
from analysis import jobs_by_city, jobs_by_sector

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    conn = get_connection()
    cursor = conn.cursor()

    search = request.form.get("search", "")
    selected_sector = request.form.get("sector", "")
    action = request.form.get("action")

    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()

    df = pd.DataFrame(jobs, columns=[
        "id", "title", "company", "location",
        "job_type", "salary", "date_posted", "description", "link"
    ])

    # RECHERCHE
    if action == "search" and search:
        df = df[
            df["title"].str.contains(search, case=False, na=False) |
            df["company"].str.contains(search, case=False, na=False) |
            df["location"].str.contains(search, case=False, na=False)
        ]

    # FILTRE
    sector_stats, full_df = jobs_by_sector()
    if action == "filter" and selected_sector:
        df = full_df[full_df["sector"] == selected_sector]

    stats = jobs_by_city()

    labels = [str(x) for x in stats.index]
    values = [int(x) for x in stats.values]

    sector_labels = [str(x) for x in sector_stats.index]
    sector_values = [int(x) for x in sector_stats.values]

    conn.close()

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
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM jobs", conn)
    conn.close()

    output = BytesIO()
    df.to_excel(output, index=False)
    output.seek(0)

    return send_file(output, download_name="jobs.xlsx", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)