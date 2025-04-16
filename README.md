# Python Analysis Project

## Project Overview

This project is designed to analyse housing data in London. It includes data processing, analysis, and visualisation to extract meaningful insights from the dataset provided.

## Project Structure

```plaintext
python-analysis-project/
├── analysis.py                # Main script for data analysis
├── Python Analysis Project.pdf # Project documentation (if applicable)
├── README.md                  # Project overview and instructions
├── requirements.txt           # File listing project dependencies
├── data/                      # Directory containing data files
│   ├── houses-in-london.zip   # Compressed dataset
│   └── london_houses.csv      # CSV file with housing data
```

## Prerequisites

- Python 3.8 or higher
- Recommended: A virtual environment to manage dependencies

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd python-analysis-project
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Unzip the dataset (if not already unzipped):

   ```bash
   unzip data/houses-in-london.zip -d data/
   ```

## Usage

Run the analysis script:

```bash
python analysis.py
```

Choose the CLI option for the metric you want to analyse. A corresponding visualisation will be generated and displayed.

## CLI Options

When you run the script, you will be presented with the following options in the CLI:

1. **Show Price Distribution**: Displays a histogram of house prices in London.
2. **Show Average Price by Neighborhood**: Displays a bar plot of average house prices by neighborhood.
3. **Show Price vs Square Meters**: Displays a scatter plot showing the relationship between property size and price.
4. **Show Correlation Heatmap**: Displays a heatmap of correlations between numerical features in the dataset.
5. **Exit**: Exits the CLI application.

## Data

The dataset (`london_houses.csv`) contains information about housing in London. Ensure the data is properly formatted and located in the `data/` directory.

## Credits

The dataset used in this project is sourced from Kaggle: [Houses in London](https://www.kaggle.com/datasets/oktayrdeki/houses-in-london/data?select=london_houses.csv).
