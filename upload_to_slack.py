import os
import logging
from typing import List  # 型ヒントのためにインポート

import requests
from selenium.webdriver import Chrome, ChromeOptions, Remote
from selenium.common.exceptions import NoSuchElementException

# WebhookのURLを環境変数から取得する。
SLACK_INCOMING_WEBHOOK_URL = "https://hooks.slack.com/services/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"


logging.info(f'Notifying to Slack: {SLACK_INCOMING_WEBHOOK_URL}')

# 取得したコンテンツのスキの数とURLをSlackに通知する。
requests.post(SLACK_INCOMING_WEBHOOK_URL, json={
    'text': f':Hello World: {SLACK_INCOMING_WEBHOOK_URL}',
    #'text': f':heart: {content["like"]} {content["url"]}',
    #'unfurl_links': True,  # リンクのタイトルや画像を表示する。
})


