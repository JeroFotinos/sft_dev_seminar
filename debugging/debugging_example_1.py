def filter_and_sort(temps, threshold):
    # import ipdb; ipdb.set_trace()
    filtered = [t for t in temps if t > threshold]
    sorted_temps = filtered.sort()
    return sorted_temps

if __name__ == "__main__":
    temps = [23.1, 19.5, 21.7, 25.0]
    print(filter_and_sort(temps, 20))
