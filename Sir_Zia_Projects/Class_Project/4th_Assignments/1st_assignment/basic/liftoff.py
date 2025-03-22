import time

def countdown():
    for i in range(10, 0, -1):  # ✅ Reverse counting karega
        print(i, end=" ", flush=True)  # ✅ Line-by-line delay
        time.sleep(0.5)  # ✅ Realistic effect ke liye delay
    print("\n🚀 Liftoff!")

if __name__ == '__main__':
    countdown()
