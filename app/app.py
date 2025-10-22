from typing import List


# FIX: 再次确保函数定义前有两个空行
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


def calculate_total_length(columns: List[str]) -> int:
    """计算列表中所有字符串的总长度"""
    return sum(len(col) for col in columns)


if __name__ == "__main__":
    header = ["id", "name", "value", "id", "value", "name", "id"]
    new_header = dedupe_header(header)
    print(f"Original header: {header}")
    print(f"Deduplicated header: {new_header}")

