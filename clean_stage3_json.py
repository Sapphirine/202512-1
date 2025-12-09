import json
import os

VIDEO_DIR = "datasets/stage3/videos"
JSON_PATH = "datasets/stage3/video_instruct_data.json"
OUTPUT_JSON = "datasets/stage3/video_instruct_data_clean.json"

def main():
    print("🚀 开始清洗 Stage 3 JSON...")
    # 1. 扫描本地视频 ID
    existing_ids = set()
    for f in os.listdir(VIDEO_DIR):
        if f.endswith(('.mp4', '.mkv', '.webm')):
            existing_ids.add(os.path.splitext(f)[0])
    print(f"✅ 本地视频数: {len(existing_ids)}")

    # 2. 读取全量 JSON
    with open(JSON_PATH, 'r') as f:
        data = json.load(f)

    # 3. 过滤：只保留本地有的
    clean_data = []
    for item in data:
        # 兼容不同的键名情况
        vid = item.get("video_id") or item.get("video_name") or item.get("image_id")
        if vid in existing_ids:
            clean_data.append(item)

    # 4. 保存
    with open(OUTPUT_JSON, 'w') as f:
        json.dump(clean_data, f)
    print(f"🎉 清洗完毕！有效数据: {len(clean_data)} 条。已保存至 {OUTPUT_JSON}")

if __name__ == "__main__":
    main()