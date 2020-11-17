from memory_profiler import profile


# @profile
def use_huge_memory():
    print("start use_huge_memory")
    huge_list = list(range(10000000))
    # del huge_list
    print("finish use_huge_memory")


@profile
def step():
    print("start step")
    use_huge_memory()
    print("finish step")


if __name__ == "__main__":
    step()
