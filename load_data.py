import pandas as pd
import mysql.connector
from config import db_config

# ✅ Load dataset
file_path = "Dataset/loan_default.csv"
column_names = ["LoanID", "Age", "Income", "LoanAmount", "CreditScore",
                "MonthsEmployed", "NumCreditLines", "InterestRate",
                "DebtToIncomeRatio", "Education", "EmploymentStatus",
                "MaritalStatus", "HomeOwnership", "HasBankruptcies",
                "Purpose", "PreviousDefaults", "OtherLoans", "LoanStatus"]

df = pd.read_csv(file_path, names=column_names, header=None, skiprows=1, dtype=str)  # ✅ Read all as string first

# ✅ Convert categorical values properly
df["HasBankruptcies"] = df["HasBankruptcies"].map({"Yes": 1, "No": 0})
df["PreviousDefaults"] = df["PreviousDefaults"].map({"Yes": 1, "No": 0})
df["OtherLoans"] = df["OtherLoans"].map({"Yes": 1, "No": 0})

# ✅ Ensure LoanStatus matches ENUM values correctly
df["LoanStatus"] = df["LoanStatus"].map({"0": "Rejected", "1": "Approved"})

# ✅ Fill NaN values before proceeding
df.fillna({"PreviousDefaults": 0, "LoanStatus": "Rejected"}, inplace=True)  # Set reasonable defaults

# ✅ Remove duplicate LoanIDs to prevent MySQL primary key error
df.drop_duplicates(subset=["LoanID"], keep="first", inplace=True)

# ✅ Debugging: Check unique values
print("Unique LoanStatus values:", df["LoanStatus"].unique())
print("Unique PreviousDefaults values:", df["PreviousDefaults"].unique())

# ✅ Connect to MySQL and insert data
try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    print("✅ Connected to MySQL database successfully!")

    # ✅ Clear the existing table to avoid duplicate errors
    cursor.execute("DELETE FROM loan_data")

    sql = """INSERT INTO loan_data (LoanID, Age, Income, LoanAmount, CreditScore, MonthsEmployed,
            NumCreditLines, InterestRate, DebtToIncomeRatio, Education, EmploymentStatus, MaritalStatus,
            HomeOwnership, HasBankruptcies, Purpose, PreviousDefaults, OtherLoans, LoanStatus) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    values = [tuple(row) for _, row in df.iterrows()]
    cursor.executemany(sql, values)  # Batch insert

    conn.commit()
    print(f"✅ {cursor.rowcount} rows successfully inserted into MySQL!")

except mysql.connector.Error as err:
    print(f"❌ Error: {err}")

finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'conn' in locals() and conn:
        conn.close()
