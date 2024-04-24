import argparse

scans = []

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Braum: An experimental web vulnerability scanner tool")
    parser.add_argument("--hostname", help="path to the hostname")

    args = parser.parse_args()

    for scan in scans:
        if scan(args.hostname):
            print(f"Found vulnerability: {scan.name}")
