import module_1.function1 as f1
import module_2.function2 as f2
import module_3.function3 as f3

def main():
    totalFruits = f1.appleCount() + f2.orangeCount() + f3.grapeCount()

    print(totalFruits)


if __name__=="__main__":
    main()