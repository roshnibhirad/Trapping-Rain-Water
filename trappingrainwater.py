height = [1,5,3,2,6,1,3]
total_water = 0
for i, curr in enumerate(height):
    left = 0 if i == 0 else max(height[:i])
    right = 0 if i == len(height) - 1 else max(height[i+1:])
    total_water += max(0, min(left, right) - curr)

print(total_water)