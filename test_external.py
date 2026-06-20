#!/usr/bin/env python3
"""Test external process for CommunicationMod - echoes received game state."""
import sys, json

print("ready", flush=True)
while True:
    line = sys.stdin.readline()
    if not line:
        break
    try:
        data = json.loads(line)
        sys.stderr.write(f"OK: screen_type={data.get('screen_type', 'N/A')}, in_game={data.get('in_game')}, ready={data.get('ready_for_command')}\n")
        sys.stderr.flush()
    except json.JSONDecodeError as e:
        sys.stderr.write(f"ERR: {e}\n")
        sys.stderr.flush()
