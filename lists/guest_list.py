guests = ['Denis', 'Miri', 'Eni', 'Ani', 'Alex']

# Sending invitations
name = guests[0].title()
print(f"{name} you are invited to dinner.")

name = guests[1].title()
print(f"{name} you are invited to dinner.")

name = guests[2].title()
print(f"{name} you are invited to dinner.")

name = guests[3].title()
print(f"{name} you are invited to dinner.")

name = guests[4].title()
print(f"{name} you are invited to dinner.")


# A guest can't make it, replacing him
name = guests[1].title()
print(f"\n{name} can't make it to the dinner.")
del guests[1]
guests.insert(1, 'Odi')


# Re-inviting
name = guests[0].title()
print(f"\n{name} you are invited to dinner.")

name = guests[1].title()
print(f"{name} you are invited to dinner.")

name = guests[2].title()
print(f"{name} you are invited to dinner.")

name = guests[3].title()
print(f"{name} you are invited to dinner.")

name = guests[4].title()
print(f"{name} you are invited to dinner.")

print(f"\nI found a bigger table baby.\n")

guests.insert(0, 'Jonis')
guests.insert(3, 'Kliton')
guests.append('Leonora')

print(guests)

# Reinving again
name = guests[0].title()
print(f"\n{name} you are invited to dinner.")

name = guests[1].title()
print(f"{name} you are invited to dinner.")

name = guests[2].title()
print(f"{name} you are invited to dinner.")

name = guests[3].title()
print(f"{name} you are invited to dinner.")

name = guests[4].title()
print(f"{name} you are invited to dinner.")

name = guests[5].title()
print(f"{name} you are invited to dinner.")

name = guests[6].title()
print(f"{name} you are invited to dinner.")

name = guests[7].title()
print(f"{name} you are invited to dinner.")

print(len(guests))
print("\nI can only invite two people.")

removed_guest = guests.pop()
print(f"{removed_guest.title()} I'm sorry I can't invite you to dinner.")

removed_guest = guests.pop()
print(f"{removed_guest.title()} I'm sorry I can't invite you to dinner.")

removed_guest = guests.pop()
print(f"{removed_guest.title()} I'm sorry I can't invite you to dinner.")

removed_guest = guests.pop()
print(f"{removed_guest.title()} I'm sorry I can't invite you to dinner.")

removed_guest = guests.pop()
print(f"{removed_guest.title()} I'm sorry I can't invite you to dinner.")

removed_guest = guests.pop()
print(f"{removed_guest.title()} I'm sorry I can't invite you to dinner.\n")

name = guests[0].title()
print(f"{name} you're still invited.")

name = guests[1].title()
print(f"{name} you're still invited.")

del guests[0]
del guests[0]
print(guests)

