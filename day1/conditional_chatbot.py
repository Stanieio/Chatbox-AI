user=input("you:").lower()
bot=""  #response variable
if user=="hi":
    bot = "hello"
elif user =="hello":
    bot ="hello, how may i help u ?"
elif user =="name":
    bot="i am simple chatbot"
elif user=="bye":
    bot="good bye have a geat day"
else:
    bot="i dont understand"
print("BOT:",bot)