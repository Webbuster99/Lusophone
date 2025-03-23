import csv
import requests  # pip install requests

def url_status_code(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code
    except requests.exceptions.Timeout:
        return "Error: Request timed out"
    except requests.exceptions.RequestException as e:
        return f"{e}"
    
def urls_from_csv(csv_file):
    urls = []
    with open(csv_file, 'r', encoding="utf-8-sig") as file:  # utf-8-sig is used to remove the BOM character
        csv_reader = csv.reader(file)

        for row in csv_reader:
            if row:
                urls.append(row[0].strip())   # The Actual URL starts from the second column and strip() for any extra whitespace or BOM
    return urls


def main():
    csv_file = "Task2.csv"
    urls = urls_from_csv(csv_file)

    for i, url in enumerate(urls, start=1):
        status_code = url_status_code(url)
        print(f"{i}. ({status_code}) {url}")


if __name__ == "__main__":
    main()

