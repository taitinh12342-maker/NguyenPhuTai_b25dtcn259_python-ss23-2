from storage.disk_manager import calculate_disk_blocks
from storage.io_helper import safe_create_dir
from analytics.time_validator import parse_and_inspect_date

raw_files = [
    {"filename": "pod_ep1.mp3",        "size_bytes": 4500,   "duration_sec": 180, "upload_at": "2026-06-10"},
    {"filename": "movie_trailer.mp4",  "size_bytes": 105000, "duration_sec": 145, "upload_at": "2026-06-31"},
    {"filename": "clip_short.mp4",     "size_bytes": 8200,   "duration_sec": 15,  "upload_at": "2026-05-15"},
]

FILE_TYPE_MAP = {
    ".mp3": "audio",
    ".wav": "audio",
    ".mp4": "video",
    ".mkv": "video",
}

def classify_file(filename):
    extension = "." + filename.rsplit(".", 1)[-1].lower()
    return FILE_TYPE_MAP.get(extension)

print("======== HỆ THỐNG QUẢN LÝ LƯU TRỮ RIKKEI MEDIA ======")
safe_create_dir("media_vault/audio")
safe_create_dir("media_vault/video")
print("[SYSTEM] Kiểm tra hạ tầng lưu trữ... Hoàn tất.")     

total_files = len(raw_files)
success_count = 0

for file_info in raw_files:
    filename = file_info["filename"]
    print(f"\n[TỆP TIN: {filename}]")

    upload_date = parse_and_inspect_date(file_info["upload_at"])
    if upload_date is None:
        print(f"""+ Trạng thái phân loại: 🔴 THẤT BẠI 
(Lỗi: Định dạng ngày upload '{file_info['upload_at']}' không tồn tại)""")
        continue

    size_bytes = file_info["size_bytes"]
    disk_blocks = calculate_disk_blocks(size_bytes)

    print(f"+ Dung lượng thực tế: {size_bytes:,} Bytes")
    print(f"+ Số khối phân vùng (4KB Block): {disk_blocks} Blocks")

    media_folder = classify_file(filename)
    if media_folder:
        destination = f"media_vault/{media_folder}"
        safe_create_dir(destination)
        print(f"+ Trạng thái phân loại: 🟢 HỢP LỆ (Lưu trữ vào thư mục '{media_folder}')")
        success_count += 1
    else:
        print(f"+ Trạng thái phân loại: 🔴 THẤT BẠI (Lỗi: Định dạng tệp không được hỗ trợ)")
print(f"TIẾN ĐỘ QUÉT: Hoàn thành xử lý {success_count}/{total_files} tệp tin thành công. Hệ thống ổn định.")
