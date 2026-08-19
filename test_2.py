#test_2.py
import random, time

t1 = time.time()
for i in range(100):
  print(random.randint(1,50))
  time.sleep(0.1)

t2 = time.time()
print(f"Time taken: {t2-t1}")
