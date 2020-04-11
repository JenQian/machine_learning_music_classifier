# @app.route("/")
# def index():
#   with open('audio_only.csv') as csv_file:
#     data = csv.reader(csv_file, delimiter=',')
#     first_line = True
#     places = []
#     for row in data:
#       if not first_line:
#         places.append({
#           "city": row[0],
#           "attraction": row[1],
#           "gif_url": row[2]
#         })
#       else:
#         first_line = False
#   return render_template("index.html", places=places)