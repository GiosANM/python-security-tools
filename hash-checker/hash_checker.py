import argparse, hashlib
from pathlib import Path

def sha256_file(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("file")
    args = p.parse_args()
    print(sha256_file(args.file))
