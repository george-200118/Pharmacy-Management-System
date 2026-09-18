# Pharmacy Management System

A desktop pharmacy inventory and sales management application built with **Python Tkinter** and **SQLite**.

## Features

- Add new medicines with company, usage, type, lot number, dates, price, and quantity
- Sell medicines and automatically update stock levels
- View and search all medicines
- Track total quantity by medicine name
- View expired medicines
- View missing/out-of-stock medicines
- Update medicine prices
- Delete medicines
- Export medicine records to Excel (`.xlsx`)

## Tech Stack

- Python 3
- Tkinter (GUI)
- SQLite (`sqlite3`)
- Pillow (`PIL`)
- tkcalendar
- openpyxl

## Project Structure

- `main.py` - Main application and all screens
- `pharmacy.db` - SQLite database file
- `pharmacy.jpg`, `medicine.jpg`, `back.png` - UI image assets
- `draft.py` - Experimental/demo script (not part of main app flow)

## Setup

1. Clone the repository.
2. Install dependencies:

```bash
pip install pillow tkcalendar openpyxl
```

## Run

From the repository root:

```bash
python main.py
```

## Database

On startup, the app ensures these tables exist:

- `Medicine`
- `Medicine_Names`

## Notes

- The application is designed for desktop use.
- The window opens in maximized mode.
