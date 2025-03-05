Loan Default Analysis using Python & MySQL

------Project Overview-----

This project analyzes loan default data using Python and MySQL. The goal is to clean, analyze, and visualize the data to understand loan approval trends based on factors like credit score, income, loan amount, and interest rate.

By leveraging MySQL for data storage and Python (Pandas, Seaborn, Matplotlib) for analysis, this project provides insights into loan approval patterns.

------Project Structure-----
Loan_Default_Analysis_Python_MySQL/
│── config.py              # Connects Python to MySQL  
│── load_data.py           # Loads data from MySQL into Pandas  
│── loan_analysis.py       # Cleans, analyzes, and visualizes data  
│── run_queries.py         # Runs SQL queries on MySQL database  
│── requirements.txt       # Lists required Python libraries  
│── README.md              # Project documentation  
│  
├── Dataset/  
│   ├── loan_default.csv   # Loan dataset  
│  
├── Output/                # Stores visualization outputs  
│  
├── SQL_scripts/  
│   ├── create_table.sql   # SQL script for creating tables 

------Setup & Installation for Project------
1. Installed MySQL and MySQL Shell
2. Installed Python and VS Code
3. Installed Required Python Libraries

Run the following command to install dependencies:

pip install -r requirements.txt
4. Updated MySQL Credentials
Modifyed config.py to include MySQL database credentials before running queries.
5. Run the Scripts
python load_data.py        # Loads data into Pandas  
python loan_analysis.py    # Analyzes and visualizes the data  
The generated visualizations will be saved in the Output/ folder.

------Key Insights from Analysis-------
This project provides insights into loan approvals based on financial factors:

Credit Score Trends 📊: Visualizes how credit scores impact loan approvals.
Loan Approval Rates ✅: Shows approval vs. rejection rates.
Income & Loan Amount Impact 💰: Analyzes how income and loan amount affect approvals.

-----Technologies Used-----
Python: Pandas, Seaborn, Matplotlib, SQLAlchemy
MySQL: Data storage & queries
VS Code: Development environment
GitHub: Version control

------Usage Instructions-----

1. Clone the Repository
First, download the project from GitHub:
git clone <repo_url>
cd Loan_Default_Analysis_Python_MySQL

2. Install Required Libraries
Install all necessary Python libraries from requirements.txt:
pip install -r requirements.txt

3. Set Up MySQL Database
Open MySQL Shell and create a new database.
Run the SQL script to create the required tables:
mysql -u root -p < SQL_scripts/create_table.sql

4. Update MySQL Credentials
Modify config.py with your MySQL username, password, host, and database name to enable database connection.

5. Load Data into MySQL
Run the script to insert the dataset into the MySQL database:
python load_data.py

6. Run Data Analysis
Execute the analysis script to clean, analyze, and visualize loan data:
python loan_analysis.py
The visualizations will be stored in the Output/ folder.

7. Execute SQL Queries (Optional)
You can run specific SQL queries on the database using:
python run_queries.py

8. Check Results
Analysis outputs (graphs and insights) will be available in the Output/ folder.
Database tables can be checked directly in MySQL using:
SELECT * FROM loan_table;