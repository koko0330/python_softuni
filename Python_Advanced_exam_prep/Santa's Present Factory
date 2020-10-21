from collections import deque

boxes = [int(x) for x in input().split()]
magics = deque([int(x) for x in input().split()])

toys = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}
crafted = {"Doll": 0, "Wooden train": 0, "Teddy bear": 0, "Bicycle": 0}

while boxes and magics:
    box = boxes.pop()
    magic = magics.popleft()

    if box == 0 and magic == 0:
        continue

    if box == 0:
        magics.appendleft(magic)
        continue

    if magic == 0:
        boxes.append(box)
        continue

    total = box * magic

    if total in toys:
        toy = toys[total]
        crafted[toy] += 1

    elif total < 0:
        summed = box + magic
        boxes.append(summed)

    elif total > 0:
        boxes.append(box + 15)

if (crafted["Doll"] and crafted["Wooden train"]) or (crafted["Teddy bear"] and crafted["Bicycle"]):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if boxes:
    print(f"Materials left: {', '.join([str(x) for x in reversed(boxes)])}")
if magics:
    print(f"Magic left: {', '.join([str(x) for x in magics])}")

for (item, quantity) in sorted(crafted.items()):
    if quantity:
        print(f"{item}: {quantity}")
