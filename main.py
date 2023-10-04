import tornado.web
import tornado.ioloop
import random

file_path = "text files\songs.txt"
data_array = []

with open(file_path, "r") as file:
    headings = file.readline().strip().split(", ")  # Read and split the first line (headings)
    
    for line in file:
        values = line.strip().split(", ")  # Split the line into values
        row_dict = dict(zip(headings, values))  # Create a dictionary using headings as keys
        data_array.append(row_dict)  # Add the dictionary to the array

print(data_array)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("web\songs.html", artist="", question="", score="")

def make_app():
    return tornado.web.Application([
        (r"/songs", MainHandler),
        (r"/web/static/(.*)", tornado.web.StaticFileHandler, {"path": "web/static"}),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8970)
    print("sun on port 8970")
    tornado.ioloop.IOLoop.current().start()