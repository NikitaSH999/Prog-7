import tornado.ioloop
import tornado.web as web
import tornado.websocket
import asyncio
import json
from collections import deque
from uuid import uuid4

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
          instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class Buffer:
    def __init__(self):
        self.__messages = deque([], 50)
        self.__name = ''

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def add_message(self, name, user_id, message):
        id = uuid4()
        self.__messages.append({'message-id': str(id), "user-id": user_id, "name": name, "message": message})

    def get_messages(self):
        return self.__messages

    def render(self):
        seq_render = []
        seq = self.__messages
        if seq:
            for msg in seq:
                seq_render.append(f'<li><span class="name">{msg["name"]}</span><span class="message">{msg["message"]}</span></li>')
        return json.dumps({"messages": ''.join(seq_render)})

class StartHandler(web.RequestHandler):
    def get(self):
        self.render('autorization.html')

class IndexHandler(web.RequestHandler):
    def get(self):
        self.render('index.html')

class StatisticsHandler(web.RequestHandler):
    def get(self):
        self.render('statistics.html')

buffer = Buffer()

class MainHandler(tornado.websocket.WebSocketHandler):
    connection = set()

    def open(self):
        self.connection.add(self)
        self.id = str(uuid4())
        print('new websocket is open')

    def on_message(self, message):
        data = json.loads(message)
        print(data)
        if data.get("request"):
            if data["request"] == "add message":
                buffer.add_message(data["name"], self.id, data['message'])
                [con.write_message(json.dumps({"getUpdate": "new message"})) for con in self.connection]
            if data["request"] == "get name":
                name = {"setName": buffer.get_name()}
                self.write_message(json.dumps(name))
            if data["request"] == "update":
                self.write_message(buffer.render())
            if data["request"] == "stat":
                self.id += '-------stat'
                nconn = len(self.connection) - 1
                resp = {"allUsers": nconn, "stat": "ok"}
                messages = buffer.get_messages()
                for con in self.connection:
                    summ = 0
                    for msg in messages:
                        if msg["user-id"] == con.id:
                            summ += 1
                    resp.update({con.id: summ})
                self.write_message(json.dumps(resp))
        else:
            buffer.set_name(data["name"])

    def on_close(self):
        print('some websocket is close')
        self.connection.remove(self)

def make_app():
    return web.Application([
        (r"/", StartHandler),
        (r"/index", IndexHandler),
        (r"/stat", StatisticsHandler),
        (r"/websocket", MainHandler)
    ], debug=True)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888, 'localhost')
    tornado.ioloop.IOLoop.current().start()