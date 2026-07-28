import streamlit as st
import pandas as pd


# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="Artayb Analytics Studio",
    page_icon="📊",
    layout="wide"
)


# ---------------- APP HEADER ----------------

st.title("Artayb Analytics Studio")

st.caption(
    "Turn your raw CSV data into clear summaries, "
    "visuals, and useful insights."
)


# ---------------- SIDEBAR ----------------

st.sidebar.title("📊 Artayb Studio")

st.sidebar.info(
    "Upload a CSV file to explore, analyze, "
    "and clean your data."
)

st.sidebar.markdown("""
### What you can explore

- Data preview
- Column explorer
- Dataset information
- Missing-data report
- Data types
- Statistical overview
- Interactive visualization
- Data quality score
- Smart cleaning
- Downloadable results
""")


# ---------------- FILE UPLOAD ----------------

uploaded_file = st.file_uploader(
    "Upload your CSV file",
    type=["csv"]
)


# ---------------- DATA ANALYSIS ----------------

if uploaded_file is not None:

    # Save uploaded data in session state
    if (
        "raw_df" not in st.session_state
        or st.session_state.get(
            "uploaded_file_name"
        ) != uploaded_file.name
    ):

        st.session_state["raw_df"] = (
            pd.read_csv(uploaded_file)
        )

        st.session_state["cleaned_df"] = (
            st.session_state["raw_df"].copy()
        )

        st.session_state[
            "uploaded_file_name"
        ] = uploaded_file.name

        st.session_state[
            "is_cleaned"
        ] = False


    # Original dataset
    df = st.session_state["raw_df"]


    # ---------------- SUCCESS MESSAGE ----------------

    st.success(
        "CSV file uploaded successfully!"
    )


    # ---------------- COLUMN EXPLORER ----------------

    st.subheader("🎯 Column Explorer")

    selected_columns = st.multiselect(
        "Choose columns you want to view",
        df.columns.tolist(),
        default=df.columns.tolist()
    )

    if selected_columns:

        st.dataframe(
            df[selected_columns],
            use_container_width=True
        )


    # ---------------- DATA PREVIEW ----------------

    st.subheader("📄 First 5 Records")

    st.dataframe(
        df.head(),
        use_container_width=True
    )


    # ---------------- DATASET INFORMATION ----------------

    st.subheader("📊 Dataset Information")

    col1, col2 = st.columns(2)

    col1.metric(
        "Total Rows",
        df.shape[0]
    )

    col2.metric(
        "Total Columns",
        df.shape[1]
    )

    st.write(
        "**Column Names:**",
        df.columns.tolist()
    )


    # ---------------- MISSING VALUES ----------------

    st.subheader("🔍 Missing Values")

    missing_values = (
        df.isnull().sum()
    )

    st.dataframe(
        missing_values,
        use_container_width=True
    )


    # ---------------- DATA TYPES ----------------

    st.subheader("📋 Data Types")

    st.dataframe(
        df.dtypes,
        use_container_width=True
    )


    # ---------------- STATISTICAL SUMMARY ----------------

    st.subheader(
        "📈 Statistical Summary"
    )

    numeric_columns = (
        df.select_dtypes(
            include="number"
        )
        .columns
        .tolist()
    )

    if numeric_columns:

        st.dataframe(
            df.describe(),
            use_container_width=True
        )

    else:

        st.info(
            "No numeric columns are available "
            "for statistical analysis."
        )


    # ---------------- VISUALIZATION ----------------

    st.subheader(
        "📊 Data Visualization"
    )

    if numeric_columns:

        selected_column = st.selectbox(
            "Select a numeric column",
            numeric_columns
        )

        st.bar_chart(
            df[selected_column]
        )

    else:

        st.warning(
            "No numeric columns were found "
            "for visualization."
        )


    # ---------------- SMART SUMMARY ----------------

    st.subheader(
        "✨ Artayb Smart Summary"
    )

    total_missing = (
        df.isnull().sum().sum()
    )

    st.write(
        f"This dataset contains "
        f"**{df.shape[0]} rows** and "
        f"**{df.shape[1]} columns**."
    )

    if total_missing == 0:

        st.success(
            "Great! No missing values "
            "were found."
        )

    else:

        st.warning(
            f"The dataset contains "
            f"**{total_missing} missing values**."
        )

    if numeric_columns:

        highest_mean_column = (
            df[numeric_columns]
            .mean()
            .idxmax()
        )

        st.info(
            f"**{highest_mean_column}** has "
            f"the highest average value "
            f"among the numeric columns."
        )


    # ---------------- DATA QUALITY ----------------

    st.subheader(
        "🩺 Data Quality Check"
    )

    total_cells = (
        df.shape[0] * df.shape[1]
    )

    if total_cells > 0:

        quality_score = (
            (
                total_cells
                - total_missing
            )
            / total_cells
        ) * 100

        st.metric(
            "Data Quality Score",
            f"{quality_score:.1f}%"
        )

        if quality_score >= 95:

            st.success(
                "Excellent! Your dataset "
                "is highly complete."
            )

        elif quality_score >= 80:

            st.info(
                "Good quality, but some "
                "values may need attention."
            )

        else:

            st.warning(
                "This dataset may need "
                "cleaning before deeper analysis."
            )


    # ---------------- CLEANING SUGGESTIONS ----------------

    st.subheader(
        "🛠️ Smart Cleaning Suggestions"
    )

    columns_with_missing = (
        missing_values[
            missing_values > 0
        ]
    )

    if columns_with_missing.empty:

        st.success(
            "Your dataset does not "
            "contain missing values."
        )

    else:

        for (
            column,
            missing_count
        ) in columns_with_missing.items():

            missing_percentage = (
                missing_count
                / len(df)
            ) * 100

            st.write(
                f"• **{column}** has "
                f"{missing_count} missing "
                f"values "
                f"({missing_percentage:.1f}%)."
            )


    # ---------------- DATA CLEANING ----------------

    st.subheader(
        "🧹 Clean Your Data"
    )

    cleaning_option = st.selectbox(
        "Select a cleaning method",
        [
            "Fill numeric missing values with mean",
            "Remove rows containing missing values"
        ]
    )

    if st.button(
        "Clean Dataset"
    ):

        cleaned_df = df.copy()

        if (
            cleaning_option
            == "Fill numeric missing values with mean"
        ):

            for column in (
                cleaned_df
                .select_dtypes(
                    include="number"
                )
                .columns
            ):

                cleaned_df[column] = (
                    cleaned_df[column]
                    .fillna(
                        cleaned_df[column]
                        .mean()
                    )
                )

            st.success(
                "Numeric missing values "
                "were filled with column averages."
            )

        else:

            cleaned_df = (
                cleaned_df.dropna()
            )

            st.success(
                "Rows containing missing "
                "values were removed."
            )

        st.session_state[
            "cleaned_df"
        ] = cleaned_df

        st.session_state[
            "is_cleaned"
        ] = True


    # ---------------- CLEANING RESULTS ----------------

    if st.session_state[
        "is_cleaned"
    ]:

        cleaned_df = (
            st.session_state[
                "cleaned_df"
            ]
        )

        st.subheader(
            "📊 Cleaning Results"
        )

        col1, col2, col3, col4 = (
            st.columns(4)
        )

        col1.metric(
            "Rows Before",
            df.shape[0]
        )

        col2.metric(
            "Rows After",
            cleaned_df.shape[0]
        )

        col3.metric(
            "Missing Before",
            df.isnull().sum().sum()
        )

        col4.metric(
            "Missing After",
            cleaned_df
            .isnull()
            .sum()
            .sum()
        )

        st.subheader(
            "✅ Cleaned Dataset"
        )

        st.dataframe(
            cleaned_df,
            use_container_width=True
        )

        cleaned_csv = (
            cleaned_df
            .to_csv(
                index=False
            )
            .encode("utf-8")
        )

        st.download_button(
            label="⬇️ Download Cleaned CSV",
            data=cleaned_csv,
            file_name="cleaned_data.csv",
            mime="text/csv"
        )


    # ---------------- DOWNLOAD ORIGINAL DATA ----------------

    st.subheader(
        "⬇️ Download Original Data"
    )

    original_csv = (
        df.to_csv(
            index=False
        )
        .encode("utf-8")
    )

    st.download_button(
        label="Download Original CSV",
        data=original_csv,
        file_name="original_data.csv",
        mime="text/csv"
    )