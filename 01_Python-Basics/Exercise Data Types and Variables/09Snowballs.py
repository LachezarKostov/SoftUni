N = int(input())
MAXSnowballValue = 0
MAXsnowballSnow = 0
MAXsnowballTime = 0
MAXsnowballQuality = 0


for i in range(N):
    snowballSnow = int(input())
    snowballTime = int(input())
    snowballQuality = int(input())

    snowballValue = (snowballSnow // snowballTime) ** snowballQuality

    if snowballValue > MAXSnowballValue:
        MAXSnowballValue = snowballValue
        MAXsnowballSnow = snowballSnow
        MAXsnowballTime = snowballTime
        MAXsnowballQuality = snowballQuality

print(f"{MAXsnowballSnow} : {MAXsnowballTime} = {MAXSnowballValue} ({MAXsnowballQuality})")
