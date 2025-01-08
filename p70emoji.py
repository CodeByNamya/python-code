import emoji
print(emoji.emojize(":thumbs_up:"))
print(emoji.emojize("I love Python! :snake:"))
option=input("enter you mood->").lower()
if option=="happy":
    print("\U0001F600")
elif option=="sad":
    print(emoji.emojize("\U0001F62A"))
