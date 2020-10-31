import math

rec = float(input())
dis = float(input())
t1m = float(input())

drag = (math.floor(dis / 15))*12.5

time = t1m * dis

final_time = time + drag

if final_time >= rec:
    print(f"No, he failed! He was {(final_time-rec):.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {final_time:.2f} seconds.")


