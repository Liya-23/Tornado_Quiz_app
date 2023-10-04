import tornado.web
import tornado.ioloop

file_path = r"text files/songs.txt"  # Use raw string to avoid escape characters
result_array = []
data_array = []

with open(file_path, "r") as file:
    headings = file.readline().strip().split(", ")  # Read and split the first line (headings)
    for line in file:
        values = line.strip().split(", ")  # Split the line into values
        row_dict = dict(zip(headings, values))  # Create a dictionary using headings as keys
        data_array.append(row_dict)  # Add the dictionary to the array


with open(file_path, "r") as file:
    text_data = file.read()
# Split the text data into lines and extract artists' names
lines = text_data.strip().split('\n')
artists = [line.split(',')[0] for line in lines[1:]]
song_one = [line.split(',')[1] for line in lines[1:]]
song_two = [line.split(',')[2] for line in lines[1:]]
song_three = [line.split(',')[3] for line in lines[1:]]
song_four = [line.split(',')[4] for line in lines[1:]]
# Print the list of artists
print(data_array)
print(artists)
print(song_one)
print(song_two)
print(song_three)
print(song_four)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("web/songs.html", artists=artists)  # Pass artists' names to the template

def make_app():
    return tornado.web.Application([
        (r"/songs", MainHandler),
        (r"/web/static/(.*)", tornado.web.StaticFileHandler, {"path": "web/static"}),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8970)
    print("Server is running on port 8970")
    tornado.ioloop.IOLoop.current().start()
