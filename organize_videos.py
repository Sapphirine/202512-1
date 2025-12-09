import os
import shutil

# ================= 配置 =================
# 视频所在的根目录
VIDEO_ROOT = "datasets/CondensedMovies_Videos"
# ========================================

def main():
    print(f"🚀 开始整理视频文件: {VIDEO_ROOT}")
    
    if not os.path.exists(VIDEO_ROOT):
        print("❌ 错误：找不到视频目录！")
        return

    moved_count = 0
    
    # 1. 遍历所有子文件夹 (2019, 2020...)
    for item in os.listdir(VIDEO_ROOT):
        year_dir = os.path.join(VIDEO_ROOT, item)
        
        # 如果是文件夹 (比如 2019)，就进去找视频
        if os.path.isdir(year_dir):
            print(f"📂 正在扫描子文件夹: {item} ...")
            
            for filename in os.listdir(year_dir):
                src_path = os.path.join(year_dir, filename)
                
                # 检查是不是视频文件
                if os.path.isfile(src_path) and filename.lower().endswith(('.mp4', '.mkv', '.webm')):
                    # 获取视频ID (去掉后缀)
                    video_id = os.path.splitext(filename)[0]
                    
                    # 【关键操作】强制改名为 .mp4，并移到根目录
                    # 注意：这里只是改名，没有转码。大多数播放器和训练库(decord)都能兼容这种“伪装”的mp4
                    new_filename = f"{video_id}.mp4"
                    dst_path = os.path.join(VIDEO_ROOT, new_filename)
                    
                    # 移动文件
                    shutil.move(src_path, dst_path)
                    moved_count += 1
            
            # 搬空后，删除空的年份文件夹
            try:
                os.rmdir(year_dir)
                print(f"🗑️ 已删除空文件夹: {item}")
            except:
                pass

    print("-" * 30)
    print(f"✅ 整理完成！共移动并重命名了 {moved_count} 个视频。")
    print(f"所有视频现在都位于 {VIDEO_ROOT} 下，且后缀均为 .mp4")

if __name__ == "__main__":
    main()