# Incident Ticket: INC-4092-P1

**Service Affected:** Order Management & Settlement Pipeline (OMS)  
**Severity:** P1 - Critical (Trading Flow Impacted)  
**Status:** Resolved  
**Reported By:** Automated Monitoring / L1 Support Desk  
**Assigned To:** Production Support Analyst (Irvinc-Labs)  

---

### Timeline (AEST)
* **09:15 AM** - Alert triggered: Spike in database timeout exceptions on order `ORD-1002`.
* **09:18 AM** - L1 desk pages L2 Production Support; incident ticket created.
* **09:22 AM** - L2 Support investigates `trading_engine.log` and isolates the database pool exhaustion error.
* **09:30 AM** - Temporary mitigation applied: Cleared stale connections and restarted the worker process.
* **09:45 AM** - Verification checks confirm trade ingestion and settlement flows have normalized. Incident closed.

### Resolution Summary
Identified unclosed transaction handles during peak order matching. Restarted the ingestion service and verified normal execution logs. Handed over to Problem Management for root cause analysis (RCA).
