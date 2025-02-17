# Dicoding Collection Dashboard Project ✨

Welcome to the Dicoding Collection Dashboard project! This project is focused on analyzing air quality data collected from various monitoring stations in Beijing, China. The data, spanning several years, provides insights into pollution trends, correlations among different pollutants, seasonal variations, and the impact of peak and non-peak hours on air quality. The dashboard was built using **Streamlit** to make the analysis interactive and accessible to users.

You can access the dashboard here: [Dicoding Collection Dashboard](https://air-quality-submission.streamlit.app/)

## Project Overview

The purpose of this project is to explore air quality data from multiple monitoring stations in Beijing, with a focus on visualizing and understanding the relationships between different pollutants, seasonal patterns, and variations during different times of the day. This interactive dashboard makes use of **Pandas**, **Matplotlib**, and **Seaborn** for data analysis and visualization.

### Features:

- **Correlation Analysis**: Examine relationships between pollutants such as PM2.5, PM10, NO2, SO2, and more.
- **Yearly Trends**: Visualize trends in pollutant levels across different years (2013-2017).
- **Seasonal Variations**: Analyze how air quality changes with different seasons.
- **Busy vs Non-Busy Hours**: Compare air quality during peak traffic hours and non-peak hours.

## Dataset

The dataset contains air quality measurements from various monitoring stations in Beijing, collected between **March 2013** and **February 2017**. Data includes concentrations of pollutants such as **PM2.5**, **PM10**, **SO2**, **NO2**, **CO**, and **O3**, along with meteorological factors like **temperature**, **pressure**, and **wind speed**.

### Data Folder

The data used for this project is located in the `Data/` folder and contains CSV files named as follows:

- `PRSA_Data_Aotizhongxin_20130301-20170228.csv`
- `PRSA_Data_Guanyuan_20130301-20170228.csv`
- `PRSA_Data_Changping_20130301-20170228.csv`
- _(and other monitoring stations)_

Each file corresponds to a specific monitoring station and contains hourly data for the mentioned period.

## Requirements

The project dependencies are listed in `requirements.txt`. To install them, run the following command:

```sh
pip install -r requirements.txt
```

### Main Dependencies:

- **streamlit==1.22.0**: Framework for building the dashboard.
- **pandas==1.5.3**: Data manipulation and analysis.
- **matplotlib==3.6.2**: Data visualization.
- **seaborn==0.12.2**: Statistical data visualization.
- **numpy==1.23.5**: Numerical computing.

## Setup Instructions

### Using Anaconda

To set up your environment with Anaconda, use the following commands:

```sh
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

### Using Shell/Terminal with Pipenv

If you prefer using Pipenv to manage your environment:

```sh
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Running the Dashboard

To run the Streamlit dashboard, use the command below:

```sh
streamlit run Dashboard/main.py
```

Make sure you are in the correct directory where `main.py` is located before running this command.

## Directory Structure

```
SUBMISSION/
│
├── .ipynb_checkpoints/       # Checkpoints generated by Jupyter Notebook
├── .venv/                    # Virtual environment folder for dependencies
│
├── Dashboard/                # Main folder containing the Streamlit app and supporting code
│   ├── __pycache__/          # Compiled Python files
│   ├── function.py           # Custom functions used in the Streamlit app
│   ├── main.py               # Main file for the Streamlit dashboard
│   └── requirements.txt      # Required Python packages for the dashboard
│
├── Data/                     # Folder containing air quality datasets from multiple monitoring stations
│   ├── PRSA_Data_Aotizhongxin_20130301-20170228.csv
│   ├── PRSA_Data_Changping_20130301-20170228.csv
│   └── ...                   # Additional CSV files for other monitoring stations
│
├── Proyek_Analisis_Data.ipynb  # Jupyter Notebook for performing exploratory data analysis
├── README.MD                   # README file providing an overview of the project
├── requirements.txt            # Dependencies for the project
└── url.txt                     # Text file containing URLs (possibly data sources or references)
```

## Project Workflow

1. **Data Preparation**: Load and clean the data from CSV files using Pandas.
2. **Exploratory Data Analysis (EDA)**: Perform an initial analysis using `Proyek_Analisis_Data.ipynb` to understand data distribution and relationships.
3. **Dashboard Development**: Build an interactive dashboard using Streamlit to visualize trends, correlations, and seasonal variations in air quality.
4. **Insights Generation**: Present findings in a user-friendly format to help in understanding pollution patterns and making data-driven decisions.

## Insights Generated

1. **Correlation**: PM2.5 and PM10 show a strong correlation, likely due to shared sources such as vehicle emissions and dust. Controlling one pollutant can help reduce the other.
2. **Seasonal Patterns**: Pollutant concentrations are higher during **winter** due to increased heating activities and stagnant weather, and lower during **summer** due to better air dispersion.
3. **Traffic Impact**: Surprisingly, pollutant levels did not show significant differences between busy and non-busy hours, indicating that constant sources like industries may have a more substantial impact.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute it as long as proper credit is given.
