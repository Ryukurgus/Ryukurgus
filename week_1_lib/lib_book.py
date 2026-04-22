from class_book import Book
import json
from book_data import *  # 假设你的功能文件名为 book_data.py

def show_menu():
    print("\n======= 图书管理系统 =======")
    print("1. 添加图书")
    print("2. 删除图书")
    print("3. 显示所有图书")
    print("4. 搜索图书")
    print("5. 按作者排序")
    print("6. 按书名排序")
    print("0. 退出")
    print("============================")

def main():
    load_data_from_file()
    while True:
        show_menu()
        choice = input("请输入操作序号：")

        if choice == "1":
            print("\n----- 添加图书 -----")
            new_id = input("请输入图书编号：")
            name = input("请输入书名：")
            author = input("请输入作者：")
            add_book(new_id, name, author)

        elif choice == "2":
            print("\n----- 删除图书 -----")
            goal_book_id = input("请输入要删除的图书编号：")
            del_book(goal_book_id)

        elif choice == "3":
            print("\n----- 显示所有图书 -----")
            show_all_books()

        elif choice == "4":
            print("\n----- 搜索图书 -----")
            goal_name = input("请输入要搜索的书名：")
            search_book(goal_name)

        elif choice == "5":
            print("\n----- 按作者排序 -----")
            sort_by_author()

        elif choice == "6":
            print("\n----- 按书名排序 -----")
            sort_by_name()

        elif choice == "0":
            print("退出系统，再见！")
            break
        else:
            print("输入序号无效，请重新输入！")

if __name__ == "__main__":
    main()