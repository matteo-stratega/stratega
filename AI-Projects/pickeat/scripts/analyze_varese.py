#!/usr/bin/env python3
"""
Varese Performance Analytics
Quick analysis of game-by-game performance

Usage:
    python3 scripts/analyze_varese.py [csv_path]

If no CSV provided, looks for data in clients/varese/data/
"""

import sys
import csv
from pathlib import Path
from datetime import datetime

def load_csv(path):
    """Load CSV and return list of dicts"""
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def analyze_orders(data):
    """Basic order analysis"""
    if not data:
        print("No data to analyze")
        return

    total_orders = len(data)

    # Try to find revenue/amount column
    amount_col = None
    for col in ['amount', 'total', 'revenue', 'price', 'value']:
        if col in data[0]:
            amount_col = col
            break

    if amount_col:
        revenues = [float(row[amount_col].replace('€', '').replace(',', '.'))
                   for row in data if row.get(amount_col)]
        total_revenue = sum(revenues)
        avg_order = total_revenue / len(revenues) if revenues else 0

        print(f"📊 VARESE PERFORMANCE SUMMARY")
        print(f"=" * 40)
        print(f"Total Orders: {total_orders}")
        print(f"Total Revenue: €{total_revenue:.2f}")
        print(f"Average Order Value: €{avg_order:.2f}")
        print(f"=" * 40)
    else:
        print(f"📊 VARESE ORDERS")
        print(f"=" * 40)
        print(f"Total Orders: {total_orders}")
        print(f"(No revenue column found)")
        print(f"=" * 40)

def main():
    # Find data file
    if len(sys.argv) > 1:
        csv_path = Path(sys.argv[1])
    else:
        # Look for data in default location
        base = Path(__file__).parent.parent
        data_dir = base / 'clients' / 'varese' / 'data'

        if data_dir.exists():
            csvs = list(data_dir.glob('*.csv'))
            if csvs:
                csv_path = csvs[0]
                print(f"Using: {csv_path}")
            else:
                print(f"No CSV files found in {data_dir}")
                return
        else:
            print("No data directory found. Provide CSV path as argument.")
            return

    if not csv_path.exists():
        print(f"File not found: {csv_path}")
        return

    data = load_csv(csv_path)
    analyze_orders(data)

if __name__ == '__main__':
    main()
