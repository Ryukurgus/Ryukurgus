import re

#逻辑：
#收尾去空格是为了防止用户误触
#打印是为了让用户更好的知道本次操作的结果

def clean_text(text: str) -> str:
    """统一去空格工具"""
    return text.strip() if text else ""

def is_book_list_empty(book_list: list) -> bool:
    """判断书库是否为空，统一提示"""
    if not book_list:
        print("当前书库为空")
        return True
    return False

def print_book_table(books: list):
    """统一打印图书表格工具（显示、搜索、排序共用）"""
    if not books:
        print("当前无图书数据")
        return

    print(f"{'图书编号':<10}{'书名':<20}{'作者':<15}{'库存':<8}")
    for b in books:
        print(f"{b.book_id:<10}{b.name:<20}{b.author:<15}{b.count:<8}")
    print("The end of the list")
    print("任务已完成")

def validate_input(new_id: str, name: str, author: str) -> bool:
    """统一输入校验工具（ID、书名、作者合法性）"""
    new_id = clean_text(new_id)
    name = clean_text(name)
    author = clean_text(author)

    if not new_id:
        print("添加失败：图书编号不能为空！")
        return False
    if not re.fullmatch(r'^[a-zA-Z0-9]+$', new_id):
        print("添加失败：图书编号不合法！仅允许字母、数字")
        return False
    if not name or not re.fullmatch(r'^[\u4e00-\u9fa5a-zA-Z ]+$', name):
        print("添加失败：书名不合法！")
        return False
    if not author or not re.fullmatch(r'^[\u4e00-\u9fa5a-zA-Z ]+$', author):
        print("添加失败：作者不合法！")
        return False
    return True