import random

min = 1
max = 8787
count = 0
random_number = random.randint(min,max)
print(random_number)
print("===============猜數字遊戲==================\n\n")
while True:
  num = int(input(f"請輸入數字({min}~{max}:)"))
  count += 1
  if(num == random_number):
    print("猜對了")
    print(f"總共猜了:{count}次")
    break
  elif(num>random_number):
      print(f"小")
      max = num - 1
  elif(num<random_number):
      print(f"大")
      min = num + 1

  print(f"已經猜了{count}次")


print("可以滾了")