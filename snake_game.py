import curses
import random

# Ekranı başlat
stdscr = curses.initscr()
curses.curs_set(0)  # imleci gizle
h, w = stdscr.getmaxyx()
win = curses.newwin(h, w, 0, 0)
win.keypad(1)
win.timeout(100)  # 100ms'de bir ekran yenile

# Yılanın başlangıç pozisyonu
snake = [
    [h//2, w//4],
    [h//2, w//4 - 1],
    [h//2, w//4 - 2]
]

# Yön
key = curses.KEY_RIGHT

# Yem
food = [random.randint(1, h-2), random.randint(1, w-2)]
win.addch(food[0], food[1], '*')

# Oyun döngüsü
while True:
    next_key = win.getch()
    key = key if next_key == -1 else next_key

    head = snake[0]
    if key == curses.KEY_DOWN:
        new_head = [head[0]+1, head[1]]
    elif key == curses.KEY_UP:
        new_head = [head[0]-1, head[1]]
    elif key == curses.KEY_LEFT:
        new_head = [head[0], head[1]-1]
    elif key == curses.KEY_RIGHT:
        new_head = [head[0], head[1]+1]
    else:
        continue

    snake.insert(0, new_head)

    # Çarpışma kontrolü
    if (
        new_head[0] in [0, h] or
        new_head[1] in [0, w] or
        new_head in snake[1:]
    ):
        curses.endwin()
        print("OYUN BİTTİ! Skor:", len(snake) - 3)
        break

    if new_head == food:
        food = None
        while food is None:
            nf = [random.randint(1, h-2), random.randint(1, w-2)]
            if nf not in snake:
                food = nf
        win.addch(food[0], food[1], '*')
    else:
        tail = snake.pop()
        win.addch(tail[0], tail[1], ' ')

    win.addch(new_head[0], new_head[1], '#')
