from bs4 import BeautifulSoup
import requests


def parse(text):
    phone = set()
    current_text = ''
    for char in text:
        if char == '>':
            current_text = ''
        elif char == '<':
            if current_text.strip() and (current_text !='[' and current_text != ', '):
                phone.add(str(current_text))
                current_text = ''
        else:
            current_text += char
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

    print("\n")


if __name__ == "__main__":
    main()
