from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

#SWORD = "python"
SWORD = sys.argv[1]

# Firefoxのドライバを得る --- (※1)
options = FirefoxOptions()
#options.add_argument('-headless')
driver = Firefox(options=options)

# ログインページにアクセス --- (※2)
url_login = "https://www.google.com/"
driver.get(url_login)

# 検索語を入力して送信する。
input_element = driver.find_element_by_name('q')
input_element.send_keys(SWORD)
input_element.send_keys(Keys.RETURN)

# 検索結果を表示する。
for h3 in driver.find_elements_by_css_selector('a > h3'):
    a = h3.find_element_by_xpath('..')  # h3の親要素を取得。
    print("h3 = ",h3.text)
    print("url = ",a.get_attribute('href'))
    print("\n")


# ブラウザのスクリーンショット取得
#time.sleep(2)
#driver.save_screenshot("website.png")

# ブラウザの終了
#driver.quit()

