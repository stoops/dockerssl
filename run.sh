#!/bin/bash
cd /
python3 -m http.server >/dev/null 2>&1 &
python3 /app/cert.py >/dev/null 2>&1
exit 0
