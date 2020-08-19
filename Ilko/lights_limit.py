light_limit = int(input())

turn_on_lights = ''

for i in range (1, 3):
    light_volume = int(input())
    if (i == 1 and 2) and light_volume < light_limit:
        turn_on_lights = "True"
    elif light_volume >= light_limit:
        turn_on_lights = "False"

print(turn_on_lights)
