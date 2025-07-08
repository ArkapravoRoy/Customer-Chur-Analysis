import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

data=pd.read_csv(r"C:\Users\NeelLaptop\Desktop\Python\Youtube\Project1\Telco-Customer-Churn.csv")
# print(data.info())
# Replacing empty values to 0 in 'TotalCharges' column
data["TotalCharges"]=data["TotalCharges"].replace(" ","0")
data["TotalCharges"]=data["TotalCharges"].astype(float)
# print(data.info())
# print(data.isnull().sum())  # Checking for null values in the dataset
# print(data.duplicated().sum())  # Checking for duplicate rows in the dataset

#Converting SeniorCitizen to Object
def Convert(abc):
    if abc==1:
        return "Yes"
    else:
        return "No"

data["SeniorCitizen"]=data["SeniorCitizen"].apply(Convert)
# print(data.head(30))

ab=sb.countplot(x="Churn",data=data)
ab.bar_label(ab.containers[0])  # Adding labels to the bars in the count plot
plt.title("Count of Churned Customers")
plt.show()  # Plotting the count of churned customers
#showing using pie chart
churn=data["Churn"].value_counts()
plt.pie(churn,autopct="%1.1f%%",colors=["skyblue","lightgreen"])
plt.title("Churn Distribution")     
plt.show()  # Plotting the pie chart for churn distribution

sb.countplot(x="SeniorCitizen",data=data,hue="Churn")
plt.title("Senior Citizens by Churn Status")
plt.show()

ct = pd.crosstab(data['SeniorCitizen'], data['Churn'])

# Step 2: Convert to percentages
ct_percent = ct.div(ct.sum(axis=1), axis=0) * 100

# Step 3: Plot stacked bar chart manually
ax = ct_percent.plot(kind='bar', stacked=True, figsize=(8,6), colormap='Set2',color=['skyblue', 'lightgreen'])

# Step 4: Add percentage labels
for i, row in enumerate(ct_percent.values):
    cumulative = 0
    for j, val in enumerate(row):
        if val > 0:
            ax.text(i, cumulative + val / 2, f'{val:.1f}%', ha='center', va='center', fontsize=10)
            cumulative += val

# Step 5: Customize plot
plt.title("Senior Citizens by Churn Status (Stacked %)")
plt.xlabel("Senior Citizen (0 = No, 1 = Yes)")
plt.ylabel("Percentage")
plt.legend(title="Churn")
plt.tight_layout()
plt.show()


#Printing Histograms of Tenure

sb.histplot(x="tenure",data=data,hue="Churn")
plt.show()

#Printing Bar chart of Contract by Churn Status
sb.countplot(x="Contract",data=data,hue="Churn")
plt.title("Contract by Churn Status")
plt.show()

print(data.columns.values)

cols = ['PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
        'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']

# Set up a 3x3 grid of subplots
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(18, 12))
axes = axes.flatten()

# Plot each countplot
for i, col in enumerate(cols):
    sb.countplot(data=data, x=col, ax=axes[i], palette='Set2',hue='Churn')
    axes[i].set_title(col, fontsize=12)
    axes[i].set_xlabel("")  # Remove x-axis label
    axes[i].set_ylabel("Count")

# Remove any unused subplot axes (if any)
for j in range(len(cols), len(axes)):
    fig.delaxes(axes[j])

# Adjust layout to prevent overlap
plt.tight_layout()
plt.suptitle("Service Feature Distributions", fontsize=16, y=1.03)
plt.show()

#The dataset explores customer churn behavior across various telecom services such as PhoneService, InternetService, and StreamingTV. Each subplot shows a countplot comparing churned vs non-churned customers for a specific service. Notably, services like OnlineSecurity and TechSupport show a higher churn rate among customers who did not subscribe. This visualization helps identify which services are most associated with customer retention or loss.
sb.countplot(x="PaymentMethod",data=data,hue="Churn")
plt.title("PaymentMethod by Churn Status")
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()
