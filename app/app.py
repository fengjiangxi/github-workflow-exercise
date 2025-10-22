from typing import List

# FIX: 在函数定义前增加一个空行，满足 E302 (需要两个空行)
def dedupe_header(columns: List[str]) -> List[str]:
    """
    通过向重复项附加数字后缀来使标题列名称唯一。

    规则:
    - 名称的第一次出现保持原样。
    - 同一名称的第 2、3 次出现会附加 ".1", ".2", ...
    - 顺序与给定完全一致。
    - 输入是字符串列表（列名）；输出是等长的列表。

    示例:
        ["id", "name", "id", "name", "name"] ->
        ["id", "name", "id.1", "name.1", "name.2"]
    """
    # FIX: 长字符串被拆分成了多行，以满足 E501 (行长度限制)
    counts = {}
    new_columns = []
    for col in columns:
        if col in counts:
            counts[col] += 1
            new_columns.append(f"{col}.{counts[col]}")
        else:
            counts[col] = 0
            new_columns.append(col)
    return new_columns


# FIX: 在函数定义前增加一个空行，满足 E302
def calculate_total_length(columns: List[str]) -> int:
    """计算列表中所有字符串的总长度"""
    return sum(len(col) for col in columns)


# FIX: 在 if __name__ 前增加一个空行，满足 E305
if __name__ == "__main__":
    header = ["id", "name", "value", "id", "value", "name", "id"]
    new_header = dedupe_header(header)
    print(f"Original header: {header}")
    print(f"Deduplicated header: {new_header}")
