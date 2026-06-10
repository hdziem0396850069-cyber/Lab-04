import tornado.ioloop
import tornado.web
import tornado.websocket

clients = set()

class WebSocketServer(tornado.websocket.WebSocketHandler):
    def open(self):
        clients.add(self)
        print("New client connected")

    def on_close(self):
        clients.remove(self)
        print("Client disconnected")

    def on_message(self, message):
        print("Received:", message)
        # Broadcast to all connected clients
        for client in clients:
            client.write_message(message)

def make_app():
    return tornado.web.Application([
        (r"/websocket", WebSocketServer),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("WebSocket server running on ws://localhost:8888/websocket")
    tornado.ioloop.IOLoop.current().start()
