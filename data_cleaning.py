import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data.csv")

print("Original Data")
print(df)

# -----------------------------
# Remove Duplicate Rows
# -----------------------------
df = df.drop_duplicates()

# -----------------------------
# Fill Missing Values
# -----------------------------
df["Age"] = df["Age"].fillna(df["Age"].mean())

df["Department"] = df["Department"].fillna("Unknown")

df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# -----------------------------
# Convert Data Types
# -----------------------------
df["Age"] = df["Age"].astype(int)
df["Salary"] = df["Salary"].astype(int)

# -----------------------------
# Save Cleaned Data
# -----------------------------
df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned Data")
print(df)

# -----------------------------
# Generate Report
# -----------------------------
print("\n------ REPORT ------")
print("Total Employees :", len(df))
print("Average Salary :", df["Salary"].mean())
print("Average Age :", df["Age"].mean())

# -----------------------------
# Visual Report
# -----------------------------
salary = df.groupby("Department")["Salary"].mean()

plt.figure(figsize=(6,4))
salary.plot(kind="bar", color="skyblue")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Salary")

plt.tight_layout()
plt.savefig("report.png")

plt.show()

print("\nReport Generated Successfully!")