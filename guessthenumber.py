print("""
  ________                                __  .__                                 ___.                 
 /  _____/ __ __   ____   ______ ______ _/  |_|  |__   ____     ____  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/ \   __\  |  \_/ __ \   /    \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \   |  | |   Y  \  ___/  |   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >  |__| |___|  /\___  > |___|  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/             \/     \/       \/            \/    \/     \/       
                                                                                                       
                                                                                                       
                                                                                                       
                                                                                                       
                                                                                                       
                                                                                                       
""")
target=24
mode=input("easy or hard")
if mode=="easy":
  i=10
if mode=="hard":
  i=5
for j in range(i):
  n=int(input("enter a number between 1 and 100"))
  if n==target:
    print(f"number is {n}")
    break
  elif n<target:
    print("Too low")
  else:
    print("Too High")
