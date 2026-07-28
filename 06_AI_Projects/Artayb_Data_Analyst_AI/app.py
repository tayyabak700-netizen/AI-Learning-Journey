import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Artayb Data Analyst AI",
    page_icon="🤖",
    layout="wide"
)

st.title("Artayb Analytics Studio")
st.caption(
    "Turn your raw CSV data into clear summaries, visuals, and useful insights."
)

st.sidebar.title("📊 Artayb Studio")

st.sidebar.info(
    "Start by uploading a CSV file. Artayb will organize and summarize your data."
)

st.sidebar.markdown("""
### What you can explore

- Data preview
- Column explorer
- Dataset health check
- Missing-data report
- Statistical overview
- Interactive visualization
- Downloadable results
""")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("🎯 Select Columns")

    selected_columns = st.multiselect(
        "Choose columns you want to view",
        df.columns.tolist(),
        default=df.columns.tolist()
    )

    if selected_columns:
        st.dataframe(df[selected_columns])

    st.success("File uploaded successfully!")
    st.subheader("📄 First 5 Records")
    st.dataframe(df.head())
    st.subheader("📊 Dataset Information")

    st.write("Rows:", df.shape[0])
    st.write("Columns:", df.shape[1])

    st.write("Column Names:")
    st.write(df.columns.tolist())

    st.subheader("🔍 Missing Values")

    missing_values = df.isnull().sum()

    st.write(missing_values)

    st.subheader("📋 Data Types")

    st.write(df.dtypes)

    st.subheader("📈 Statistical Summary")

    st.write(df.describe())

    st.subheader("📊 Data Visualization")

    numeric_columns = df.select_dtypes(include="number").columns.tolist()

    if numeric_columns:
        selected_column = st.selectbox(
            "Select a numeric column",
            numeric_columns
        )

        st.bar_chart(df[selected_column])
    else:
        st.warning("No numeric columns found in this dataset.")

    st.subheader("⬇️ Download Data")

    csv_data = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download CSV",
        data=csv_data,
        file_name="analyzed_data.csv",
        mime="text/csv"
    )

    st.subheader("✨ Artayb Smart Summary")

    total_missing = df.isnull().sum().sum()
    st.write(f"📊 This dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")
    
    if total_missing == 0:
        st.success("✅ Great! No missing values were found in the dataset.")
    else:
        st.warning(
            f"⚠️ The dataset contains {total_missing} missing values."
        )
    
    numeric_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()
    
    if numeric_columns:
        st.write(
            f"🔢 The dataset contains {len(numeric_columns)} numeric columns."
        )
    
        highest_mean_column = df[numeric_columns].mean().idxmax()
    
        st.info(
            f"📈 '{highest_mean_column}' has the highest average value "
            f"among the numeric columns."
        )
    else:
        st.warning(
            "No numeric columns were found for numerical analysis."
        )

    st.subheader("🩺 Data Quality Check")

    total_cells = df.shape[0] * df.shape[1]
    
    if total_cells > 0:
        quality_score = (
            (total_cells - total_missing) / total_cells
        ) * 100
    
        st.metric(
            "Data Quality Score",
            f"{quality_score:.1f}%"
        )
    
        if quality_score >= 95:
            st.success(
                "Excellent! Your dataset is highly complete."
            )
        elif quality_score >= 80:
            st.info(
                "Good quality, but some values may need attention."
            )
        else:
            st.warning(
                "This dataset needs cleaning before deeper analysis."
            )

    st.subheader("🛠️ Smart Cleaning Suggestions")

    missing_by_column = df.isnull().sum()

    columns_with_missing = missing_by_column[
        missing_by_column > 0
    ]

    if columns_with_missing.empty:
        st.success(
            "Your dataset does not contain missing values."
        )
    else:
        st.warning(
            "Some columns contain missing values."
        )

        for column, missing_count in columns_with_missing.items():
            missing_percentage = (
                missing_count / len(df)
            ) * 100

            st.write(
                f"• **{column}** has "
                f"{missing_count} missing values "
                f"({missing_percentage:.1f}%)."
            )

        st.info(
            "Consider filling missing values or removing "
            "rows after checking the importance of each column."
        )

    st.subheader("🧹 Clean Your Data")

    st.write(
        "Choose how you want to handle missing values."
    )

    cleaning_option = st.selectbox(
        "Select a cleaning method",
        [
            "Fill numeric missing values with mean",
            "Remove rows containing missing values"
        ]
    )

    if st.button("Clean Dataset"):

        cleaned_df = df.copy()

        if cleaning_option == (
            "Fill numeric missing values with mean"
        ):

            numeric_columns = cleaned_df.select_dtypes(
                include="number"
            ).columns

            for column in numeric_columns:
                cleaned_df[column] = (
                    cleaned_df[column].fillna(
                        cleaned_df[column].mean()
                    )
                )

            st.success(
                "Numeric missing values were filled with column averages!"
            )

        elif cleaning_option == (
            "Remove rows containing missing values"
        ):

            cleaned_df = cleaned_df.dropna()

            st.success(
                "Rows containing missing values were removed!"
            )
        st.subheader("📊 Cleaning Results")

        before_rows = df.shape[0]
        after_rows = cleaned_df.shape[0]

        before_missing = df.isnull().sum().sum()
        after_missing = cleaned_df.isnull().sum().sum()

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Rows Before",
            before_rows
        )

        col2.metric(
            "Rows After",
            after_rows
        )

        col3.metric(
            "Missing Values Before",
            before_missing
        )

        col4.metric(
            "Missing Values After",
            after_missing
        )

        st.subheader("✅ Cleaned Dataset")

        st.dataframe(cleaned_df)

        cleaned_csv = (
            cleaned_df.to_csv(index=False)
            .encode("utf-8")
        )

        st.download_button(
            label="⬇️ Download Cleaned CSV",
            data=cleaned_csv,
            file_name="cleaned_data.csv",
            mime="text/csv"
        )

    st.subheader("💬 Ask Artayb About Your Data")

    user_question = st.text_input(
        "Ask a question about your dataset"
    )

    if user_question:

        question = user_question.lower()

        if "row" in question:
            st.info(
                f"Your dataset contains {df.shape[0]} rows."
            )

        elif "column" in question:
            st.info(
                f"Your dataset contains {df.shape[1]} columns."
            )

        elif "missing" in question:
            st.info(
                f"Your dataset contains "
                f"{df.isnull().sum().sum()} missing values."
            )

        elif "numeric" in question:
            numeric_count = len(
                df.select_dtypes(
                    include="number"
                ).columns
            )

            st.info(
                f"Your dataset contains "
                f"{numeric_count} numeric columns."
            )

        else:
            st.warning(
                "I can currently answer questions about "
                "rows, columns, missing values, and numeric columns."
            )

    st.subheader("📄 Download Analysis Report")

    report = f"""
ARTAYB ANALYTICS REPORT

Total Rows: {df.shape[0]}
Total Columns: {df.shape[1]}
Total Missing Values: {df.isnull().sum().sum()}

Column Names:
{", ".join(df.columns.tolist())}
"""

    st.download_button(
        label="⬇️ Download Report",
        data=report,
        file_name="artayb_analysis_report.txt",
        mime="text/plain"
    )