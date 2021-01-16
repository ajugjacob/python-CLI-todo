#Importing required libraries
import sys
import datetime
import os


#Create required files
def create():
    open(todo_path, "x")
    open(done_path, "x")


#Add a new todo
def add(n):
    f = open(todo_path, "a")
    f.write(f"{n}\n")
    print(f"Added todo: \"{n}\"")


#Show remaining todos
def show():
    new_lines=[]
    with open(todo_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            new_lines.append(line[:-1])
    if new_lines == []:
        print("There are no pending todos!")
    for i in reversed(range(len(new_lines))):
        print(f"[{i+1}] {new_lines[i]}")


#Delete a todo
def delete(n):
    with open(todo_path, "r") as f:
        lines = f.readlines()
    if int(n) != 0 and int(n)<=len(lines):
        lines.pop(int(n)-1)
        with open(todo_path, "w") as f:
            f.writelines(lines)
        print(f"Deleted todo #{n}")
    else:
        print(f"Error: todo #{n} does not exist. Nothing deleted.")
    

#Complete a todo
def completed(n):
    with open(todo_path, "r") as f:
        lines = f.readlines()
    if int(n) != 0 and int(n)<=len(lines):
        done = lines[int(n)-1]
        lines.pop(int(n)-1)
        with open(todo_path, "w") as f:
            f.writelines(lines)
        with open(done_path, "a") as f:
            f.write(f"x {datetime.date.today()} {done}")
        print(f"Marked todo #{n} as done.")
    else:
        print(f"Error: todo #{n} does not exist.")


#Show usage
def usage():
    print('''Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statisticss''')

#HTML
def html():
    with open (todo_path, "r") as f1:
        print("<ul>")
        lines = f1.readlines()
        for line in lines:
            print(f"<li> {line.strip()} </li>")
        print("</ul>\n")
    
    with open (done_path, "r") as f2:
        print("<ul>")
        lines = f2.readlines()
        for line in lines:
            print(f"<li> {line.strip()} </li>")
        print("</ul>")

#Statistics
def report():
    with open(todo_path, "r") as f1:
        lines_pending = f1.readlines()
        with open(done_path, "r") as f2:
            lines_completed = f2.readlines()
    print(f"{datetime.date.today()} Pending : {len(lines_pending)} Completed : {len(lines_completed)}")
    

#Driver code
if __name__ == '__main__':
    #Getting the Present Working Directory
    OUTDIR = os.getcwd()
    done_path = os.path.join(OUTDIR, 'done.txt')
    todo_path = os.path.join(OUTDIR, 'todo.txt')
    try:
        create()
    except:
        pass
    try:
        if sys.argv[1] == 'add':
            try:
                add(sys.argv[2])
            except:
                print("Error: Missing todo string. Nothing added!")
        elif sys.argv[1] == 'ls':
            show()
        elif sys.argv[1] == 'del':
            try:
                delete(sys.argv[2])
            except:
                print("Error: Missing NUMBER for deleting todo.")
        elif sys.argv[1] == 'done':
            try:
                completed(sys.argv[2])
            except:
                print("Error: Missing NUMBER for marking todo as done.")
        elif sys.argv[1] == 'help':
            usage()
        elif sys.argv[1] == 'report':
            report()
        elif sys.argv[1] == 'html':
            html()

    except:
        usage()