import argparse, hashlib, json
from pathlib import Path

def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(65536), b""):
            h.update(block)
    return h.hexdigest()

def create_baseline(directory, output):
    root = Path(directory)
    baseline = {
        str(p.relative_to(root)): digest(p)
        for p in root.rglob("*") if p.is_file()
    }
    Path(output).write_text(json.dumps(baseline, indent=2), encoding="utf-8")

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Create a SHA-256 integrity baseline.")
    p.add_argument("directory")
    p.add_argument("--output", default="baseline.json")
    args = p.parse_args()
    create_baseline(args.directory, args.output)
    print(f"Baseline written to {args.output}")
