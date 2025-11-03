# Data Analyst & AI Dashboard

*A sneak peek at the AI-powered data exploration dashboard.*

<img width="1639" height="819" alt="Screenshot 2025-11-03 at 12 01 16 PM" src="https://github.com/user-attachments/assets/ec369bb7-5f3c-4bc9-b5a6-64c56810b88c" />


---

## Project Overview

The **Data Analyst & AI Dashboard** is an interactive Streamlit web app that allows users to **upload CSV datasets**, interact with them using **natural language**, generate **visualizations**, and get **AI-powered insights and recommendations**.  

This tool is designed for **analysts, business professionals, and non-technical users** to quickly explore datasets and derive actionable insights without writing code.

---

## 1️⃣ Upload Your CSV

- Click the **Upload CSV** button.
- Select your dataset from your local machine.
- The app will automatically parse and display a **sample of the first 5 rows**.
- Supported file types: `.csv`

*Example: Upload a Superstore dataset to explore sales, customers, and regions.*

![Upload CSV Example](./images/upload_csv.png)

---

## 2️⃣ Ask AI to Filter Your Data

- Enter a **natural language query** in the input box:
  - Examples:
    - `"Show only sales from Kentucky"`
    - `"Top 5 states by revenue"`
    - `"Monthly sales trend in 2020"`
- The AI interprets your query and generates **filters, aggregations, and chart recommendations automatically**.

> The AI ensures that **only the relevant rows are included** in filtered results.

![AI Query Example](./images/ai_query.png)

---

## 3️⃣ Visualize the Data

- Choose a chart type or leave **Auto** for AI selection.
- Supported visualizations:
  - **Bar Chart** – compare categorical data
  - **Line Chart** – analyze trends over time
  - **Pie Chart** – see proportions
  - **Histogram** – analyze distributions
  - **Scatter Plot** – explore relationships between numeric fields
- Charts are generated **based on your filtered dataset** and include:
  - **Dynamic axes** based on selected columns
  - **Top N values** if applicable
  - Color-coded metrics for clarity

![Visualization Example](./images/visualization.png)

---

## 4️⃣ AI Insights & Recommendations

- **Quick Insight**: Short summary next to each chart highlighting trends, anomalies, and key takeaways.
- **Full Executive Summary**: Detailed analysis including:
  - What the data is telling us
  - Opportunities and risks
  - Clear actionable recommendations for next steps
- AI summaries are generated from the **filtered dataset**, ensuring accurate insights.

![AI Summary Example](./images/ai_summary.png)

---

## 5️⃣ Download Filtered Data

- After filtering and visualization, click **Download Filtered CSV**.
- The downloaded file contains **only the rows matching your AI query**, ready for reporting or further analysis.

![Download CSV Example](./images/download_csv.png)

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/data-analyst-ai.git
cd data-analyst-ai
