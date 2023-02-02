countries = ['France', 'Albania', 'Germany', 'Belgium', 'Qatar', 'Italy', 'Japan', 'China']

countries[4] = 'Portugal'
print(countries)

countries.append('Pakistan')
print(f"\n{countries}")

countries.insert(0, 'India')
print(f"\n{countries}")

del countries[0]
print(f"\n{countries}")

too_far_away = countries.pop(-2)
print(f"\n{too_far_away}")

countries.remove('Belgium')
print(f"\n{countries}")

print(f"\n{sorted(countries)}")

countries.sort()
print(f"\n{countries}")

countries.reverse()
print(f"\n{countries}")

print(len(countries))
