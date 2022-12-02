file_name = "database/val@email.com_Mathematics.txt"
with open(file_name, "rb") as file:
    data = file.read()[:-256]
data = data.decode('utf-8')

marks = []
data = data.split("[")

data.pop(0)
data = data[0].split("}]")

data.pop(-1)
data = data[0].split("},")

for mark in data:
    marks.append(mark + "}")

mark_show = []
for mark in marks:
    mark_show.append(mark[(16+len("Mathematics")):-1] )
