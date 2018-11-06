import tornado.ioloop
import tornado.web
import json

#curl -XPOST 'http://10.133.146.50:8888/tenant?user=lily&age=5' -d'{"appid":["10001","10002"]}'

#POST方法
class TenantHandler(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        v = self.get_argument('user')
        a=int(self.get_argument('age'))

        payload = json.loads(self.request.body)
        appid=payload['appid']
        #获取参数，进行其它的处理

        result = {
            "code": 0,
            "msg": "ok",
            "data": {'user':v,'age':a,'num':appid}
        }

        self.write(json.dumps(result))

#DELETE方法
class TenantDelHandler(tornado.web.RequestHandler):
    def delete(self):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        v = self.get_argument('user')
        a = int(self.get_argument('age'))

        payload = json.loads(self.request.body)
        appid = payload['appid']
        # 获取参数，进行其它的处理

        result = {
            "code": 0,
            "msg": "ok",
            "data": {}
        }

        self.write(json.dumps(result))

#GET方法
class TenantGetHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        v = self.get_argument('user')
        a = int(self.get_argument('age'))

        payload = json.loads(self.request.body)
        appid = payload['appid']
        # 获取参数，进行其它的处理
        self.write('hello world')

def make_app():
    return tornado.web.Application([
        (r"/tenant", TenantHandler),
        (r"/tenant/del", TenantDelHandler),
        (r"/tenant/get", TenantGetHandler)
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()