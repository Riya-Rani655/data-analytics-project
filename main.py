
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DATASET_PATH = 'Advertising.csv'

def run_analysis():
    print("--- Starting Data Analytics Pipeline ---")
    
    # 1. Load Data
    try:
        df = pd.read_csv(DATASET_PATH)
        print(f"Successfully loaded '{DATASET_PATH}'\n")
    except FileNotFoundError:
        print(f"Error: '{DATASET_PATH}' not found in project folder!")
        return

    # Clean index column if present
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])

    # 2. Dataset Overview
    print("=== First 5 Rows ===")
    print(df.head())
    
    print("\n=== Dataset Summary Stats ===")
    print(df.describe())
    
    print("\n=== Missing Values ===")
    print(df.isnull().sum())

    # 3. Save Correlation Heatmap
    plt.figure(figsize=(8, 5))
    sns.heatmap(df.corr(), annot=True, cmap='Blues', fmt=".2f")
    plt.title('Advertising Spend vs. Sales Correlation Heatmap')
    plt.tight_layout()
    plt.savefig('correlation_heatmap.png')
    
    print("\nVisualization successfully saved as 'correlation_heatmap.png'")
    print("--- Pipeline Execution Complete ---")

if __name__ == '__main__':
    run_analysis()