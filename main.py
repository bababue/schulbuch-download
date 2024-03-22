import sys
import os
sys.path.append("./modules")
if not os.path.exists("output"):
        os.makedirs("output")


if __name__ == "__main__":

    print("[1]: Westermann Verlag (BiBox2)") #westermann
    print("[2]: Merkur Verlag Rinteln (Merkur Medien)") #merkur
    print()
    
    providernumber = input("Please choose desired provider: (Enter number 1-2): ")
    
    def askcredentials():
        global email
        global password
        email = input("Email: ")
        password = input("Password: ")
    
    match providernumber:
        case "1":
            askcredentials()
            bookid = int(input("BookId: "))
            lastpage = int(input("Last Page: "))
            import westermann
            westermann.download(email, password, bookid, lastpage)
            westermann.merge()
        case "2":
            askcredentials()
            bookid = input("BookId: ")
            lastpage = int(input("Last Page: "))
            import merkurmedien
            merkurmedien.download(email, password, bookid, lastpage)
            merkurmedien.merge()
        case _:
            print(f"Your input was invalid. Please try again")