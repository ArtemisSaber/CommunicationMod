#!/usr/bin/env python3
"""Test script for CommunicationMod - captures raw JSON and hex-dumps non-ASCII."""
import sys, json, os

stderr = open(os.path.expanduser("~/test_comm_output.txt"), "w")

print("ready", flush=True)

while True:
    line = sys.stdin.buffer.readline()
    if not line:
        break
    decoded = line.decode('utf-8')
    try:
        data = json.loads(decoded)
        gs = data.get('game_state', {})
        deck = gs.get('deck', [])
        for card in deck:
            name = card.get('name', '')
            stderr.write(f"CARD: id={card.get('id')}, name='{name}', hex={name.encode('utf-8').hex()}\n")
        # Also check event
        ss = gs.get('screen_state', {})
        event_name = ss.get('event_name', '')
        stderr.write(f"EVENT_NAME: '{event_name}' hex={event_name.encode('utf-8').hex()}\n")
        for opt in ss.get('options', []):
            label = opt.get('label', '')
            text = opt.get('text', '')
            stderr.write(f"OPTION: label='{label}' hex={label.encode('utf-8').hex()}, text='{text}' hex={text.encode('utf-8').hex()}\n")
        stderr.write("---\n")
        stderr.flush()
    except Exception as e:
        stderr.write(f"ERR: {e}\n")
        stderr.flush()
