import csv
with open("students.csv", 'w', encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f,fieldnames=["name","age","score"])
    writer.writeheader()
    writer.writerow({"name":"Alice","age":20,"score":85})
    writer.writerow({"name": "Bob", "age": 21, "score": 92})
    writer.writerow({"name": "Cindy", "age": 19, "score": 78})
    writer.writerow({"name": "David", "age": 22, "score": 90})
    writer.writerow({"name": "Eva", "age": 20, "score": 88})
    writer.writerow({"name": "Frank", "age": 21, "score": 65})
    writer.writerow({"name": "Grace", "age": 20, "score": 95})
    writer.writerow({"name": "Henry", "age": 19, "score": 72})
    writer.writerow({"name": "Ivy", "age": 22, "score": 83})
    writer.writerow({"name": "Jack", "age": 21, "score": 60})

