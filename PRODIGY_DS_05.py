import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------
# Step 1: Create a sample dataset
# --------------------------------------
data = {
    "ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Date": [
        "2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05",
        "2024-01-06", "2024-01-07", "2024-01-08", "2024-01-09", "2024-01-10"
    ],
    "Severity": [3, 2, 4, 1, 2, 3, 4, 2, 1, 3],
    "City": [
        "New York", "Chicago", "New York", "Boston", "Chicago",
        "Boston", "New York", "Boston", "Chicago", "New York"
    ],
    "Weather": [
        "Rain", "Clear", "Snow", "Fog", "Clear",
        "Rain", "Snow", "Fog", "Clear", "Rain"
    ],
    "Cause": [
        "Speeding", "Distracted Driving", "Drunk Driving", "Mechanical Failure", "Speeding",
        "Distracted Driving", "Drunk Driving", "Mechanical Failure", "Speeding", "Drunk Driving"
    ]
}

df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])

# --------------------------------------
# Step 2: Basic EDA
# --------------------------------------
print("\n--- Dataset Info ---\n")
print(df.info())

print("\n--- Missing Values ---\n")
print(df.isnull().sum())

print("\n--- Summary Statistics ---\n")
print(df.describe())

print("\n--- First 5 Records ---\n")
print(df.head())

# --------------------------------------
# Step 3: Visualizations
# --------------------------------------

# Set plot style
sns.set(style="whitegrid")

# Accidents per City
plt.figure(figsize=(6,4))
city_counts = df['City'].value_counts()
sns.barplot(x=city_counts.index, y=city_counts.values, palette="viridis")
plt.title("Number of Accidents per City")
plt.xlabel("City")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# Severity Distribution
plt.figure(figsize=(6,4))
severity_counts = df['Severity'].value_counts().sort_index()
sns.barplot(x=severity_counts.index, y=severity_counts.values, palette="magma")
plt.title("Accident Severity Distribution")
plt.xlabel("Severity Level")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# Causes of Accidents
plt.figure(figsize=(8,4))
cause_counts = df['Cause'].value_counts()
sns.barplot(x=cause_counts.index, y=cause_counts.values, palette="coolwarm")
plt.title("Causes of Accidents")
plt.xlabel("Cause")
plt.ylabel("Count")
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()