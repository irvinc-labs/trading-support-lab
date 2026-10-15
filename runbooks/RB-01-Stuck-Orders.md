# Runbook: Handling Stuck Trade Settlements

**Document ID:** RB-01  
**Target Audience:** L1 / L2 Production Support Analysts  

## Purpose
To provide step-by-step instructions for identifying and safely resolving orders stuck in a pending settlement state due to database connectivity timeouts.

## Step 1: Detection & Verification
1. Check the primary log aggregator or local log file for the error signature:
   `CRITICAL: Database connection pool exhausted`
2. Run log checks or inspect `trading_engine.log` to determine the affected order IDs.

## Step 2: Immediate Mitigation
1. Notify stakeholders via the incident bridge or chat channel.
2. Safely restart the local processing daemon.
3. Validate that incoming orders resume normal processing states (`SUCCESS`).

## Step 3: Escalation
If connection pool errors persist for more than 15 minutes post-restart, escalate immediately to the Database Administration (DBA) team.
