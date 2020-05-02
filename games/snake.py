# snake game using python by Ali-Aref Mohammadi
import random
import curses

cur = curses.initscr()
curses.curs_set(0)
curHeight, curWidth = cur.getmaxyx()
window = curses.newwin(curHeight, curWidth, 0, 0)
window.keypad(1)
window.timeout(100)

snake_x = curWidth // 4
snake_y = curHeight // 2
snake = [[snake_y, snake_x], [snake_y, snake_x - 1], [snake_y, snake_x - 2]]

food = [curHeight // 2, curWidth // 2]
window.addch(food[0], food[1], "O")
key = curses.KEY_RIGHT

while True:
    try:
        next_key = window.getch()
    # on keyboard interrupt
    except:
        curses.endwin()
        quit()

    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, curHeight] or snake[0][1] in [0, curWidth] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
            new_food = [
                random.randint(1, curHeight - 1),
                random.randint(1, curWidth - 1),
            ]
            food = new_food if new_food not in snake else None
        window.addch(food[0], food[1], "O")
    else:
        tail = snake.pop()
        window.addch(int(tail[0]), int(tail[1]), " ")
        window.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
