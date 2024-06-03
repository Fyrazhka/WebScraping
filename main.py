from bs4 import BeautifulSoup
import requests
import re


def parse(text):
    phone = []
    text_pattern = re.compile(r'<.*?>')
    current_text = text_pattern.sub("", text).split(',')
    phone.extend(current_text)
    return phone


def main():
    url = 'https://shop.mts.by/phones/'
    html_content = ""
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
    else:
        print("Response Error", response.status_code)
    soup = BeautifulSoup(html_content, 'html.parser')
    phone_name = set(parse(str(soup.select('.products__unit__title a'))))
    phone_price = set(parse(str(soup.select('.products__unit__price__number--full'))))

    for name, price in zip(phone_name, phone_price):
         print(f"Phone: {name} | Price: {price}")


if __name__ == "__main__":
    main()
