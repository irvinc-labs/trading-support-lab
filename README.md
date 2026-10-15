# Trading Support Lab

A simulated production support environment modeled after enterprise financial systems, built to demonstrate incident triage, log analysis, ITIL-compliant runbooks, and operational resilience.

## Architecture & Scope
* **Simulation Engine:** Python-based order ingestion and settlement processor (`app/order_engine.py`).
* **Environment:** Executed and tested in Linux (WSL Ubuntu).
* **Focus Areas:** 
  * Incident Management & P1 Triage (`incidents/`)
  * Standard Operating Procedures & Runbooks (`runbooks/`)
  * Log forensics and error isolation.

## Repository Structure

    trading-support-lab/
    ├── app/
    │   └── order_engine.py         # Python trading simulation & error generator
    ├── incidents/
    │   └── INC-4092-P1-Outage.md   # ServiceNow-style P1 incident ticket
    ├── runbooks/
    │   └── RB-01-Stuck-Orders.md   # L1/L2 Operational Runbook
    └── trading_engine.log          # Runtime log output (ignored by Git)

## How to Run the Simulation

1. **Clone the repository:**
   `git clone https://github.com/irvinc-labs/trading-support-lab.git`
   `cd trading-support-lab`

2. **Execute the Trading Engine:**
   `python3 app/order_engine.py`

3. **Inspect Output:**
   * Terminal output displays live log events.
   * A `trading_engine.log` file will be generated in the root directory for log forensics.
