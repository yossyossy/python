from selenium.webdriver import Chrome, ChromeOptions, Remote
from selenium.webdriver.common.keys import Keys
import sys
import time

args = sys.argv
arg_url = args[1] 
#arg_url = 'https://kassiopeya.com/archives/3121'
#search_word ='python'

options = ChromeOptions()
# ヘッドレスモードを有効にするには、次の行のコメントアウトを解除する。
options.headless = True
driver = Chrome(options=options)  # ChromeのWebDriverオブジェクトを作成する。

# Googleのトップ画面を開く。
#driver.get('https://kassiopeya.com/archives/3121')
driver.get(arg_url)
print("u r l = ", arg_url)


#for t in driver.find_elements_by_css_selector('h1'):
t_list = driver.find_elements_by_css_selector('h1')
print("title = ",t_list[0].text)
print("\n")


print("summary start----------------------------------------")
# 検索結果を表示する。
for h2 in driver.find_elements_by_css_selector('h2 > span'):
    #print("h_tag = ",h2.text)
    print("h2tag = ",h2.text)


print("summary end  ----------------------------------------")

print("detail  start----------------------------------------")
# 検索結果を表示する。
for htag in driver.find_elements_by_css_selector('h2 > span,h3 > span'):
    print("h23tag = ",htag.text)

print("detail  end  ----------------------------------------")

driver.quit()  # ブラウザーを終了する。
