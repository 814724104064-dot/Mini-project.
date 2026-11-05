# Firewall Rule Optimization – Mini Project

## Project overview
A Python educational simulation that removes exact duplicate firewall rules,
detects rules that use the same protocol and port with different actions, and
displays the remaining rules in priority order.

## Requirements
- Python 3.8 or later
- No external libraries required

## How to run
1. Extract the ZIP file.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python main.py
   ```

## Rule format
Each rule is represented as:

`(priority, protocol, port, action)`

Example: `(1, "TCP", 80, "ALLOW")`

A lower priority number is displayed first.

## Important note
This is a classroom simulation only. It does not install, configure, or change
a real firewall. Conflicting rules are reported for manual review rather than
automatically removed, because real firewall behavior depends on rule order
and the firewall platform's matching semantics.
