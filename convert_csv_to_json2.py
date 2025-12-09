import pandas as pd
import json
import os

# 读取 CSV
csv_path = 'datasets/stage3/video_instruct_data.csv'
df = pd.read_csv(csv_path)

json_data = []

# 遍历每一行
for index, row in df.iterrows():
    # 获取视频ID
    vid = str(row['video_id']).strip()
    
    # 获取问题和答案
    question = str(row['q']).strip()
    answer = str(row['a']).strip()

    # 【关键修改】这里改回代码喜欢的 "q" 和 "a"
    entry = {
        "video_id": vid,
        "q": question,      # 之前写的是 "instruction"，现在改回 "q"
        "a": answer,        # 之前写的是 "answer"，现在改回 "a"
        "length": 100
    }
    json_data.append(entry)

# 覆盖保存为 JSON
output_path = 'datasets/stage3/video_instruct_data.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=4)

print(f"转换完成！已重新生成符合代码要求的 JSON。")