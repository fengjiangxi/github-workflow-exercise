from collections import defaultdict
from typing import List

def dedupe_header(columns: List[str]) -> List[str]:
    """
    通过向重复项附加数字后缀来使标题列名称唯一。

    规则:
    - 名称的第一次出现保持原样。
    - 同一名称的第 2、3 次出现会附加 ".1", ".2", ...
    - 顺序与给定完全一致。
    - 输入是字符串列表（列名）；输出是等长的列表。

    示例:
        ["id", "name", "id", "name", "name"] -> ["id", "name", "id.1", "name.1", "name.2"]
    """
    seen_counts = defaultdict(int)
    result: List[str] = []

    for col in columns:
        count = seen_counts[col]
        if count == 0:
            result.append(col)
        else:
            result.append(f"{col}.{count}")
        seen_counts[col] += 1

    return result

def calculate_total_length(columns: List[str]) -> int:
    """计算列表中所有字符串的总长度"""
    return sum(len(col) for col in columns)

# 主程序入口，方便直接运行查看效果
if __name__ == "__main__":
    sample_columns = ["id", "name", "id", "name", "name", "email"]
    unique_columns = dedupe_header(sample_columns)
    print(f"Original columns: {sample_columns}")
    print(f"Deduplicated columns: {unique_columns}")
