from langchain_core.tools import tool

@tool
def search(query: str):
    """模拟⼀个搜索⼯具"""
    if "上海" in query.lower() or "shanghai" in query.lower():
        return "现在30度,有雾."

    return "现在是35度,阳光明媚。"

tools = [search]