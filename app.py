# Danh sách để lưu các công việc
tasks = []
def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    tasks.append(task_name)
    print(f"Đã thêm công việc: '{task_name}'")
#--- Điểm bắt đầu của chương trình ---
if __name__=="__main__":
    print("Chào mừng đến với ứng dụng To-Do-List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")

def list_tasks():
    if tasks:
        print("Danh sách công việc:")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")
    else:
        print("Hiện không có công việc nào.")
