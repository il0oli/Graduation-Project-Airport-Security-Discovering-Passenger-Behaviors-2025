from video_analysis import analyze_camera

if __name__ == "__main__":
    analyze_camera()



















# from file_selection import select_file
# from video_analysis import analyze_image, analyze_video

# if __name__ == "__main__":
#     file_path = select_file()

#     if file_path:
#         print(f"✅ File selected: {file_path}")

#         if file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
#             analyze_image(file_path)
#         elif file_path.lower().endswith(('.mp4', '.avi', '.mov')):
#             analyze_video(file_path)
#         else:
#             print("⚠️ Unsupported file type!")
#     else:
#         print("❌ No file selected.")
