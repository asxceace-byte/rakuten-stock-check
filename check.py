import requests
from bs4 import BeautifulSoup

# =========================
# 監視する商品
# =========================

ITEMS = [

    {
        "name": "プリンセス&クラシック",
        "url": "https://item.rakuten.co.jp/compass-shop/bonbondrop_2d/?scid=wi_ich_iphoneapp_item_share"
    },

    {
        "name": "ちょこみん",
        "url": "https://item.rakuten.co.jp/symbolstore/sym000530/?scid=wi_ich_iphoneapp_item_share"
    },

    {
        "name": "はちみつ4枚セット",
        "url": "https://item.rakuten.co.jp/nobumaru/sne2604/?scid=wi_ich_iphoneapp_item_share"
    },

    {
        "name": "ちょこみん最安値",
        "url": "https://item.rakuten.co.jp/cinemacollection/qla-01212/?scid=wi_ich_iphoneapp_item_share"
    }

]

# =========================
# Discord Webhook URL
# =========================

WEBHOOK_URL = "https://discordapp.com/api/webhooks/1502088889907806348/4L_Z0fwuCF4R3fO2kPav4WHK-McLL47ta7cMEqLLxuy2NEtEmWYaGFnuneX-PIVPenw6"

headers = {
    "User-Agent": "Mozilla/5.0"
}

for item in ITEMS:

    try:

        r = requests.get(item["url"], headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")

        text = soup.text

        # 在庫復活判定
        if "カートに追加" in text:

            message = {
                "content": f"""🚨【在庫復活】

{item["name"]}

{item["url"]}
"""
            }

            requests.post(WEBHOOK_URL, json=message)

            print(f"{item['name']} 通知送信")

        else:
            print(f"{item['name']} はまだ売り切れ")

    except Exception as e:
        print(f"{item['name']} エラー:", e)
