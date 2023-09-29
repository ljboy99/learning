import json
#ok lets figure out how job files work
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
  
custname= input("Customer Name:\n")
shoemodel = input("Shoe Model:\n")
shoewidth = input("Shoe width:\n")
shoesize = float(input("Size:\n"))
ispaid()
didtheypay = print("Paid: "+paymentstatus)

custorder = shoemodel, shoewidth, shoesize, didtheypay

filename = {custname:custorder}
print(json.dumps(filename))
