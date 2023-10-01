import json, os

isExist = os.path.exists("current_orders")
if isExist == False:
    os.mkdir("current_orders")


paymentstatus = ""
def ispaid():
  global paymentstatus
  paymentstatus = "RETRY"
  while paymentstatus == "RETRY":
    try:
      paymentstatus = input("Paid? (Y/N)")
      if paymentstatus.upper() == "Y":
        paymentstatus = "Yes"
      elif paymentstatus.upper() == "N":
        paymentstatus = "No"
      else:
        print("Incorrect input. Try again.")
        ispaid()
    except:
      print("Something went wrong, \n please try again.")
      ispaid()
  return paymentstatus

custname = input("Customer Name\n")
custphone = input("Phone Number\n")
shoemodel = input("Shoe Model:\n")
shoewidth = input("Shoe width:\n")
shoesize = float(input("Size:\n"))
ispaid()
didtheypay = "Paid: "+paymentstatus

custorder = (custphone, shoemodel, shoewidth, shoesize, didtheypay)


filename = json.dumps({custname: custorder}, indent=2)

with open("current_orders/"+custname+"_"+shoemodel+".json", "w") as outfile:
  outfile.write(filename)
