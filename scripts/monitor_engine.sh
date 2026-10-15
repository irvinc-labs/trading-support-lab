#!/bin/bash
# ==============================================================================
# Script: scripts/monitor_engine.sh
# Purpose: Real-time log monitor and threshold alerting (Automated Sentinel)
# ==============================================================================

LOG_FILE="trading_engine.log"
THRESHOLD=3

if [ ! -f "$LOG_FILE" ]; then
echo "[ALERT] Log file $LOG_FILE not found!"
exit 1
fi

ERROR_COUNT=$(grep -c "ERROR" "$LOG_FILE")
CRITICAL_COUNT=$(grep -c "CRITICAL" "$LOG_FILE")

echo "============================================="
echo " TRADING ENGINE HEALTH STATUS CHECK"
echo "============================================="
echo "Total Errors Found: $ERROR_COUNT"
echo "Total Critical Events: $CRITICAL_COUNT"
echo "============================================="

if [ "$ERROR_COUNT" -gt "$THRESHOLD" ]; then
echo "[STATUS: CRITICAL] Error count ($ERROR_COUNT) exceeds operational threshold ($THRESHOLD)!"
echo "[ACTION REQUIRED] Triggering L2 incident response..."
else
echo "[STATUS: HEALTHY] System operating within normal parameters."
fi
