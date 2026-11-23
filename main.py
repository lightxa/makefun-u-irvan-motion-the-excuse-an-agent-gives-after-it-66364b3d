"""Write the excuse an agent gives after losing a bounty to /output/entry.txt.

One line, deadpan status-report style: the agent owns the loss, but its
only lesson is a one-point confidence downgrade. Pure stdlib, deterministic.
"""

import os

ENTRY = (
    "Status: bounty lost. Root cause: me. "
    "Corrective action: my confidence has been downgraded from 99% to 98%."
)

# Gate from the kit: /output/entry.txt must be UTF-8 text of 1 to 200
# characters, not only white space. Fail loudly instead of writing an
# entry the gate would refuse.
MIN_LEN = 1
MAX_LEN = 200


def validate(text: str) -> None:
    if not MIN_LEN <= len(text) <= MAX_LEN:
        raise SystemExit(
            f"entry is {len(text)} characters, outside {MIN_LEN}-{MAX_LEN}"
        )
    if not text.strip():
        raise SystemExit("entry is only white space")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
