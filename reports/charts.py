import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('reports/csv_files/file_summary.csv')
df = df[["FileType","FileName", "Type"]].copy()


# Calculate percentages of each file type
file_type_counts = df['FileType'].value_counts()
file_type_labels = file_type_counts.index
file_type_sizes = file_type_counts.values

# Create pie chart
def type_percent_chart():
    plt.figure(figsize=(8, 8))
    plt.pie(file_type_sizes, labels=file_type_labels, autopct='%1.1f%%', startangle=140)
    plt.title("Percentage of File Types Analyzed")
    plt.show()


# Set up the figure and subplots
def data_percent_chart():
    num_file_types = len(file_type_labels) + 1  # One for "Percentage of File Types"
    fig, axes = plt.subplots(1, num_file_types, figsize=(16, 8), subplot_kw={'aspect': 'equal'})
    fig.suptitle("Data Breakdown", fontsize=16)

    # Pie chart for file type percentages
    axes[0].pie(file_type_sizes, labels=file_type_labels, autopct='%1.1f%%', startangle=140)
    axes[0].set_title("Percentage of File Types")

    # Pie charts for each file type's data breakdown
    file_type = df["FileType"].unique()
    for i, type in enumerate(file_type):
        filtered_df = df[df['FileType'] == type]
        type_counts = filtered_df['Type'].value_counts()
        type_labels = type_counts.index
        type_sizes = type_counts.values

        axes[i + 1].pie(type_sizes, labels=type_labels, autopct='%1.1f%%', startangle=140)
        axes[i + 1].set_title(f"Data Breakdown for {type} Files")

    # Adjust layout and display
    plt.tight_layout()
    plt.subplots_adjust(top=0.85)  # Add space for the main title
    plt.show()   


def data_chart():
    # Aggregate counts of 'Type' by 'FileName'
    type_counts = df.groupby(["FileName", "Type"]).size().unstack(fill_value=0)

    # Plotting the data
    ax = type_counts.plot(kind="bar", stacked=False, figsize=(10, 6))

    # Customize the chart
    plt.title("Distribution of Types Across Files", fontsize=14)
    plt.xlabel("File Names", fontsize=12)
    plt.ylabel("Count", fontsize=12)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.legend(title="Type", fontsize=10)
    plt.tight_layout()

    # Show the plot
    plt.show()
