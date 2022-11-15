# Import Necessary Python Modules
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.ticker as mtick

# Load kiva_data.csv and inspect
df = pd.read_csv("kiva_data.csv")
df.head()

# Examine the data
print(df.head(25))

# Bar charts
f, ax = plt.subplots(figsize=(15, 10)) # Create the figure
sns.barplot(data=df, x="country", y="loan_amount") # Plot the data
fmt = '${x:,.0f}' # Adding "$" units
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)

# Learn More By Using hue In Your Visualization
f, ax = plt.subplots(figsize=(15, 10)) # Creates the figure, you're only using this syntax so you can modify the y-axis ticks below
sns.barplot(data=df, x="country", y="loan_amount", hue="gender")

fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)

# Styling
sns.set_palette("Pastel2") # Set color palette
sns.set_style("darkgrid") # Set style
sns.set_context("paper", font_scale=1.8) # Set style
plt.figure(figsize=(25, 15)) # Create figure and axes
ax.set_title("Kiva loan per gender to different countries")
sns.barplot(data=df, x="country", y="loan_amount", hue="gender") # Use Seaborn to create the bar plot

# Box Plots With Kiva Data
plt.figure(figsize=(16, 10))
sns.set_palette("Pastel1")
sns.boxplot(data=df, x="country", y="loan_amount", hue="gender")

# Box Plot by Activity
plt.figure(figsize=(16, 10))
sns.set_palette("Accent")
sns.boxplot(data=df, x="activity", y="loan_amount", hue="gender")

# Violin Plots
plt.figure(figsize=(16, 10))
sns.violinplot(data=df, x="activity", y="loan_amount", hue="gender")