places = ['Germany', 'Sweden', 'France', 'Luxemburg', 'Canada']

print(places)
print(sorted(places))
print(places)

print(sorted(places, reverse=True))
print(places)

places.reverse()
print(places)

places.reverse()
print(places)

places.sort()
print(places)

places.sort(reverse=True)
print(places)

print("\nThe first three items in the list are:")
for place in places[:3]:
    print(f"-{place}")

print("\nThree items from the middle are:")
for place in places[1:4]:
    print(f"-{place}")

print("The last three items in the list are:")
for place in places[-3:]:
    print(f"-{place}")
