class Book:
    def __init__(self,id,name,quality):
        self.id=id
        self.name=name
        self.quanity=quality
    
class User:
    def __init__(self,id,name,password):
        self.id=id
        self.name=name
        self.password=password
        self.borrworsbook=[]
        self.returnbook=[]
class Library():
    def __init__(self, name, password):
        self.name=name
        self.users=[]
        self.books=[]
        
    def addBook(self,id,name,q):
        
        for book in self.books:
            if book.id==id:
                print("Book alradi exists with in id")
                return
            
        book=Book(id,name,q)
        self.book.append(book)
        print(f"Book: {book.name} added sucessfully")
    
    def added_User(self,id,name,p):
        
        for user in self.users:
            if user.id==id:
                print("User already exist")
        
        user=User(id,name,p)
        self.users.append(user)    
        print(f"User:{user.name} Added such successfully")
    
    def borrowBook(self,user,BookId):
        
            for book in self.books:
                if book.id==BookId:
                    if book in user.borrworsbook:
                        print(f"Already Brrowrs")
                        return
                    elif book.quanity<1:
                        print("No available cpies")
                    else:
                        user.borrworsbook.append(book)
                        book.quanity-=1
                        print("brrows successfully")
                        return
            print(f"Not found any book id :{BookId}")
    
    
    def returnBook(self,user,BookId):
        
            for book in self.books:
                if book.id==BookId:
                    if book in user.borrworsbook:
                        book.quanity+=1
                        print(f"Already Brrowrs")
                        return
                    else:
                         
                        print("you did not borrw this book ")
                        return
            print(f"Not found any book id :{BookId}")