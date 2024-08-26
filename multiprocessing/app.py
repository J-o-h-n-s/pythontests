import multiprocessing as mp
import time
import math

results_a = []
results_b = []
results_c = []


def make_calculation_a(numbers):
    for number in numbers:
        results_a.append(math.sqrt(number**3))


def make_calculation_b(numbers):
    for number in numbers:
        results_b.append(math.sqrt(number**4))


def make_calculation_c(numbers):
    for number in numbers:
        results_c.append(math.sqrt(number**5))


if __name__ == "__main__":
    number_list = list(range(5000000))

    p1 = mp.Process(target=make_calculation_a, args=(number_list,))
    p2 = mp.Process(target=make_calculation_b, args=(number_list,))
    p3 = mp.Process(target=make_calculation_c, args=(number_list,))

    start = time.time()
    make_calculation_a(number_list)
    make_calculation_b(number_list)
    make_calculation_c(number_list)

    temp_a = results_a
    temp_b = results_b
    temp_c = results_c

    time_taken_sp = time.time() - start
    print("Time taken while single processing:", time_taken_sp)

    start = time.time()
    p1.start()
    p2.start()
    p3.start()
    time_taken_mp = time.time() - start
    print("Time taken while multi processing:", time_taken_mp)

    print(
        "Results are equal:",
        temp_a == results_a and temp_b == results_b and temp_c == results_c,
    )

    print("Time saved by multi processing:", time_taken_sp - time_taken_mp)

    exit()
