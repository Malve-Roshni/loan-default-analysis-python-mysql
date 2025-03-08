# Loan Default Analysis using Python & MySQL

## 📌 Project Overview
This project analyzes loan default data using **Python** and **MySQL** to identify patterns in loan approvals and defaults. The dataset includes details such as **credit scores, income levels, loan amounts, and interest rates**.

Using **MySQL for data storage** and **Python (Pandas, Seaborn, Matplotlib) for analysis**, this project provides insights into how financial factors influence loan approvals.

---

## 📂 Project Structure
```
Loan_Default_Analysis_Python_MySQL/
│── config.py           # Connects Python to MySQL
│── load_data.py        # Loads data from MySQL into Pandas
│── loan_analysis.py    # Cleans, analyzes, and visualizes data
│── run_queries.py      # Runs SQL queries on MySQL database
│── requirements.txt    # Lists required Python libraries
│── README.md           # Project documentation
│
├── Dataset/
│   ├── loan_default.csv    # Loan dataset
│
├── Output/                 # Stores visualization outputs
│
├── SQL_scripts/
│   ├── create_table.sql    # SQL script for creating tables
```

---

## ⚙️ Setup & Installation

### **1️⃣ Install Dependencies**
Ensure you have **Python, MySQL, and VS Code** installed.
Run the following command to install required Python libraries:
```sh
pip install -r requirements.txt
```

### **2️⃣ Set Up MySQL Database**
- Install MySQL and MySQL Shell.
- Open MySQL Shell and create a database:
  ```sql
  CREATE DATABASE loan_analysis;
  ```
- Run the SQL script to create tables:
  ```sh
  mysql -u root -p < SQL_scripts/create_table.sql
  ```

### **3️⃣ Update MySQL Credentials**
Modify **config.py** to include your MySQL **username, password, host, and database name** before running queries.

### **4️⃣ Load Data into MySQL**
Run the script to insert the dataset into MySQL:
```sh
python load_data.py
```

### **5️⃣ Run Data Analysis**
Execute the analysis script to clean, analyze, and visualize loan data:
```sh
python loan_analysis.py
```
✅ The generated **visualizations** will be saved in the `Output/` folder.

### **6️⃣ (Optional) Execute SQL Queries**
Run specific SQL queries on the database using:
```sh
python run_queries.py
```

---

## 🔍 Key Insights from Analysis
This project provides insights into loan approvals based on financial factors:

- **📊 Credit Score Trends:** How credit scores impact loan approvals.
- **✅ Loan Approval Rates:** Approval vs. rejection trends.
- **💰 Income & Loan Amount Impact:** How income and loan amount affect approvals.

---

## 🛠️ Technologies Used
- **Python**: Pandas, Seaborn, Matplotlib, SQLAlchemy
- **MySQL**: Data storage & SQL queries
- **VS Code**: Development environment
- **GitHub**: Version control

---

## 🚀 Usage Instructions

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/Malve-Roshni/loan-default-analysis-python-mysql.git
cd Loan_Default_Analysis_Python_MySQL
```

### **2️⃣ Install Required Libraries**
```sh
pip install -r requirements.txt
```

### **3️⃣ Set Up MySQL Database**
- Open MySQL Shell and create a database:
  ```sql
  CREATE DATABASE loan_analysis;
  ```
- Run the SQL script to create tables:
  
  mysql -u root -p < SQL_scripts/create_table.sql
  

### **4️⃣ Update MySQL Credentials**
Modify **config.py** with your MySQL **username, password, host, and database name** to enable database connection.

### **5️⃣ Load Data into MySQL**
```sh
python load_data.py


### **6️⃣ Run Data Analysis**
```sh
python loan_analysis.py
```
✅ Graphs and insights will be saved in the `Output/` folder.

### **7️⃣ Check SQL Query Results**
Run queries directly in MySQL:
```sql
SELECT * FROM loan_table;
```

---

## 📄 About
**Loan Default Analysis using Python & MySQL**: A comprehensive data pipeline for querying, cleaning, analyzing, and visualizing loan data. Includes **SQL queries, Python scripts, and detailed reports**.

🔗 **GitHub Repository:** [Loan Default Analysis](https://github.com/Malve-Roshni/loan-default-analysis-python-mysql)

---