import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# Objective 1: Dataset Overview & Structure

# Load Dataset
filepath = "/Users/prashantbaral/Downloads/whodata.xlsx"
df = pd.read_excel(filepath, sheet_name="AAP_2022_city_v9")

# Basic Dataset Overview
print("Head of dataset:")
print(df.head())

print("\nData Info:")
df.info()

print("\nStatistical Summary:")
df.describe(include='all')

# Objective 2: Data Cleaning & Preprocessing

# Drop unnecessary columns
df.drop(columns=["Status", "Number and type of monitoring stations"], inplace=True)

# Define pollutant columns
pollutants = ["PM2.5 (μg/m3)", "PM10 (μg/m3)", "NO2 (μg/m3)"]

# Handle missing values by filling with mean
for col in pollutants:
    df[col].fillna(df[col].mean(), inplace=True)

# Normalize pollutant values
scaler = StandardScaler()
df_scaled = df.copy()
df_scaled[pollutants] = scaler.fit_transform(df_scaled[pollutants])

# Visualize missing values by column
missing_vals = df.isnull().sum().sort_values(ascending=False)
plt.figure(figsize=(10, 5))
sns.barplot(x=missing_vals.index, y=missing_vals.values)
plt.xticks(rotation=90)
plt.title("Missing Values by Column")
plt.tight_layout()
plt.show()

# Objective 3: Regional Air Quality Analysis

# Visual: Average PM2.5 by WHO Region
region_group = df.groupby("WHO Region")[pollutants].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(data=region_group, x="WHO Region", y="PM2.5 (μg/m3)")
plt.xticks(rotation=45)
plt.title("Average PM2.5 by WHO Region")
plt.tight_layout()
plt.show()

# Visual: PM2.5 Distribution by WHO Region
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="WHO Region", y="PM2.5 (μg/m3)")
plt.xticks(rotation=45)
plt.title("PM2.5 Distribution by WHO Region")
plt.tight_layout()
plt.show()

# Objective 4: City-Level Insights

# Visual: Top 10 Cities by PM2.5
top_pm25 = df.nlargest(10, "PM2.5 (μg/m3)")
plt.figure(figsize=(10, 6))
sns.barplot(data=top_pm25, y="City or Locality", x="PM2.5 (μg/m3)", hue="WHO Country Name", dodge=False)
plt.title("Top 10 Cities by PM2.5 Levels")
plt.tight_layout()
plt.show()

# Visual: Number of Cities per WHO Region
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x="WHO Region", order=df["WHO Region"].value_counts().index)
plt.xticks(rotation=45)
plt.title("Number of Cities per WHO Region")
plt.tight_layout()
plt.show()

# Objective 5: Temporal Trends Analysis

# Visual: Yearly PM2.5 Trend
yearly_trend = df.groupby("Measurement Year")[["PM2.5 (μg/m3)", "NO2 (μg/m3)"]].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.lineplot(data=yearly_trend, x="Measurement Year", y="PM2.5 (μg/m3)", marker='o')
plt.title("Yearly PM2.5 Trend")
plt.tight_layout()
plt.show()

# Objective 6: Statistical & Comparative Analysis

# Visual: Correlation Heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(df[pollutants].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# Visual: PM2.5 vs NO2 Regression
plt.figure(figsize=(8, 6))
sns.regplot(data=df, x="PM2.5 (μg/m3)", y="NO2 (μg/m3)", scatter_kws={'alpha': 0.5})
plt.title("PM2.5 vs NO2 Scatterplot with Regression Line")
plt.tight_layout()
plt.show()

# Objective 7: Temporal Coverage & Distribution Shape

# Visual: Average Temporal Coverage
coverage_cols = ["PM25 temporal coverage (%)", "PM10 temporal coverage (%)", "NO2 temporal coverage (%)"]
avg_coverage = df[coverage_cols].mean()
plt.figure(figsize=(8, 5))
sns.barplot(x=avg_coverage.index, y=avg_coverage.values)
plt.title("Average Temporal Coverage (%)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# Visual: Clean KDE Plot of PM2.5
cleaned_pm25 = [
    float(val) for val in df["PM2.5 (μg/m3)"]
    if isinstance(val, (int, float)) and np.isfinite(val)
]
plt.figure(figsize=(8, 5))
sns.kdeplot(x=cleaned_pm25, fill=True)
plt.title("Clean KDE Plot of PM2.5 (μg/m3)")
plt.xlabel("PM2.5 (μg/m3)")
plt.ylabel("Density")
plt.tight_layout()
plt.show()
