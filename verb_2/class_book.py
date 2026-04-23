class Book:
    def __init__(self, book_id: str, name: str, author : str ,count : int):
        self.book_id = book_id
        self.name = name
        self.author = author
        self.count =count

    def to_dict(self):#转字典
        return{
            "book_id":self.book_id,
            "name":self.name,
            "author":self.author,
            "count":self.count
        }

    @staticmethod
    def from_dict(data : dict):#转对象
        return Book(
            book_id = data["book_id"],
            name = data["name"],
            author = data["author"],
            count = data["count"]
        )