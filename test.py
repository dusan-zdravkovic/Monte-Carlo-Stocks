print("Hello Dusan")

# for i in range(20):
#     print("Dusan Rocks" + 1)

for i in range(20):
    print(f"Dusan Rocks {i+1}")


# watch

i = 1
while i <= 20:
    print(f"Dusan Rocks {i}")
    i += 1


def print_message(times):
    for i in range(1, times + 1):
        print(f"Dusan Rocks {i}")


print_message(10)
