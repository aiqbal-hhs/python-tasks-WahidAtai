print("welcome to henderson pizza place")
#max 5 pizzas
pizza_type = input("what pizza would you like")
if pizza_type == regular:
   print("that would be $8.50 per pizza")
elif pizza_type == gourmet:
   print("that would be $13.50 per pizza")
pizzas_avaliable== ("Beef & Onion,Seafood Deluxe, Summer Shrimp, BBQ, Bacon & Mushroom, BBQ Hawaiian, Italiano")
 
#delivery or pickup
pick_or_delivery = input(" would you like the pizza deliverd to your house or would you like to pickup from our store").lower().strip()
no = pick_or_delivery.split(" ")
output = ""
for i in no:
    output += i

if output == "pickup":
   input("what is your name")
   input("what is your address")
   print("ok thank you very much your order will be ready in 30 minutes")
if output == "delivery":
    input("what is your name")
    input("what is your address")
print("thank you very much delivery will cost an extra $7")

