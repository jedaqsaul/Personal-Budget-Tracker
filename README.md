# Personal Budget Tracker

A terminal-based personal budgeting tool that allows users to track expenses by category, view summaries, and manage their monthly budget.

## Features

- Add, update, and delete users
- Add categories (e.g., Food, Transport, Rent)
- Record transactions for specific users and categories
- View total spending, remaining budget, and summary by category
- Interactive CLI interface

## Technologies Used

- Python 3
- SQLAlchemy ORM
- Alembic (for database migrations)
- SQLite (for local database)

## Project Structure

├── cli.py # Main entry point for the interactive CLI
├── config/
│ └── setup.py # Configures and connects to the database
├── db/
│ └── store.db # SQLite database file
├── lib/
│ ├── models.py # SQLAlchemy models for User, Category, Transaction
├── seed.py # Script to seed initial data (e.g., default categories)
├── helpers.py # Helper functions for user, category, and transaction logic
├── debug.py # Optional debug script for testing functions
├── migrations/ # Alembic migration files
├── alembic.ini # Alembic configuration
├── README.md # Project documentation


## Models & Relationships

- **User**
  - Has many `Transaction`s
- **Category**
  - Has many `Transaction`s
- **Transaction**
  - Belongs to one `User`
  - Belongs to one `Category`

GitHub link here:[https://github.com/jedaqsaul/Personal-Budget-Tracker]


