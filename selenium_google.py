from selenium.webdriver import Chrome, ChromeOptions, Remote
from selenium.webdriver.common.keys import Keys
import sys
import time

args = sys.argv
#search_word =args[1] 
search_word ='python'

options = ChromeOptions()
# ヘッドレスモードを有効にするには、次の行のコメントアウトを解除する。
#options.headless = True
driver = Chrome(options=options)  # ChromeのWebDriverオブジェクトを作成する。

# Googleのトップ画面を開く。
driver.get('https://www.google.co.jp/')

# タイトルに'Google'が含まれていることを確認する。
#assert 'Google' in driver.title

# 検索語を入力して送信する。
input_element = driver.find_element_by_name('q')
input_element.send_keys(search_word)
input_element.send_keys(Keys.RETURN)

# タイトルに'Python'が含まれていることを確認する。
#assert 'Python' in driver.title

# スクリーンショットを撮る。
#driver.save_screenshot('search_results.png')

# 検索結果を表示する。
result = []
for h3 in driver.find_elements_by_css_selector('a > h3'):
    a = h3.find_element_by_xpath('..')  # h3の親要素を取得。
    #print("a = ",a)
    title = h3.text
    href = a.get_attribute('href')
    result.append((title, href))
    print("\n")

print("result = ", result)


print('add --------------------------')
i = 0
for title, href in result:
    print('i=',i)
    print('title=',title)
    print('url=',href)
    time.sleep(1)
    driver.get(href)
    
    # 検索結果を表示する。
    try:
        h1 = driver.find_elements_by_css_selector('h1')
        print("h1 = ",h1[i].text)

        h2 = driver.find_elements_by_css_selector('h2')
        print("h2 = ",h2[i].text)

    except:
        print("error")


    print("\n")
    i = i+1
    #break



    
driver.quit()  # ブラウザーを終了する。
