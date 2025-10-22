import os
import sys
from typing import List

# FIX: 将所有 import 语句移动到文件顶部，修复 E402
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                               '..')))
from app.app import calculate_total_length, dedupe_header


# FIX: 确保函数间有两个空行，修复 E302
def test_unique_columns():
    """测试所有列都唯一的情况"""
    assert dedupe_header(["id", "name", "email"]) == ["id", "name", "email"]


def test_all_duplicate_columns():
    """测试所有列都相同的情况"""
    assert dedupe_header(["a", "a", "a"]) == ["a", "a.1", "a.2"]


def test_mixed_columns():
    """测试混合唯一和重复列的情况"""
    source = ["id", "name", "id", "value", "name", "id"]
    expected = ["id", "name", "id.1", "value", "name.1", "id.2"]
    assert dedupe_header(source) == expected


def test_empty_list():
    """测试输入为空列表的情况"""
    assert dedupe_header([]) == []


def test_with_trailing_duplicates():
    """测试重复项在末尾的情况"""
    # FIX: 长行被拆分，修复 E501
    source = ["a", "b", "c", "c", "c"]
    expected = ["a", "b", "c", "c.1", "c.2"]
    assert dedupe_header(source) == expected


def test_calculate_total_length_normal():
    """测试计算总长度的正常情况"""
    assert calculate_total_length(["id", "name", "email"]) == 11


def test_calculate_total_length_empty():
    """测试计算总长度的空列表情况"""
    # FIX: 移除了行末多余的空格，修复 W291
    assert calculate_total_length
