import argparse

from selenium import webdriver

scans = []

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Braum: An experimental web vulnerability scanner tool")
    parser.add_argument("--url", required=True)

    args = parser.parse_args()

    driver = webdriver.Firefox()

    for scan in scans:
        driver.get(args.url)
        if scan(driver):
            print(f"Found vulnerability: {scan.name}")

    driver.close()
