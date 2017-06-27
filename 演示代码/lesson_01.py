#coding=utf-8
#导入需要的模块
import tornado.httpserver
import tornado.web
import tornado.options
import tornado.ioloop
from tornado.options import define, options

#定义一个默认的端口号
define("port", default=8000, help="port", type=int)

#定义一个请求的处理逻辑
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("abcde")

class AaaHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("aaa")

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello world")


#项目入口
if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r"/", IndexHandler),
            (r'/aaa', AaaHandler),
            (r'/hello', HelloHandler),
        ]
    )
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()






