favorite_languages = {'Denis': 'Python',
                      'Jonis': 'C++',
                      'Toni': 'C#',
                      'Leo': 'Java',
                      }

friends = ['Denis', 'Alex', 'Jonis', 'Mira', 'Flori', 'Toni', 'Leo']

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("\n")

for friend in friends:
    if friend in favorite_languages.keys():
        print(f"Thanks for taking the poll, {friend.title()}.")
    else:
        print(f"{friend.title()},  what's your favorite language?")
