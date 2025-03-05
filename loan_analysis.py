import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from config import create_connection  # Import MySQL connection function

def load_data():
    """Fetch data from MySQL and load into Pandas DataFrame."""
    engine = create_connection()
    if engine:
        query = "SELECT * FROM loan_data;"  
        df = pd.read_sql(query, engine)
        print("✅ Data successfully loaded into Pandas DataFrame")
        return df
    else:
        print("❌ Failed to load data")
        return None

def clean_data(df):
    """Check for missing values, duplicates, and fix data types."""
    print("\n🔍 Checking for missing values:")
    print(df.isnull().sum())  

    # ✅ Fill missing numerical values with median
    df.fillna(df.median(numeric_only=True), inplace=True)

    # ✅ Drop duplicate rows if any
    df.drop_duplicates(inplace=True)

    # ✅ Ensure categorical columns are treated correctly
    categorical_cols = ["Education", "EmploymentStatus", "MaritalStatus", "HomeOwnership", "Purpose", "LoanStatus"]
    for col in categorical_cols:
        df[col] = df[col].astype(str)  

    print("\n✅ Data cleaned successfully!")
    return df

def save_graphs_to_pdf(df):
    """Generate all loan analysis visualizations and save them to a single PDF."""
    pdf_path = "Output/loan_analysis_report.pdf"  
    with PdfPages(pdf_path) as pdf:
        sns.set_style("whitegrid")  

        # ✅ 1. Credit Score Distribution
        plt.figure(figsize=(8, 5))
        sns.histplot(df["CreditScore"], bins=30, kde=True, color="#1f77b4")
        plt.title("Credit Score Distribution")
        plt.xlabel("Credit Score")
        plt.ylabel("Frequency")
        pdf.savefig()  # Save the figure
        plt.close()

        # ✅ 2. Loan Approval Distribution (Fixed Warning)
        plt.figure(figsize=(6, 4))
        sns.countplot(data=df, x="LoanStatus", hue="LoanStatus", palette={"Rejected": "#d62728", "Approved": "#2ca02c"}, legend=False)
        plt.title("Loan Approval vs. Rejection")
        plt.xlabel("Loan Status")
        plt.ylabel("Count")
        pdf.savefig()
        plt.close()

        # ✅ 3. Credit Score vs Loan Approval (Fixed Warning)
        plt.figure(figsize=(8, 5))
        sns.boxplot(data=df, x="LoanStatus", y="CreditScore", hue="LoanStatus", palette={"Rejected": "#ff7f0e", "Approved": "#9467bd"}, legend=False)
        plt.title("Credit Score vs Loan Approval")
        plt.xlabel("Loan Status")
        plt.ylabel("Credit Score")
        pdf.savefig()
        plt.close()

        # ✅ 4. Income vs Loan Approval (Fixed Warning)
        plt.figure(figsize=(8, 5))
        sns.boxplot(data=df, x="LoanStatus", y="Income", hue="LoanStatus", palette={"Rejected": "#e377c2", "Approved": "#17becf"}, legend=False)
        plt.title("Income vs Loan Approval")
        plt.xlabel("Loan Status")
        plt.ylabel("Income")
        pdf.savefig()
        plt.close()

        # ✅ 5. Loan Amount vs Interest Rate
        plt.figure(figsize=(8, 5))
        sns.scatterplot(x=df["LoanAmount"], y=df["InterestRate"], hue=df["LoanStatus"], palette="coolwarm", alpha=0.6)
        plt.title("Loan Amount vs Interest Rate")
        plt.xlabel("Loan Amount")
        plt.ylabel("Interest Rate")
        pdf.savefig()
        plt.close()

    print(f"📄 Report saved successfully: {pdf_path}")

# ✅ Main Execution
if __name__ == "__main__":
    df = load_data()
    if df is not None:
        print(df.head())  
        df = clean_data(df)  
        save_graphs_to_pdf(df)
