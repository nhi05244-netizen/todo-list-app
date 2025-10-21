# Danh sách công việc (mỗi công việc là một dictionary)
tasks = []

# Hàm thêm công việc mới
def add_task(task_name):
    tasks.append({'name': task_name, 'completed': False})

# Hàm hiển thị danh sách công việc
def list_tasks():
    if not tasks:
        print("Hiện không có công việc nào.")
    else:
        print("Danh sách công việc:")
        for i, task in enumerate(tasks, start=1):
            status = "[x]" if task['completed'] else "[ ]"
            print(f"{i}. {status} {task['name']}")

# Hàm đánh dấu công việc là hoàn thành
def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print(f"Đã hoàn thành: {tasks[task_index]['name']}")
    else:
        print("Chỉ số công việc không hợp lệ.")
        
if __name__ == "__main__":
    add_task("Học bài Git")
    add_task("Làm bài tập Python")

    list_tasks()
    print()

    complete_task(1)
    print()

    list_tasks()
main
