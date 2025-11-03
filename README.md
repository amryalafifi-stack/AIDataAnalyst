# Data Analyst AI Dashboard


<img width="1702" height="639" alt="Screenshot 2025-11-03 at 11 41 58 AM" src="https://github.com/user-attachments/assets/99860c74-62f2-4e97-9f8d-9d647e23e64e" />


*A sneak peek at the AI-powered data exploration dashboard.*

## Project Overview
The **Data Analyst & AI Dashboard** is an interactive Streamlit web app that allows users to upload CSV datasets and interact with them using **natural language queries**. The app uses **OpenAI's GPT models** to parse user instructions, filter data accurately, generate visualizations (bar, line, pie, histogram), and provide AI-driven insights and executive summaries.

This tool is designed for **business analysts, data enthusiasts, and non-technical users** to explore datasets quickly and gain actionable insights without coding.

---

## Features

- **Upload any CSV**: Instantly load your dataset for analysis.
- **Natural language filtering**: Ask the AI to filter your data with queries like:
  - "Show only sales from Kentucky"
  - "Top 5 states by revenue"
  - "Monthly sales trend in 2020"
- **Automatic visualizations**: Bar, line, pie, histogram, or scatter plots generated based on your query.
- **AI Insights**:
  - Quick, concise insights next to charts.
  - Full executive summary including recommendations and next steps.
- **Download filtered data**: Export only the rows matching your AI-filtered query.
- **Responsive & interactive UI**: Streamlit interface with light, clean theme for easy interpretation.

---

## Screenshots

### Dashboard Home
![Home](./images/home.png)

### Filtered Data Example
![Filtered Data](./images/filtered_data.png)

### AI Summary & Visuals
![Insights](./images/ai_summary.png)

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/data-analyst-ai.git
cd data-analyst-ai
