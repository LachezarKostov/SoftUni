from _collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = [int(x) for x in input().split(" ")]
locks = deque([int(x) for x in input().split(" ")])
intelligence = int(input())

counter = 0
starting_bullets = len(bullets)
while bullets:

    if counter == barrel_size:
        print("Reloading!")
        counter = 0
    counter += 1

    if not locks:
        break
    current_bullet = bullets.pop()
    current_lock = locks[0]

    if current_bullet <= current_lock:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")

if not locks:
    bullets_price = (starting_bullets - len(bullets)) * bullet_price
    earned = intelligence - bullets_price
    print(f"{len(bullets)} bullets left. Earned ${earned}")


elif not bullets:
    print(f"Couldn't get through. Locks left: {len(locks)}")

