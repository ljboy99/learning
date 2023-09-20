from tqdm import tqdm
import time
#I'm a dirty thief, I copy-pasted off of geeksforgeeks
#Forgive me, I just wanted to make my notes T-T
for i in tqdm(range(101),
              #Present a loading message next
              #To the progress bar
              desc="Loading…",
              #ascii = True will make it a text bar
              ascii=False,
              #Control the length
              ncols=75):
    #Time delay for demo purposes
    time.sleep(0.1)

print("Complete.")
