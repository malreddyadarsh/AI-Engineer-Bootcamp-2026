def display(cricketers):
    for cric in cricketers:
        print("Cricketer's name :",cric[0],"\nTotal runs         :",cric[1],"\nAverage Score      :",cric[2],)
              
        
def highest_score(cricketers):
    high=cricketers[0][1]
    name=""
    for cric in cricketers:
        if cric[1]>high:
            high=cric[1]
            name=cric[0]
    print("Highest runs scored :", high,name)
    return name
    

def average_score(cricketers):
    for emp in cricketers:
        print("Cricketer's name :",emp[0]," Average score :",emp[2])

def main():
    cricketers=(
        ("Virat",9280,52.60),
        ("Rohit",7800,45.45),
        ("Rahul",6000,46.78),
        ("Dhoni",1200,40.60),
        ("Dhawan",7800,42.46)
    )


    display(cricketers)
    print("Highest run getter's name is :",highest_score(cricketers))
    average_score(cricketers)

main()