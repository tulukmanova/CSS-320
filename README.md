# CSS-320
module 1 
# Multi-Level Task Manager (Task A)

## Description
This program manages a to-do list using three priority levels:
- Urgent
- Normal
- Backlog

Each priority is implemented as a FIFO queue.

## Data Structure Choice
I used Python lists to simulate queue behavior:
- Enqueue: `append(task)` adds to the end of the list
- Dequeue: `pop(0)` removes from the front of the list

This matches how a real queue works (first in, first out).

## Features
- Add tasks to a selected priority queue
- Remove (dequeue) the next task from a selected priority queue
- View tasks by priority
- View all tasks across all priorities

## How to Run
1. Save the file as `task_manager.py`
2. Run:
   ```bash
   python task_manager.py
