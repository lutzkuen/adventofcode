
import math

with open("input.txt", "r") as f:
    start_ts, bus_lines, _ = f.read().split('\n')

bus_ids = [int(bus_id) for bus_id in bus_lines.split(',') if bus_id != "x"]

shortest_wait = 999999
best_bus = -1
start_ts = int(start_ts)

for bus_id in bus_ids:
    depart_ts = math.ceil(start_ts / bus_id) * bus_id
    if (depart_ts - start_ts) < shortest_wait:
        print(f"{start_ts} {depart_ts} {bus_id}")
        shortest_wait = depart_ts - start_ts
        best_bus = bus_id

print(f"{best_bus} {shortest_wait} {best_bus * shortest_wait}")
