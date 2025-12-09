import pandas as pd
import json
import os

# ================= 配置 =================
BASE_DIR = "datasets"
METADATA_DIR = os.path.join(BASE_DIR, "CondensedMovies_Metadata")
VIDEO_DIR = os.path.join(BASE_DIR, "CondensedMovies_Videos")
OUTPUT_JSON = os.path.join(BASE_DIR, "cmd_annotations.json")
# ========================================

def main():
    print("🚀 生成标准 CMD JSON...")
    
    # 1. 读取 CSV
    df_clips = pd.read_csv(os.path.join(METADATA_DIR, "clips.csv"))
    df_desc = pd.read_csv(os.path.join(METADATA_DIR, "descriptions.csv"))
    df_merged = pd.merge(df_clips, df_desc, on="videoid", how="inner")

    # 2. 扫描本地视频 (现在它们都在根目录了，且都是 mp4)
    existing_ids = set()
    for f in os.listdir(VIDEO_DIR):
        if f.endswith(".mp4"):
            existing_ids.add(os.path.splitext(f)[0])
            
    print(f"✅ 本地找到 {len(existing_ids)} 个视频")

    # 3. 生成列表
    annotations = []
    for _, row in df_merged.iterrows():
        vid = row['videoid']
        if vid in existing_ids:
            # 只要 image_id 和 caption，完全符合原始代码要求
            annotations.append({
                "image_id": vid,
                "caption": row['description']
            })

    # 4. 保存
    with open(OUTPUT_JSON, 'w') as f:
        json.dump(annotations, f)
    print(f"🎉 JSON 生成完毕: {len(annotations)} 条数据")

if __name__ == "__main__":
    main()