import datetime
import random
import time

def log_message(level, message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{level}] {message}"
    print(log_entry)
    with open("trading_engine.log", "a") as f:
        f.write(log_entry + "\n")

def process_trade():
    orders = [
        {"id": "ORD-1001", "symbol": "VTS", "qty": 50, "type": "BUY"},
        {"id": "ORD-1002", "symbol": "VAS", "qty": 120, "type": "SELL"},
        {"id": "ORD-1003", "symbol": "VGS", "qty": 200, "type": "BUY"},
    ]

    for order in orders:
        log_message("INFO", f"Processing Order {order['id']}: {order['type']} {order['qty']} units of {order['symbol']}")
        
        if order["id"] == "ORD-1002":
            log_message("ERROR", f"CRITICAL: Database connection pool exhausted while settling {order['id']}. Transaction failed.")
        else:
            log_message("INFO", f"SUCCESS: Order {order['id']} executed and settled successfully.")
        
        time.sleep(1)

if __name__ == "__main__":
    log_message("INFO", "Trading Engine Daemon Started.")
    process_trade()
    log_message("INFO", "Trading Engine Cycle Completed.")
