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
personal-budget-tracker/
├── alembic.ini
├── cli.py
├── config/
│   └── setup.py
├── db/
│   └── store.db
├── lib/
│   ├── models.py  
├── helpers.py
├── migrations/
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions/
│       └── [migration files].py
├── seed.py
├── Pipfile
├── Pipfile.lock
├── README.md
└── debug.py


## Models & Relationships

- **User**
  - Has many `Transaction`s
- **Category**
  - Has many `Transaction`s
- **Transaction**
  - Belongs to one `User`
  - Belongs to one `Category`

GitHub link here:[https://github.com/jedaqsaul/Personal-Budget-Tracker]


