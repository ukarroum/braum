import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Braum: An experimental web ids")
    parser.add_argument("--log-path", help="path to the access logs")

    args = parser.parse_args()

