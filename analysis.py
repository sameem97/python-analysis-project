import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# === Setup ===
# Load data
df = pd.read_csv('data/london_houses.csv')

# Clean + Prepare
df.drop_duplicates(inplace=True)
df.rename(columns={"Price (£)": "Price"}, inplace=True)

if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

df['Garden'] = df['Garden'].map({'Yes': 1, 'No': 0})
df['Balcony'] = df['Balcony'].map({'Balcony': 1, 'No Balcony': 0})

# === Analysis Functions ===
def price_distribution():
    """This histogram shows the distribution of house prices in London."""
    plt.figure(figsize=(10, 5))
    sns.histplot(df['Price'], bins=30, kde=True)
    plt.title("House Price Distribution in London")
    plt.xlabel("Price (£)")
    plt.ylabel("Number of Houses")
    plt.show()

def average_price_by_neighborhood():
    """This bar plot shows the average price of houses in different neighborhoods."""
    plt.figure(figsize=(14, 6))
    sns.barplot(data=df, x='Neighborhood', y='Price', estimator=np.mean)
    plt.xticks(rotation=90)
    plt.title("Average Price by Neighborhood")
    plt.tight_layout()
    plt.show()

def price_vs_size():
    """This scatter plot shows the relationship between the size of the property and its price."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Square Meters', y='Price', hue='Neighborhood', alpha=0.7)
    plt.title("Price vs. Size of Property")
    plt.tight_layout()
    plt.show()

def correlation_heatmap():
    """This heatmap shows the correlation between numerical features in the dataset."""
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
    plt.title("Correlation Between Numerical Features")
    plt.tight_layout()
    plt.show()

# === CLI Menu ===
def main_menu():
    """Main menu for the CLI application."""
    print("Welcome to the London Housing Analysis CLI!")
    while True:
        print("\n🏡 London Housing Analysis Menu")
        print("1. Show Price Distribution")
        print("2. Show Average Price by Neighborhood")
        print("3. Show Price vs Square Meters")
        print("4. Show Correlation Heatmap")
        print("5. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            price_distribution()
        elif choice == '2':
            average_price_by_neighborhood()
        elif choice == '3':
            price_vs_size()
        elif choice == '4':
            correlation_heatmap()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("❌ Invalid input. Please enter a number between 1 and 5.")

# === Run ===
if __name__ == "__main__":
    main_menu()
