import sqlite3

# Connect to SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('token_usage.db')
cursor = conn.cursor()

# Create table for user balances
cursor.execute('''CREATE TABLE IF NOT EXISTS user_balances
               (user_id INTEGER PRIMARY KEY, balance REAL)''')

# Create table for transactions (optional, for detailed tracking)
cursor.execute('''CREATE TABLE IF NOT EXISTS transactions
               (transaction_id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, tokens_used INTEGER, cost REAL, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')

conn.commit()


def add_new_user(user_id):
    """Add a new user with an initial balance of $1.00 if they don't exist."""
    if get_balance(user_id) is None:  # Check if the user already exists
        cursor.execute("INSERT INTO user_balances (user_id, balance) VALUES (?, 1.00)", (user_id,))
        conn.commit()


def update_balance(user_id, cost):
    """Update the user's balance after each interaction."""
    cursor.execute("UPDATE user_balances SET balance = balance - ? WHERE user_id = ?", (cost, user_id))
    conn.commit()


def log_transaction(user_id, tokens_used, cost):
    """Log a transaction in the database (optional)."""
    cursor.execute("INSERT INTO transactions (user_id, tokens_used, cost) VALUES (?, ?, ?)", (user_id, tokens_used, cost))
    conn.commit()

def calculate_cost(tokens_used):
    """Calculate the cost based on the number of tokens used."""
    return (tokens_used / 1000000) * 0.6  # $0.60 per 1M output tokens  

def get_balance(user_id):
    """Retrieve the current balance for a user. Returns None if user does not exist."""
    cursor.execute("SELECT balance FROM user_balances WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    return result[0] if result else None


