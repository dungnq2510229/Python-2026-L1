import curses

def get_input(stdscr, prompt):
    stdscr.clear()
    stdscr.addstr(2, 2, prompt)
    stdscr.refresh()
    curses.echo()
    val = stdscr.getstr(3, 2).decode('utf-8')
    curses.noecho()
    return val
