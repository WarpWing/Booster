




def a():
    print("Function a is running at time: " + str(int(time.time())) + " seconds.")

def b():
    print("Function b is running at time: " + str(int(time.time())) + " seconds.")\

threading.Thread(target=a).start()
threading.Thread(target=a).start()
threading.Thread(target=a).start()
threading.Thread(target=a).start()

