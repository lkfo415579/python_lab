# -*- coding: utf-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import tornado.gen
from tornado.concurrent import run_on_executor
# 这个并发库在python3自带;在python2需要安装sudo pip install futures
from concurrent.futures import ThreadPoolExecutor
import time
from tornado.options import define, options
define("port", default=8002, help="run on the given port", type=int)

class SleepHandler(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(2)

    def get(self):
        tornado.ioloop.IOLoop.instance().add_callback(self.sleep)       # 这样将在下一轮事件循环执行self.sleep
        self.write("when i sleep")

    @run_on_executor
    def sleep(self):
        time.sleep(5)
        print("yes")
        return 5


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
            (r"/sleep", SleepHandler), ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
