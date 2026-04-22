from class_book import Book
import json
import os

book_list=[]
current_dir = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(current_dir, "book.json")

def load_data_from_file():
    global book_list
    try:
        with open(file_name,"r",encoding="utf-8") as f:
            data_list=json.load(f)

        book_list=[]
        for data in data_list:
            book=Book.from_dict(data)
            book_list.append(book)

        print("数据已加载")

    except FileNotFoundError:
        book_list=[]
        print("未找到文件，数据初始化完成")

    except Exception as e:
        book_list=[]
        print(f"数据加载异常，{e}")

def save_data_to_file():
    data_list=[]
    try:
        for book in book_list:
            data=Book.to_dict(book)
            data_list.append(data)
        with open(file_name,"w",encoding="utf-8") as f:
            json.dump(data_list,f,ensure_ascii=False, indent=4)
        return True

    except Exception:
        print("文件保存失败")
        return False

def get_same_category(name : str , author : str ):
    return[b for b in book_list  if b.name ==name and b.author == author]

def add_book(new_id : str , name : str ,author : str):
    for b in book_list:
        if b.book_id == new_id:
            print("不可录入相同ID的书目")
            return False

    same_category = get_same_category ( name , author )
    count_of_same = len(same_category)+1

    for b in book_list:
        if b.name == name and b.author == author:
            b.count = count_of_same

    book = Book(new_id , name , author , count_of_same)
    book_list.append(book)
    save_data_to_file()
    return True

def del_book(goal_book_id : str):
    for i , b in enumerate(book_list):
        if b.book_id == goal_book_id:
            same_category = get_same_category(b.name, b.author)
            count_of_same = len(same_category) - 1

            for b2 in book_list:
                if b2.name == b.name and b2.author==b.author:
                           b2.count = count_of_same
            del book_list[i]
            save_data_to_file()
            print ("删除成功")
            return True

    print("删除失败，未找到对应编号图书")
    return False

def show_all_books():
    if len(book_list)==0:
        print("当前书库为空")
        return False

    print(f"{'图书编号':<10}{'书名':<20}{'作者':<15}{'库存':<8}")

    for b in book_list:
        print(f"{b.book_id:<10}{b.name:<20}{b.author:<15}{b.count:<8}")

    print("The end of the list")
    print("任务已完成")
    return True

def search_book(goal_name : str):
    result_list=[]
    for i , b in enumerate(book_list):
        if goal_name in b.name:
            result_list.append(book_list[i])

    if len(result_list) == 0:
        print("抱歉，未找到对应图书")
        return False

    print("搜索成功，结果如下：")
    print(f"{'图书编号':<10}{'书名':<20}{'作者':<15}{'库存':<8}")
    for b in result_list:
        print(f"{b.book_id:<10}{b.name:<20}{b.author:<15}{b.count:<8}")
    print("The end of the list")
    return True

def sort_by_author():
    if not book_list:
        print("列表为空")
        return
    book_list.sort(key=lambda x : x .author )
    save_data_to_file()
    print("已完成按作者升序排序，以下为排序后内容：")
    show_all_books()


def sort_by_name():
    if not book_list:
        print("列表为空")
        return
    book_list.sort(key=lambda x: x.name)
    save_data_to_file()
    print("已完成按书名升序排序，以下为排序后内容：")
    show_all_books()
