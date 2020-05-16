from selenium.webdriver import Chrome, ChromeOptions, Remote
from selenium.webdriver.common.keys import Keys
import sys
import time

args = sys.argv
#search_word ='python'
search_word = args[1] 

options = ChromeOptions()
# ヘッドレスモードを有効にするには、次の行のコメントアウトを解除する。
#options.headless = True
driver = Chrome(options=options)  # ChromeのWebDriverオブジェクトを作成する。

# Googleのトップ画面を開く。
#driver.get('https://kassiopeya.com/archives/3121')
arg_url = "https://www.google.co.jp/search?hl=jp&gl=JP&num=10&q="+search_word
driver.get(arg_url)
print("u r l = ", arg_url)


print("summary start----------------------------------------")
# 検索結果を表示する。
i = 1
#for h3 in driver.find_elements_by_css_selector('a > h3'):
for h3 in driver.find_elements_by_css_selector('div #search a > h3'):
    print(f"No.{i}")
    print("title= ",h3.text)
    a = h3.find_element_by_xpath('..')
    #divrc = a.find_element_by_xpath('..//..')
    divrc = a.find_element_by_xpath('..//..//*//span[@class="st"]')
    print("url = ",a.get_attribute('href'))
    #print("divrc = ",divrc.get_attribute('class'))
    #print("divrc = ",divrc.get_attribute('.//span[@class="st"]'))
    print("meta = ",divrc.text)
    print("----------------------------------------")
    i = i + 1


print("summary end  ----------------------------------------")
quit()

print("detail  start----------------------------------------")
# 検索結果を表示する。
for htag in driver.find_elements_by_css_selector('h2 > span,h3 > span'):
    print("h23tag = ",htag.text)

print("detail  end  ----------------------------------------")

driver.quit()  # ブラウザーを終了する。
