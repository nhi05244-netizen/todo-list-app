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

# Danh sách công việc (mỗi công việc là một dictionary)
tasks = []

# Hàm thêm công việc mới
def add_task(task_name):
    tasks.append({'name': task_name, 'completed': False})

# Hàm đánh dấu công việc là hoàn thành
def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print(f"✅ Đã hoàn thành: {tasks[task_index]['name']}")
    else:
        print("⚠️ Chỉ số công việc không hợp lệ.")

# Hàm hiển thị danh sách công việc
def list_tasks():
    if not tasks:
        print("Hiện không có công việc nào.")
    else:
        print("Danh sách công việc:")
        for i, task in enumerate(tasks, start=1):
            status = "[x]" if task['completed'] else "[ ]"
            print(f"{i}. {status} {task['name']}")

# Chương trình chính
if __name__ == "__main__":
    add_task("Học bài Git")
    add_task("Làm bài tập Python")

    list_tasks()
    print()

    # Đánh dấu công việc thứ 2 (index = 1) là hoàn thành
    complete_task(1)
    print()

    list_tasks()
