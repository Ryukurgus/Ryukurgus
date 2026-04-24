from class_book import Book
from book_utils import *
import json
import os

# 全局配置
book_list = []
current_dir = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(current_dir, "book.json")

# ====================== 文件读写（纯数据操作）======================
#业务规则：1.ID唯一，即便是同一类书每个个体ID都不一样
#库存本质是在增删书目中一同更改的，所以增删书的功能中要嵌套对同一类书的判断
def load_data_from_file():
    global book_list
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            data_list = json.load(f)
        book_list = [Book.from_dict(data) for data in data_list]
        print("数据已加载")
    except FileNotFoundError:
        book_list = []
        print("未找到文件，数据初始化完成")
    except Exception as e:
        book_list = []
        print(f"数据加载异常：{e}")

def save_data_to_file():
    try:
        data_list = [Book.to_dict(b) for b in book_list]
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(data_list, f, ensure_ascii=False, indent=4)
        return True
    except Exception:
        print("文件保存失败")
        return False

# ====================== 辅助业务逻辑 ======================

#库存是同一类书的综合，所以在增删操作中要统一进行对目标数据的同类进行库存的修改

def get_same_category(name: str, author: str):
    name = clean_text(name)
    author = clean_text(author)
    return [b for b in book_list if clean_text(b.name) == name and clean_text(b.author) == author]

def update_category_count(name: str, author: str):
    same_books = get_same_category(name, author)
    new_count = len(same_books)
    for b in same_books:
        b.count = new_count

# ====================== 核心业务功能 ======================
def add_book(new_id: str, name: str, author: str):
    new_id = clean_text(new_id)
    name = clean_text(name)
    author = clean_text(author)

    # 调用工具层校验
    if not validate_input(new_id, name, author):
        return False

    # ID重复判断
    for b in book_list:
        if b.book_id == new_id:
            print("添加失败：图书编号已存在！")
            return False

    # 添加并更新库存
    book_list.append(Book(new_id, name, author, 0))
    update_category_count(name, author)

    if save_data_to_file():
        print("图书添加成功")
        return True
    else:
        book_list.pop()
        return False

def del_book(goal_book_id: str):
    goal_book_id = clean_text(goal_book_id)
    for i, b in enumerate(book_list):
        if b.book_id == goal_book_id:
            name, author = b.name, b.author
            del book_list[i]
            update_category_count(name, author)
            save_data_to_file()
            print("删除成功")
            return True
    print("删除失败，未找到对应编号图书")
    return False

def show_all_books():
    if is_book_list_empty(book_list):
        return False
    print_book_table(book_list)
    return True

def search_book(goal_name: str):
    goal_name = clean_text(goal_name).replace(" ", "")
    if not goal_name:
        print("搜索内容不能为空！")
        return False

    result = []
    for b in book_list:
        book_name = clean_text(b.name).replace(" ", "")
        # 检查用户输入的每一个字，都在书名里
        if all(char in book_name for char in goal_name):
            result.append(b)

    if not result:
        print("抱歉，未找到对应图书")
        return False

    print("搜索成功，结果如下：")
    print_book_table(result)
    return True

def sort_by_author():
    if is_book_list_empty(book_list):
        return
    book_list.sort(key=lambda x: x.author)
    save_data_to_file()
    print("已完成按作者升序排序，以下为排序后内容：")
    show_all_books()

def sort_by_name():
    if is_book_list_empty(book_list):
        return
    book_list.sort(key=lambda x: x.name)
    save_data_to_file()
    print("已完成按书名升序排序，以下为排序后内容：")
    show_all_books()