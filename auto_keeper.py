import time

import requests

Headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}


def send_respost(thread):
    postdata = {
        "name": "",
        "text": "保守",
        "thread": thread,
    }
    pre_response = requests.post(
        "https://bbs.animanch.com/inc/comment.php?preCheck",
        headers=Headers,
        data=postdata,
    )
    if pre_response.status_code == 200:
        response = requests.post(
            "https://bbs.animanch.com/inc/comment.php", headers=Headers, data=postdata
        )
        if response.status_code == 200:
            print("Success:", response.json())
        else:
            print("Failed:", response.status_code, response.text)
    else:
        print("Failed:", pre_response.status_code, pre_response.text)


def main():
    thread = int(input("threadの数字を入力:"))
    try:
        repeat = int(input("繰り返し時間を入力してください(デフォルト:8時間)"))
    except ValueError:
        repeat = 8
    repeat = repeat * 3600
    while True:
        send_respost(thread)
        time.sleep(repeat)


if __name__ == "__main__":
    main()
