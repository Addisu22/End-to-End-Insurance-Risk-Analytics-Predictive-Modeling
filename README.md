Insurance Risk & Premium Modeling - Week 3 Challenge
====================================================

Overview
=======
This initiative is part of the Week 3 challenge, which aims to analyze insurance claims data to derive insights, evaluate risk factors, and develop predictive models for a flexible, risk-based pricing system. The project encompasses a range of activities, including data exploration, statistical testing, and machine learning modeling, all while adhering to best practices in version control, continuous integration and delivery (CI/CD), and thorough documentation.

Table of Contents

1. Project Structure

2. Installation & Setup

3. Task Breakdown

        Task 1 - EDA & GitHub

        Task 2 - Data Versioning with DVC

        Task 3 - Statistical Hypothesis Testing

        Task 4 - Predictive Modeling

4. Key Insights & Recommendations

5. Usage

6. Contributing

7. License

Project Structure
=================
insurance-risk-analysis/
├── data/                  # Raw and processed datasets
├── eda/                   # EDA scripts and plots
├── dvc/                   # DVC config and tracked data
├── stats_tests/           # Hypothesis testing scripts
├── models/                # ML training and evaluation code
├── plots/                 # All visualizations
├── .github/workflows/     # CI/CD via GitHub Actions
├── .dvc/                  # DVC metadata
├── README.md
├── requirements.txt
├── .gitignore


Installation and Setup
# Clone the repository
https://github.com/ATTTT2000/insurance-risk-analysis.git
cd insurance-risk-analysis

# Install dependencies
pip install -r requirements.txt

# Initialize DVC and configure local remote
dvc init
dvc remote add -d localstorage ./dvc-storage

# Track data
dvc add data/insurance_data.csv
dvc push

Task Breadkdown
===============
Task 1 - EDA & GitHub

    Created repo with proper branching strategy: task-1

    Used GitHub Actions for CI on push and PR

    Performed EDA:

        Descriptive stats, missing value checks

        Visualized distributions and correlations

        Explored Loss Ratios by Province, Gender, and VehicleType

        Identified outliers and temporal trends

Key Visualizations

    claim_by_province.png: Avg claim amount across provinces

    correlation_matrix.png: Correlation of numeric fields

    premium_vs_claim_zipcode.png: Scatter plot of premium vs. claims by ZipCode

Task 2 - Data Versioning with DVC

    Installed and initialized DVC

    Set up local remote and tracked data

    Created reproducible data pipeline with dvc.yaml

    Branch used: task-2

Task 3 - Statistical Hypothesis Testing

    Defined and tested hypotheses using t-tests and chi-squared tests

    Segmented data for A/B tests (e.g., Male vs Female, Gauteng vs WC)

    Branch used: task-3

Example Insight

    Rejected H₀: No risk differences across provinces (p < 0.01)

            Gauteng has a 15% higher loss ratio than Western Cape

            Business recommendation: regional premium adjustment

Task 4 - Predictive Modeling

    Models: Linear Regression, Random Forest, XGBoost

    Preprocessed and encoded data

    Evaluated on RMSE and R-squared

    Used SHAP for model interpretability

    Branch used: task-4

Example SHAP Insight

    For every year older a vehicle is, the predicted claim amount increases by R1,200. Suggests refinement of age-based premium pricing.


Key Insights & Recommendations
==============================

High Claim Risk in Gauteng: Justifies risk loading in premiums

Older Vehicles Have Higher Claims: Time-based depreciation factor in pricing

Males had slightly higher severity of claims: Validate further before adjusting pricing

Seasonal Trends: End-of-year claim spikes; suggest premium buffers


Usage
=====

# Run EDA
python eda/eda_analysis.py

# Run Hypothesis Tests
python stats_tests/hypothesis_testing.py

# Train Models
python models/train_models.py


Contributing
============

Fork the repo

Create your branch: git checkout -b feature/your-feature

Commit changes: git commit -m 'Add your feature'

Push to branch: git push origin feature/your-feature

Open a pull request


License
=======
This project is licensed under the MIT License.