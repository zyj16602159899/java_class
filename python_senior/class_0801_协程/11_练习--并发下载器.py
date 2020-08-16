import gevent
from gevent import monkey
import urllib.request

monkey.patch_all()


def downloader(img_name, img_url):
    res = urllib.request.urlopen(img_url)
    img_content = res.read()
    with open(img_name, "wb") as f:
        f.write(img_content)


def main():
    gevent.joinall([
        gevent.spawn(downloader, "1.jpg", "https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=1930662946,3376692344&fm=26&gp=0.jpg"),
        gevent.spawn(downloader, "3.jpg", "https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=10391890,2830564177&fm=26&gp=0.jpg")
    ])


if __name__ == '__main__':
    main()
