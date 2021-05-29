name1 = "Marla"
name2 = "Ron"
name3 = "Mr and Mrs Hamlin's"
event1 = "Salad Party"
date1 = input("Please enter the date you want to go:") #validate on date only entry
client1 = input("Please enter your name:")
guests = int(input("Please enter the number of guests you will be bringing: "))#if number of guests are < 0 then we need an error message.
new_total_count = guests + 100 #on the last line, we have the option to convert a this number to a string.    
bringVeg = input("Are you bringing any veggies? Choose yes/no: " ) #yes/no question here. Restrict allowable responses.
if bringVeg == "yes":
    print(input("What veggie will you bring?"))
if bringVeg == "no":
    print("That's quite alright. Please let us know if you change your mind and want to bring a veggie or a friend to the salad bar.")
if guests > 0:
    assoc = input("Are any of your guests Juiceplus associates? Please answer yes/no: ")  #yes/no question here . Restrict allowable responses.
    existingclient = int(input("How many of your guests are existing Juiceplus clients? Enter a number :")) #error to remind them to enter number only.
    if existingclient == 0:
        print("Oh good! You are bringing new faces - ") #add logic to validate total number of clients vs totalguests brought.
    elif existingclient >= 0:
        print(input("Oh good! I wonder if I know them. Please let us know which guests are existing clients (separate each name with a comma):")) #accept more than one input
    else:
        print("Can't wait to see you again ! I think this salad party will shed new light to how people think about what it means to eat healthy")
else:
    print("Can't wait to see you again! I think this salad party will shed new light to how people think about what it means to eat healthy")    

print("and", client1, "-- Looking forward to seeing you soon at the", name3[11:20],  event1, "on" , date1, "...its at the home of ", name1[3:], "&", name2[:2], "!")

#new_total_count = guests + 100
print("There will be ", str(new_total_count), "guests at the party. Get your 30 second story ready.")

