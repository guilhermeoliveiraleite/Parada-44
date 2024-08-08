import time
for n1 in range(10):
    
     print(f"************ {n1+1} *************")
     for x in range(10): 
       print(f"        {n1+1} x {x+1} = {(n1+1)*(x+1)}")
time.sleep (1)



# ----------------------------------------------- #

# for a in range (1, 11): 
#     print("********")
#     for b in range (10):
#         print(f"{a} x {b+1} = {(b+1)*a}")