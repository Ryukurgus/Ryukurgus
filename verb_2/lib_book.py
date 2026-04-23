from book_data import (
    load_data_from_file,
    add_book,
    del_book,
    show_all_books,
    search_book,
    sort_by_name,
    sort_by_author
)

def show_menu():
    print("\n======= 图书管理系统 =======")
    print("1. 添加图书")
    print("2. 删除图书")
    print("3. 显示所有图书")
    print("4. 按书名搜索图书")
    print("5. 按书名排序")
    print("6. 按作者排序")
    print("0. 退出系统")
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
            book_id = input("请输入要删除的图书编号：")
            del_book(book_id)

        elif choice == "3":
            print("\n----- 显示所有图书 -----")
            show_all_books()

        elif choice == "4":
            print("\n----- 按书名搜索 -----")
            name = input("请输入书名：")
            search_book(name)

        elif choice == "5":
            sort_by_name()

        elif choice == "6":
            sort_by_author()

        elif choice == "0":
            print("感谢使用，再见！")
            break
        else:
            print("输入无效，请重新输入！")

if __name__ == "__main__":
    main()