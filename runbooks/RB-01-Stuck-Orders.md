# Operational Runbook: RB-01-Stuck-Orders

## Metadata
* **Runbook ID:** RB-01
* **Title:** Diagnostic and Remediation Procedure for Stuck or Delayed Orders
* **Target Audience:** L1 / L2 Production Support Analysts
* **System:** Trading Order Ingestion & Settlement Engine (`TRD-ENG-PROD-01`)
* **Severity Threshold:** P2 / P1 (If order backlog exceeds 500 records)

## 1. Initial Assessment & Trigger
This runbook applies when automated monitoring alerts indicate an order processing queue lag or when trade desk operators report delayed order acknowledgments.

## 2. Immediate Diagnostic Steps (Forensics)

### Step 2.1: Verify Process Status
Check if the trading engine process is active on the Linux host:
`ps aux | grep order_engine.py`

### Step 2.2: Scan Log File for Active Errors
Inspect `trading_engine.log` for unhandled exceptions or connection timeouts:
`grep "ERROR" trading_engine.log`
`grep "CRITICAL" trading_engine.log`

### Step 2.3: Calculate Error Frequency
Determine the error count to evaluate severity:
`grep -c "ERROR" trading_engine.log`

## 3. Standard Remediation Steps

### Option A: Transient Network / Database Lock
1. Safely stop the order processing daemon.
2. Verify lock clearance in the database connection pool.
3. Restart the engine service:
`python3 app/order_engine.py`

### Option B: Malformed Payload Ingestion
1. Locate offending order ID from log error output (`grep "ERROR" trading_engine.log`).
2. Move message to Dead Letter Queue (DLQ) for manual reconciliation.
3. Resume queue ingestion.

## 4. Escalation Path
If processing queue depth does not decrease within 15 minutes of service restart:
1. Escalate to L3 Core Trading Engineering team.
2. Open Incident ticket in ServiceNow (P1/P2 depending on financial risk).
3. Notify Trade Operations leads via Incident Bridge.
