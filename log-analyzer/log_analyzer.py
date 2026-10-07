import argparse
from collections import Counter
from pathlib import Path

TERMS = ("failed", "failure", "denied", "error", "warning")

def analyze(path):
    lines = Path(path).read_text(encoding="utf-8", errors="ignore").splitlines()
    counts = Counter()
    for line in lines:
        lower = line.lower()
        for term in TERMS:
            if term in lower:
                counts[term] += 1
    return counts

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("logfile")
    args = p.parse_args()
    for term, count in analyze(args.logfile).most_common():
        print(f"{term}: {count}")
