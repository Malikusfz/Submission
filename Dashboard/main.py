import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from function import load_data, categorize_hour, get_season

@st.cache_data
def load_data_cached():
    return load_data()

guanyuan_df = load_data_cached()

st.sidebar.subheader("Explanation")
st.sidebar.markdown("""
This dashboard analyzes air quality data over several years. It includes:
- **Correlation Analysis**: Examines relationships between different pollutants.
- **Yearly Trends**: Shows how pollutant levels change over time.
- **Seasonal Variations**: Compares pollution across different seasons.
- **Busy vs Non-Busy Hours**: Compares pollutant levels during peak traffic times.
""")

st.title("Air Quality Analysis Dashboard")
st.markdown("""
### By: Malikus Syafaadi Nurfaza
Welcome to the air quality analysis dashboard. Here, we will explore correlations between pollutants, weather data, and seasonal variations in air quality, along with other insights derived from the data.
""")

guanyuan_df['Time_Category'] = guanyuan_df.index.hour.map(categorize_hour)

with st.expander("Show Raw Data"):
    st.dataframe(guanyuan_df)

with st.expander("Show Dataset Info"):
    st.write(guanyuan_df.describe())

with st.container():
    st.subheader("Pollutants Distribution")
    columns = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']

    num_columns = len(columns)
    num_rows = (num_columns + 1) // 2
    fig, axes = plt.subplots(num_rows, 2, figsize=(14, 18))
    fig.tight_layout(pad=5.0)
    axes = axes.flatten()

    for i, column in enumerate(columns):
        guanyuan_df[column].hist(bins=30, edgecolor="black", ax=axes[i])
        axes[i].set_title(f'Distribution of {column}')
        axes[i].set_xlabel(f'Skewness: {guanyuan_df[column].skew():.2f}')
        axes[i].set_ylabel('Frequency')

    for j in range(num_columns, len(axes)):
        fig.delaxes(axes[j])

    st.pyplot(fig)

tab1, tab2, tab3 = st.tabs(["Correlation Analysis", "Yearly Trend", "Seasonal Variations"])

with tab1:
    st.subheader("Correlation Between Variables")
    correlation_df = guanyuan_df[columns]
    correlation_matrix = correlation_df.corr()

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5, fmt=".2f", ax=ax)
    st.pyplot(fig)
    plt.close(fig)

with tab2:
    st.subheader("Yearly Trend of PM2.5 and PM10 Concentration")

    all_year_df = guanyuan_df[['PM2.5', 'PM10']].copy()
    all_year_df['year'] = guanyuan_df.index.year
    all_year_df['month'] = guanyuan_df.index.month

    years = list(range(2013, 2018))
    graph_colors = sns.color_palette('Set2', 2)

    fig, axes = plt.subplots(3, 2, figsize=(20, 30))
    fig.tight_layout(pad=6.0)

    axes = axes.flatten()

    for i, year in enumerate(years):
        yearly_data = all_year_df[all_year_df['year'] == year]

        sns.lineplot(data=yearly_data, x='month', y='PM2.5', color=graph_colors[0], marker='o', linestyle='-', linewidth=2.5, label='PM2.5', ax=axes[i])
        sns.lineplot(data=yearly_data, x='month', y='PM10', color=graph_colors[1], marker='^', linestyle='--', linewidth=2.5, label='PM10', ax=axes[i])

        axes[i].set_title(f'Tren Bulanan PM2.5 dan PM10 - Tahun: {year}', fontsize=20, fontweight='bold')
        axes[i].set_xlabel('Bulan', fontsize=16)
        axes[i].set_ylabel('Konsentrasi (ug/m³)', fontsize=16)
        axes[i].set_xticks(range(1, 13))
        axes[i].set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], fontsize=14)
        axes[i].set_xlim(1, 12)
        axes[i].legend(title='Polutan', title_fontsize='15', loc='upper right', fontsize=14)
        axes[i].grid(True, linestyle='--', linewidth=0.7)

    if len(years) < len(axes):
        for j in range(len(years), len(axes)):
            fig.delaxes(axes[j])

    st.pyplot(fig)
    plt.close(fig)

with tab3:
    st.subheader("Seasonal Variations in Air Quality")

    guanyuan_df['Season'] = guanyuan_df.index.month.map(get_season)

    col1, col2 = st.columns(2)

    with col1:
        st.write("PM2.5 Concentration by Season")
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.boxplot(x='Season', y='PM2.5', data=guanyuan_df, palette="Set2", ax=ax)
        st.pyplot(fig)
        plt.close(fig)

    with col2:
        st.write("PM10 Concentration by Season")
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.boxplot(x='Season', y='PM10', data=guanyuan_df, palette="Set2", ax=ax)
        st.pyplot(fig)
        plt.close(fig)

st.subheader("Pollution Levels during Busy and Non-Busy Hours")

busy_nonbusy_avg = guanyuan_df.groupby('Time_Category')[['PM2.5', 'PM10']].mean()

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(busy_nonbusy_avg.index, busy_nonbusy_avg['PM2.5'], color='#1f77b4')
    ax.set_title('Average PM2.5 during Busy and Non-Busy Hours')
    ax.set_xlabel('Time Category')
    ax.set_ylabel('PM2.5 Concentration (ug/m³)')
    st.pyplot(fig)
    plt.close(fig)

with col2:
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(busy_nonbusy_avg.index, busy_nonbusy_avg['PM10'], color='#ff7f0e')
    ax.set_title('Average PM10 during Busy and Non-Busy Hours')
    ax.set_xlabel('Time Category')
    ax.set_ylabel('PM10 Concentration (ug/m³)')
    st.pyplot(fig)
    plt.close(fig)

st.subheader("Conclusion")
st.markdown("""
- **Conclusion Question 1**: From the correlation analysis results, it was found that PM2.5 and PM10 concentrations have a very strong relationship, indicating that they often originate from the same sources, such as vehicle emissions and road dust. Controlling one pollutant has the potential to significantly impact the reduction of the other. Additionally, temperature shows a positive correlation with ozone (O3) concentration, where an increase in temperature tends to increase ozone levels. This can be explained by more active chemical reactions at higher temperatures, especially under strong sunlight conditions, which accelerate the formation of ozone in the air.

- **Conclusion Question 2**: Based on the observed patterns, pollutant concentrations tend to be higher in March and April, possibly due to weather factors, human activities, or certain environmental conditions. Conversely, pollutant concentrations tend to be lower in July and August, which may be influenced by better weather conditions or reduced pollution activities during that period. This seasonal pattern can provide insights for planning more effective air pollution control strategies at certain times of the year.

- **Conclusion Question 3**: From the observed seasonal patterns, pollutant concentrations tend to be higher during winter, possibly due to increased heating activities, air stagnation, or weather conditions that trap pollutants in the atmosphere. Conversely, during summer, pollutant concentrations tend to be lower, possibly due to stronger winds, higher temperatures, and better air mixing, which help disperse pollutants. This understanding can help in designing more effective pollution control policies based on the season.

- **Conclusion Question 4**: Based on the analysis, PM2.5 and PM10 concentrations do not show significant differences between busy and non-busy hours, indicating that traffic activity is not a major factor in air pollution changes. Instead, constant pollution sources, such as industries or combustion, may have a more dominant influence on air quality. Additionally, the higher PM10 concentration compared to PM2.5 in both time categories indicates the need to focus on controlling coarse particles (PM10), which can originate from sources such as dust and construction activities, in efforts to improve overall air quality.
""")