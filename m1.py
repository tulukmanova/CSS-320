"""
Multi-Level Task Manager (Task A)
Uses Python lists to simulate 3 FIFO queues:
- urgent
- normal
- backlog
"""

from typing import Dict, List

Priority = str

def enqueue(q: List[str], task: str) -> None:
    """Add a task to the end of a queue."""
    q.append(task)

def dequeue(q: List[str]) -> str | None:
    """Remove and return the next task (front of queue)."""
    if not q:
        return None
    return q.pop(0)

def show_queue(name: str, q: List[str]) -> None:
    """Display tasks in a single queue."""
    print(f"\n{name.title()} ({len(q)}):")
    if not q:
        print("  — (empty)")
    else:
        for i, task in enumerate(q, start=1):
            print(f"  {i}. {task}")

def show_all(queues: Dict[Priority, List[str]]) -> None:
    """Display tasks across all priorities."""
    print("\n=== ALL TASKS ===")
    show_queue("urgent", queues["urgent"])
    show_queue("normal", queues["normal"])
    show_queue("backlog", queues["backlog"])
    print()

def get_priority() -> Priority | None:
    p = input("Priority (urgent/normal/backlog): ").strip().lower()
    if p not in {"urgent", "normal", "backlog"}:
        print("Invalid priority.\n")
        return None
    return p

def main() -> None:
    queues: Dict[Priority, List[str]] = {
        "urgent": [],
        "normal": [],
        "backlog": []
    }

    while True:
        print("=== Multi-Level Task Manager ===")
        print("1) Add task")
        print("2) Remove next task (dequeue)")
        print("3) View tasks by priority")
        print("4) View all tasks")
        print("5) Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            p = get_priority()
            if not p:
                continue
            task = input("Enter task: ").strip()
            if not task:
                print("Task cannot be empty.\n")
                continue
            enqueue(queues[p], task)
            print("Task added.\n")

        elif choice == "2":
            p = get_priority()
            if not p:
                continue
            removed = dequeue(queues[p])
            if removed is None:
                print("That queue is empty.\n")
            else:
                print(f"Removed: {removed}\n")

        elif choice == "3":
            p = get_priority()
            if not p:
                continue
            show_queue(p, queues[p])
            print()

        elif choice == "4":
            show_all(queues)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option.\n")

if __name__ == "__main__":
    main()
