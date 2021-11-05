n = int(input("Please input a number: "))

oddsum = 0
evensum = 0
count = 0

for i in range(1,n+1):
    if i%2 == 1:
        oddsum += i
    else:
        evensum += i
        count += 1

avg_even = evensum / count

print("Sum of odd numbers: ", oddsum)
print("Average of even numbers: ", avg_even)