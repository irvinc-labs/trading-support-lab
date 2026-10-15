# Trading Support Lab (`trading-support-lab`)

An enterprise-grade, ITIL-aligned production support lab simulating order ingestion, log forensics, real-time monitoring, and transaction reconciliation in a Linux/WSL environment.

---

## 🛠️ Key Support Automation & Tools

### 1. Order Ingestion & Trace Logging (`app/order_engine.py`)
* Simulates multi-account trade ingestion with structured event logs.
* Injects **Trace IDs / Correlation IDs** (`TraceID: TRACE-XXXXX`) into telemetry for end-to-end transaction tracking.

### 2. Automated Health Sentinel (`scripts/monitor_engine.sh`)
* Real-time Bash monitoring tool that parses error rates in `trading_engine.log`.
* Evaluates threshold violations (`THRESHOLD=3`) to automatically trigger L2 incident escalation.

### 3. Dead Letter Queue (DLQ) Quarantine (`scripts/reconcile_dlq.py`)
* Isolates corrupted or malformed trade payloads into `dlq_quarantine.json`.
* Prevents engine pipeline halting while preserving failed trades for operational replay.

---

## 📄 ITIL Operational Artifacts
* **Incident Management:** [`incidents/INC-4092-P1-Outage.md`](incidents/INC-4092-P1-Outage.md)
* **Standard Operating Procedure:** [`runbooks/RB-01-Stuck-Orders.md`](runbooks/RB-01-Stuck-Orders.md)

---

## 🚀 Quick Start & Forensic Commands

```bash
# 1. Run simulation engine
python3 app/order_engine.py

# 2. Check engine health status
./scripts/monitor_engine.sh

# 3. Quarantine failed records to DLQ
python3 scripts/reconcile_dlq.py
```
