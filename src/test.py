import threading
import time



def a():
    print("Function a is running at time: " + str(int(time.time())) + " seconds.")

def b():
    print("Function b is running at time: " + str(int(time.time())) + " seconds.")


####

for i in range(5): 
    def c():
        print(f"Iteration {i}") 
        print("Function c is running at time: " + str(int(time.time())) + " seconds.")
    threading.Thread(target=c).start()

