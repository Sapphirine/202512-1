import json
import os

# === 配置路径 ===
# 视频所在的文件夹
video_dir = 'datasets/stage3/videos'
# 原始 JSON 文件路径
json_path = 'datasets/stage3/video_instruct_data.json'

def filter_data():
    print(f"正在扫描视频文件夹: {video_dir} ...")
    
    if not os.path.exists(video_dir):
        print(f"错误: 找不到视频文件夹 {video_dir}")
        return

    # 1. 获取所有存在的视频 ID (去掉文件名后缀，比如 .mp4)
    existing_video_ids = set()
    files = os.listdir(video_dir)
    for f in files:
        # 跳过隐藏文件
        if f.startswith('.'):
            continue
        # 获取文件名作为 ID (例如 v_xyz.mp4 -> v_xyz)
        vid_id = os.path.splitext(f)[0]
        existing_video_ids.add(vid_id)
    
    print(f"找到 {len(existing_video_ids)} 个视频文件。")

    # 2. 读取原始 JSON
    print(f"正在读取 JSON: {json_path} ...")
    if not os.path.exists(json_path):
        print(f"错误: 找不到 JSON 文件 {json_path}")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    original_count = len(data)
    print(f"原始 JSON 包含 {original_count} 条数据。")

    # 3. 进行过滤
    filtered_data = []
    for item in data:
        # 获取 JSON 里的 video_id
        vid = item.get('video_id')
        # 检查是否在刚才扫描的集合里
        if vid in existing_video_ids:
            filtered_data.append(item)
    
    filtered_count = len(filtered_data)
    print(f"过滤后剩余 {filtered_count} 条数据 (剔除了 {original_count - filtered_count} 条)。")

    # 4. 覆盖保存
    if filtered_count > 0:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(filtered_data, f, indent=4)
        print("✅ JSON 文件已更新！现在可以开始训练了。")
    else:
        print("⚠️ 警告: 过滤后数据为空！请检查视频文件夹路径是否正确，或视频文件名是否与 JSON 中的 ID 匹配。")

if __name__ == "__main__":
    filter_data()