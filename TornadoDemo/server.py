# -*- coding: utf-8 -*-

import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=19521, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('./templates/index.html')


class ModelHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('./templates/First.html', title='模板页', header_text='first header', footer_text='Footer goes here')


class PoemPageHandler(tornado.web.RequestHandler):
    def post(self):
        noun1 = self.get_argument('noun1')
        noun2 = self.get_argument('noun2')
        verb = self.get_argument('verb')
        noun3 = self.get_argument('noun3')
        lists = ['3213', '321321', 'zhafkakg']
        self.render('./templates/poem.html', roads=noun1, wood=noun2, made=verb,
                    difference=noun3, listss=lists)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r'/', IndexHandler),
                    (r'/poem', PoemPageHandler),
                    (r'/model', ModelHandler),
                    (r'/main', MainHandler)]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "views"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./templates/index.html")


if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
