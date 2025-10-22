import os
import sys

# FIX (E402): 将所有 import 语句移到文件顶部
# FIX (E128): 重构了 sys.path 操作，使其更清晰且符合代码规范
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, PROJECT_ROOT)

from app.app import calculate_total_length, dedupe_header

# FIX (F401): 删除了未使用的 'from typing import List'
# 我们将在下面的类型提示中使用现代的 'list[str]' 语法

# FIX (E302): 确保所有测试函数之间有两个空行

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
    source = ["a", "b", "c", "c", "c"]
    expected = ["a", "b", "c", "c.1", "c.2"]
    assert dedupe_header(source) == expected


def test_calculate_total_length_normal():
    """测试计算总长度的正常情况"""
    assert calculate_total_length(["id", "name", "email"]) == 11


def test_calculate_total_length_empty():
    """测试计算总长度的空列表情况"""
    assert calculate_total_length
