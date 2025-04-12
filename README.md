🌍 WHO Air Quality Analysis Project

This project performs a comprehensive data cleaning and analysis pipeline on air quality data from various cities worldwide. It covers everything from data preprocessing to regional, city-level, and temporal trend analysis, followed by statistical interpretation and visualizations.

📁 Dataset Description

The dataset contains air quality data across different cities and regions:

Columns:

City or Locality: Name of the city or locality.

WHO Country Name: Name of the country as per WHO.

WHO Region: Geographical region (e.g., Africa, Europe, etc.).

Measurement Year: Year of data collection.

PM2.5 (μg/m³): Fine particulate matter with a diameter of less than 2.5 micrometers.

PM10 (μg/m³): Particulate matter with a diameter of less than 10 micrometers.

NO2 (μg/m³): Nitrogen dioxide concentration.

Temporal Coverage: Percentage of time for which the pollutant data is available.

Objectives Completed:
✅ Objective 1: Dataset Overview & Structure

Loaded and displayed basic information of the dataset.

Displayed the first few rows to understand data structure.

Reviewed data types and statistical summaries for better insight.

✅ Objective 2: Data Cleaning & Preprocessing

Dropped unnecessary columns ("Status", "Number and type of monitoring stations").

Filled missing values in the pollutant columns using mean imputation.

Normalized pollutant data using StandardScaler.

Visualized missing values to assess gaps in the dataset.

✅ Objective 3: Regional Air Quality Analysis

Analyzed and visualized average PM2.5 values for each WHO Region.

Generated a boxplot showing the distribution of PM2.5 levels by region.

✅ Objective 4: City-Level Insights

Identified the top 10 cities with the highest PM2.5 levels.

Visualized the number of cities in each WHO Region using a count plot.

✅ Objective 5: Temporal Trends Analysis

Analyzed PM2.5 and NO2 levels over time.

Plotted yearly trends for PM2.5 and NO2 concentrations.

✅ Objective 6: Statistical & Comparative Analysis

Generated a correlation heatmap between pollutants.

Visualized the regression line between PM2.5 and NO2.

✅ Objective 7: Temporal Coverage & Distribution Shape

Calculated the average temporal coverage for pollutants.

Plotted the Kernel Density Estimation (KDE) of PM2.5 values to observe the distribution.

🧠 Insights

Regional Analysis: Pollution levels (especially PM2.5) vary significantly across regions, with some regions exhibiting high pollution levels.

City-Level Insights: The cities with the highest PM2.5 levels are concentrated in specific regions.

Yearly Trends: There are noticeable fluctuations in pollution levels over the years.

Pollutant Correlations: PM2.5 and NO2 show a strong correlation, indicating a potential relationship between the two pollutants.

Temporal Coverage: There are discrepancies in temporal coverage for different pollutants, which affect the analysis of trends.

📊 Tools & Libraries Used

Python (Pandas, NumPy)

Matplotlib for visualization

Seaborn for enhanced data visualization

Scikit-learn for normalization


