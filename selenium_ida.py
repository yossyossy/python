from selenium.webdriver import Chrome, ChromeOptions, Remote
from selenium.webdriver.common.keys import Keys
import sys
import time

args = sys.argv
#search_word =args[1] 
search_word ='python'

options = ChromeOptions()
# ヘッドレスモードを有効にするには、次の行のコメントアウトを解除する。
options.headless = True
driver = Chrome(options=options)  # ChromeのWebDriverオブジェクトを作成する。

# Googleのトップ画面を開く。
driver.get('https://www.atmarkit.co.jp/ait/articles/1904/02/news024.html')


# 取得
#list_title = driver.find_elements_by_css_selector('title')
#list_h1 = driver.find_elements_by_css_selector('h1')
#list_h2 = driver.find_elements_by_css_selector('h2')

#print("list_h1 = ",list_h1)
#print("list_h2 = ",list_h2)

#for t in list_title:
#    print("title = ",t.text)

# 検索結果を表示する。
#for h1 in driver.find_elements_by_css_selector('h1'):
for h2 in driver.find_elements_by_css_selector('h2'):
#for h1 in list_h1:
    #print("h1 = ",h1)
    print("h2.text = ",h2.text)



driver.quit()  # ブラウザーを終了する。
