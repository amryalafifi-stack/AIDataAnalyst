import os
import pandas as pd
import streamlit as st
import plotly.express as px
from openai import OpenAI
from io import BytesIO
import base64

# -----------------------------
# STREAMLIT APP CONFIG
# -----------------------------
st.set_page_config(page_title="AI Dashboard By Amr Al-Afifi", layout="wide", page_icon="📊")
st.markdown(
    """
    <style>
      .reportview-container, .main {background-color: #ffffff;}
      .stButton>button {background-color: #2AA3A3; color: white; border-radius: 8px;}
      .chart-card {background: #f8f8f8; border-radius: 8px; padding: 8px; box-shadow: 0 2px 6px rgba(0,0,0,0.08);}
    </style>
    """,
    unsafe_allow_html=True,
)
st.title("📊 AI Powered Dashboard")
st.write("Upload a CSV and ask your data (e.g., 'Top 5 states by Sales'). The AI will filter, visualize, and summarize.")

# -----------------------------
# OPENAI API SETUP
# -----------------------------
OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY")  # <- Use Streamlit Secrets
if not OPENAI_API_KEY:
    st.error("❌ OpenAI API key not found! Add it in Streamlit Secrets.")
    st.stop()

client = OpenAI(api_key=OPENAI_API_KEY)

# -----------------------------
# UPLOAD CSV
# -----------------------------
uploaded_file = st.file_uploader("Upload CSV (any)", type=["csv"])
if not uploaded_file:
    st.info("Upload a CSV file to start.")
    st.stop()

try:
    df = pd.read_csv(uploaded_file)
except Exception as e:
    st.error(f"Could not read CSV: {e}")
    st.stop()

st.subheader("Data Preview (first 5 rows)")
st.dataframe(df.head())

# -----------------------------
# NATURAL LANGUAGE QUERY
# -----------------------------
nl_query = st.text_input("Ask your data (e.g., 'Top 5 states by Sales')", value="")

if st.button("Run Query"):
    if not nl_query.strip():
        st.warning("Please enter a natural-language query.")
        st.stop()

    st.info("Parsing query and generating filtered dataset...")

    prompt = f"""
You are a Python data analyst. Based on this user query, write a Pandas filtering or aggregation operation.
The variable 'df' contains the dataset.
Return ONLY a Python snippet that produces a new DataFrame called 'filtered_df'.
Dataset columns: {list(df.columns)}
User query: {nl_query}

Requirements:
- If top/bottom N requested, ensure numeric sorting
- filtered_df must contain ONLY the rows requested
- Do not include explanations, only code
"""

    try:
        # Call OpenAI API to generate code
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=1
        )

        code_snippet = resp.choices[0].message.content.strip("`python\n").strip("`")
        local_vars = {}

        # Safely execute AI-generated code
        try:
            exec(code_snippet, {"df": df, "pd": pd}, local_vars)
            filtered_df = local_vars.get("filtered_df", None)
            if filtered_df is None or not isinstance(filtered_df, pd.DataFrame):
                raise ValueError("AI did not return a valid DataFrame.")
        except Exception as e:
            st.error(f"❌ Error executing AI-generated code: {e}")
            st.code(code_snippet)
            st.stop()

        # -----------------------------
        # SHOW FILTERED DATA
        # -----------------------------
        st.subheader("Filtered Data Preview (first 5 rows)")
        st.dataframe(filtered_df.head())

        csv_data = filtered_df.to_csv(index=False)
        st.download_button(
            label="📥 Download Filtered CSV",
            data=csv_data,
            file_name="filtered_data.csv",
            mime="text/csv",
        )

        # -----------------------------
        # VISUALIZATION
        # -----------------------------
        numeric_cols = filtered_df.select_dtypes(include='number').columns.tolist()
        categorical_cols = filtered_df.select_dtypes(include='object').columns.tolist()
        chart_type = st.selectbox("Choose chart type", ["Auto", "bar", "line", "pie", "hist", "scatter"])

        fig = None
        if chart_type == "Auto":
            if numeric_cols and categorical_cols:
                x_col = categorical_cols[0]
                y_col = numeric_cols[0]
                fig = px.bar(filtered_df.head(10), x=x_col, y=y_col, color=y_col, title=f"Top 10 {x_col} by {y_col}")
            elif numeric_cols:
                fig = px.histogram(filtered_df, x=numeric_cols[0], nbins=30, title=f"Distribution of {numeric_cols[0]}")
            elif categorical_cols:
                counts = filtered_df[categorical_cols[0]].value_counts().reset_index()
                counts.columns = [categorical_cols[0], "count"]
                fig = px.pie(counts.head(10), names=categorical_cols[0], values="count", title=f"Top {categorical_cols[0]} share")
        else:
            if chart_type == "bar" and numeric_cols and categorical_cols:
                fig = px.bar(filtered_df.head(10), x=categorical_cols[0], y=numeric_cols[0], color=numeric_cols[0])
            elif chart_type == "line" and numeric_cols and categorical_cols:
                fig = px.line(filtered_df.head(10), x=categorical_cols[0], y=numeric_cols[0], markers=True)
            elif chart_type == "pie" and categorical_cols:
                counts = filtered_df[categorical_cols[0]].value_counts().reset_index()
                counts.columns = [categorical_cols[0], "count"]
                fig = px.pie(counts.head(10), names=categorical_cols[0], values="count")
            elif chart_type == "hist" and numeric_cols:
                fig = px.histogram(filtered_df, x=numeric_cols[0], nbins=30)
            elif chart_type == "scatter" and numeric_cols and len(numeric_cols) > 1:
                fig = px.scatter(filtered_df, x=numeric_cols[0], y=numeric_cols[1])

        if fig:
            st.plotly_chart(fig, use_container_width=True)

        # -----------------------------
        # AI SUMMARY
        # -----------------------------
        st.subheader("📝 AI Summary & Recommended Next Steps")
        summary_prompt = f"""
You are a Senior Business Consultant. The filtered dataset has {len(filtered_df)} rows and columns: {list(filtered_df.columns)}.
Provide a detailed analysis in two sections:
1. What the data is telling us (key insights, trends, extremes)
2. Recommended actions / next steps
"""
        summary_resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": summary_prompt}],
        )
        st.write(summary_resp.choices[0].message.content)

    except Exception as e:
        st.error(f"❌ Unexpected error: {e}")
        if 'code_snippet' in locals():
            st.code(code_snippet)
