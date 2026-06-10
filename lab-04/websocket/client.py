import tornado.ioloop
import tornado.websocket
import asyncio

url = "ws://localhost:8888/websocket"

class Client:
    def __init__(self, io_loop):
        self.io_loop = io_loop
        self.connection = None

    async def connect_and_read(self):
        while True:
            try:
                self.connection = await tornado.websocket.websocket_connect(url)
                while True:
                    message = await self.connection.read_message()
                    if message is None:
                        break
                    self.on_message(message)
            except Exception as e:
                print("Connection error:", e)
                await asyncio.sleep(3)

    def on_message(self, message):
        print("Received message:", message)

if __name__ == "__main__":
    io_loop = tornado.ioloop.IOLoop.current()
    client = Client(io_loop)
    io_loop.add_callback(client.connect_and_read)
    io_loop.start()
