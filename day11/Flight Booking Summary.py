def display_booking(booking):
    print("\n\n======Booking Summary======\n\n")
    for book in booking:
        print("==Booking Summary For Each==")
        print("Passenger name:",book[0],
            "\nFlight Number :",book[1],
            "\nSeat Number   :",book[2],
            "\nDestination   :",book[3]
            )
        
def search_passenger(booking):
    name=input("Enter passenger name to search booking :")
    for book in booking:
        if book[0]==name:
            print("Passenger name found in the booking")
            return
    print("Passenger Name Not Found in the Booking.")

def main():
    booking=(
        ("Adarsh",231,21,"Mumbai"),
        ("Vishnu",243,10,"Delhi"),
        ("James",245,31,"Kolkata")
    )

    display_booking(booking)
    search_passenger(booking)

main()