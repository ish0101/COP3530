import airlines

def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

if __name__ == '__main__':
    airports = airlines.get_airports()
    print(airports[0]["Airport"]["Code"])
