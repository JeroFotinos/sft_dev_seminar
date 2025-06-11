def filter_and_sort(temps, threshold):
    # list.sort() works in-place and returns None
    filtered = [t for t in temps if t > threshold]
    sorted_temps = filtered.sort()   # ← returns None!
    return sorted_temps

if __name__ == "__main__":
    temps = [23.1, 19.5, 21.7, 25.0]
    print(filter_and_sort(temps, 20))

# # The correct code would be
# def filter_and_sort(temps, threshold):
#     filtered = [t for t in temps if t > threshold]
#     filtered.sort()
#     return filtered
