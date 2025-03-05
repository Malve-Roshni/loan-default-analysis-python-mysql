from sqlalchemy import create_engine
import mysql.connector

# MySQL Configuration
db_config = {
    "host": "localhost",
    "user": "Roshni",  # Change if needed
    "password": "Hello123",  # Change if needed
    "database": "loan_analysis"  # Change if your database name is different
}

def create_connection():
    """Create an SQLAlchemy engine for MySQL connection."""
    try:
        engine = create_engine(f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}")
        print("✅ Successfully connected to MySQL")
        return engine
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

# Test the connection when running this script directly
if __name__ == "__main__":
    create_connection()
