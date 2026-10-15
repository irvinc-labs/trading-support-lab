import os

LOG_FILE = "trading_engine.log"
DLQ_FILE = "dlq_quarantine.json"

print("Scanning log file for corrupted payload records...")

failed_orders = []

if os.path.exists(LOG_FILE):
    with open(LOG_FILE, "r") as log:
        for line in log:
            if "ERROR" in line and "TraceID" in line:
                failed_orders.append(line.strip())

    with open(DLQ_FILE, "w") as dlq:
        for err in failed_orders:
            dlq.write(err + "\n")

    print(f"Quarantined {len(failed_orders)} corrupted record(s) into {DLQ_FILE}.")
else:
    print("Log file not found.")
