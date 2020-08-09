import time
import threading


class Show(threading.Thread):

    def sing(self):
        """唱歌5秒"""
        for i in range(5):
            print("---正在唱歌---")
            time.sleep(1)

    def dance(self):
        """跳舞5秒"""
        for i in range(5):
            print("---正在跳舞---")
            time.sleep(1)

    def run(self):
        for i in range(2):
            self.sing()
            self.dance()


if __name__ == '__main__':
    t = Show()
    t.start()
