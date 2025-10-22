# 导入 app 目录下的 app.py 中的 dedupe_header 函数
# 为了让 Python 找到 app 模块，项目根目录可能需要被添加到 PYTHONPATH
# pytest 会自动处理这个问题，但为了代码清晰，我们假设它可被导入
import sys
import os

# 将项目根目录添加到 Python 路径中
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.app import dedupe_header, calculate_total_length # 导入新函数

def test_unique_columns():
    """测试没有重复列的情况"""
    assert dedupe_header(["id", "name", "age"]) == ["id", "name", "age"]

def test_all_duplicate_columns():
    """测试所有列都重复的情况"""
    assert dedupe_header(["id", "id", "id"]) == ["id", "id.1", "id.2"]

def test_mixed_columns():
    """测试混合重复和唯一列的情况"""
    cols = ["id", "name", "id", "name", "name"]
    expected = ["id", "name", "id.1", "name.1", "name.2"]
    assert dedupe_header(cols) == expected

def test_empty_list():
    """测试输入为空列表的情况"""
    assert dedupe_header([]) == []

def test_with_trailing_duplicates():
    """测试末尾有重复项的情况"""
    assert dedupe_header(["a", "b", "c", "c", "c"]) == ["a", "b", "c", "c.1", "c.2"]

def test_calculate_total_length_normal():
    """测试计算总长度的正常情况"""
    assert calculate_total_length(["id", "name", "email"]) == 11

def test_calculate_total_length_empty():
    """测试计算总长度的空列表情况"""
    assert calculate_total_length    
