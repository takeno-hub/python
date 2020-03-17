import time
import schedule
from selenium import webdriver
from bs4 import BeautifulSoup

def job():
    # 仮想ブラウザ起動、URL先のサイトにアクセス
    driver = webdriver.Chrome()
    driver.get('https://www.chunichi.co.jp/hokuriku/article/fishing/')
    time.sleep(2)

    # ret = soup.find('.bl-bigger')
    driver.find_element_by_class_name('bl-bigger').click()
    sc_text = driver.find_element_by_class_name('News-detail').text
    sc_date = driver.find_element_by_class_name('data').text
    print(sc_date)
    print(sc_text)

    import requests
    token = "ljsMu3RiRQq2TjW4YV2iX8LtBjHCLfVgn0VZlPfquQo"
    url = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": "Bearer " + token}
    payload = {"message": sc_date}
    payload = {"message": sc_text}
    requests.post(url, headers=headers, data=payload)
def main():
    schedule.every().thursdayat("12:00").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

main()
