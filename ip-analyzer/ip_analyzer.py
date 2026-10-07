import argparse, ipaddress

def analyze(value):
    ip = ipaddress.ip_address(value)
    return {
        "address": str(ip),
        "version": ip.version,
        "private": ip.is_private,
        "global": ip.is_global,
        "loopback": ip.is_loopback,
        "multicast": ip.is_multicast,
    }

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("ip")
    args = p.parse_args()
    for k, v in analyze(args.ip).items():
        print(f"{k}: {v}")
