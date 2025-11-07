def collect_data():
    observations = []
    counts = []

    while True:
        name = input("Observation:")
        if name == "":
            break
        count = int(input("Found:"))
        observations.append(name)
        counts.append(count)

    return observations, counts



if __name__ == "__main__":
    observ, counting = collect_data()
    print(observ)
    print(counting)
