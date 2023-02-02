sandwich_orders = ['fshati', 'pastarami','proshut', 'ton', 'pastarami', 'kerpudh', 'pastarami', 'mix']
finished_sandwiches = []


print("The deli has run out of pastarami.")

while 'pastarami' in sandwich_orders:
    sandwich_orders.remove('pastarami')


while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"Making a {current_sandwich} sandwitch right now.")
    finished_sandwiches.append(current_sandwich)

print("\n")

print("The finished sandwitches:")
for sandwitch in finished_sandwiches:
    print(f"-{sandwitch}.")
