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
    """Hiển thị danh sách công việc với trạng thái."""
    if tasks:
        print("Danh sách công việc:")
        for i, task in enumerate(tasks, start=1):
            status = "[x]" if task['completed'] else "[ ]"
            print(f"{i}. {status} {task['name']}")
    else:
        print("Hiện không có công việc nào.")

def complete_task(task_index):
    """Đánh dấu một công việc là hoàn thành."""
    try:
        task = tasks[task_index]
        task['completed'] = True
        print(f"Đã hoàn thành: {task['name']}")
    except IndexError:
        print("Chỉ số công việc không hợp lệ.")

def delete_task(task_index):
    """Xóa một công việc khỏi danh sách theo chỉ số."""
    try:
        removed_task = tasks.pop(task_index)
        print(f"Đã xóa công việc: {removed_task['name']}")
    except IndexError:
        print("Chỉ số công việc không hợp lệ. Không thể xóa.")

# --- Chạy chương trình ---
if __name__ == "__main__":
    print()
    list_tasks()

    print()
    complete_task(1)

    print()
    delete_task(0)  # Xóa công việc đầu tiên

    print()
    list_tasks()