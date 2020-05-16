from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time
import requests
import lxml.html

search_word = "python"
#SWORD = sys.argv[1]


# ログインページにアクセス
#ggl_url = "https://www.google.co.jp/search?hl=jp&gl=JP&num=10&q="
#search_result = requests.get(ggl_url + search_word)
search_result = requests.get("https://www.google.co.jp/search?hl=jp&gl=JP&num=10&q="+search_word)
html = search_result.text.encode()
root = lxml.html.fromstring(html)


print('xpath -----------------------------------')
#titles = root.xpath('/html/body/div/*/a/h3')
titles = root.xpath('//a')
print(titles)

print('loop -----------------------------------')
#for title in titles:
#    print(title.text)

#for a in root.cssselect('div#search h3.r a'):
for a in root.find_elements_by_css_selector('a > h3'):
    print(a.get('href'))

print('quit -----------------------------------')
quit()
 

# 検索語を入力して送信する。
#input_element = browser.find_element_by_name('q')
#input_element.send_keys(SWORD)
#input_element.submit()


time.sleep(5)

a = input_element.find_elements_by_css_selector('a > h3')
print(a)
quit()

# 検索結果を表示する。
#for h3 in browser.find_elements_by_css_selector('a > h3'):
for h3 in input_element.find_elements_by_css_selector('a > h3'):
    a = h3.find_element_by_xpath('..')  # h3の親要素を取得。
    print("title = ",a.string)
    print("url = ",a.get_attribute('href'))
    print("\n")


# ブラウザのスクリーンショット取得
#browser.save_screenshot("website.png")

# ブラウザの終了
#browser.quit()

