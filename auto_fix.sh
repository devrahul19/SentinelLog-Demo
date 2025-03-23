#!/bin/bash
LOG_FILE="/var/log/system.log"

if grep -q "error" $LOG_FILE; then
  echo "Issue detected! Restarting service..."
  systemctl restart my_service
fi