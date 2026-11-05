"""
Firewall Rule Optimization - Educational Mini Project

This program:
1. Removes exact duplicate rules.
2. Detects rules with the same protocol and port but different actions.
3. Displays the remaining rules in priority order.

Note: This is a learning simulation. It does not modify a real firewall.
"""

rules = [
    (1, "TCP", 80, "ALLOW"),
    (2, "UDP", 53, "ALLOW"),
    (3, "TCP", 80, "ALLOW"),
    (4, "TCP", 22, "BLOCK"),
    (5, "UDP", 53, "BLOCK"),
]


def optimize_rules(firewall_rules):
    # Remove exact duplicates while preserving the original order.
    optimized = list(dict.fromkeys(firewall_rules))

    # Detect same protocol/port with different actions.
    actions_by_key = {}
    conflicts = set()

    for priority, protocol, port, action in optimized:
        key = (protocol, port)
        if key in actions_by_key and actions_by_key[key] != action:
            conflicts.add(key)
        else:
            actions_by_key[key] = action

    # Lower priority number is processed first.
    optimized.sort(key=lambda rule: rule[0])
    return optimized, sorted(conflicts)


def main():
    optimized, conflicts = optimize_rules(rules)

    print("FIREWALL RULE OPTIMIZATION")
    print("-" * 30)
    print(f"Original Rules: {len(rules)}")
    print(f"Optimized Rules: {len(optimized)}")

    print("\nOptimized Firewall Rules:")
    for rule in optimized:
        print(rule)

    print("\nConflicting Rules (protocol, port):")
    if conflicts:
        for conflict in conflicts:
            print(conflict)
    else:
        print("No conflicts found.")

    print("\nNote: Conflicts are reported for manual review; no rule is automatically deleted.")


if __name__ == "__main__":
    main()
