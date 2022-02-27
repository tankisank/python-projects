logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
def auction():
    string=input("what is your name")
    bid=int(input("what is your bid:$"))
    return string,bid

cond=True

dict={}
while cond:
    string,bid=auction()
    dict[string]=bid
    bidder=input("another bidder? y or n")
    if bidder=="y":
        cond=True
    else:
        cond=False
print(max(dict.values()))        
    
