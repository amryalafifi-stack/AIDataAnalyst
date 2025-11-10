# Data Analyst & AI Dashboard

*A sneak peek at the AI-powered data exploration dashboard.*


<img width="1651" height="758" alt="Screenshot 2025-11-03 at 12 00 04 PM" src="https://github.com/user-attachments/assets/528e9232-f150-4dc7-b64c-8626aa94206d" />



*LINK TO THE PROJECT*

https://aidataanalyst-knb6ogwr2xnacsy5tzo3h2.streamlit.app/



---

## Project Overview

The **Data Analyst & AI Dashboard** is an interactive Streamlit web app that allows users to **upload CSV datasets**, interact with them using **natural language**, generate **visualizations**, and get **AI-powered insights and recommendations**.  

This tool is designed for **analysts, business professionals, and non-technical users** to quickly explore datasets and derive actionable insights without writing code.


Python serves as both the front-end and back-end engine:

Front-end (Streamlit): Provides a user-friendly interface where anyone can interact with data, select chart types, view AI insights, and download filtered CSVs.

Back-end (Python + Pandas + Plotly + OpenAI API): Handles all data processing, filtering, aggregation, visualization, and communicates with OpenAI to generate human-like analysis and business recommendations.

This approach allows the app to be self-contained, fast, and highly customizable, while making sophisticated data analytics accessible to users without any programming experience.

---

## 1️⃣ Upload Your CSV

- Click the **Upload CSV** button.
- Select your dataset from your local machine.
- The app will automatically parse and display a **sample of the first 5 rows**.
- Supported file types: `.csv`

*Example: Upload a Superstore dataset to explore sales, customers, and regions.*


<img width="1702" height="639" alt="Screenshot 2025-11-03 at 11 41 58 AM" src="https://github.com/user-attachments/assets/ef79d36a-00d1-4b21-a9bb-9f1993e9460a" />




---

## 2️⃣ Ask AI to Filter Your Data

- Enter a **natural language query** in the input box:
  - Examples:
    - `"Show only sales from Kentucky"`
    - `"Top 5 states by revenue"`
    - `"Monthly sales trend in 2020"`
- The AI interprets your query and generates **filters, aggregations, and chart recommendations automatically**.

> The AI ensures that **only the relevant rows are included** in filtered results.

<img width="1605" height="147" alt="Screenshot 2025-11-03 at 12 00 19 PM" src="https://github.com/user-attachments/assets/4e1dec47-8c05-4855-bcda-a0c1534223fd" />



Filtered Data Preview

<img width="1609" height="353" alt="Screenshot 2025-11-03 at 12 00 30 PM" src="https://github.com/user-attachments/assets/c0c5da54-207d-4b7b-838c-1ca94567da35" />


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

<img width="1637" height="536" alt="Screenshot 2025-11-03 at 12 00 49 PM" src="https://github.com/user-attachments/assets/ce6ce93c-a57e-4a8f-a71d-e7a28092055d" />



---

## 4️⃣ AI Insights & Recommendations

- **Quick Insight**: Short summary next to each chart highlighting trends, anomalies, and key takeaways.
- **Full Executive Summary**: Detailed analysis including:
  - What the data is telling us
  - Opportunities and risks
  - Clear actionable recommendations for next steps
- AI summaries are generated from the **filtered dataset**, ensuring accurate insights.
- 

<img width="1639" height="819" alt="Screenshot 2025-11-03 at 12 01 16 PM" src="https://github.com/user-attachments/assets/282432c3-793e-4b6b-83f7-a679761da3b4" />



---


## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/data-analyst-ai.git
cd data-analyst-ai
