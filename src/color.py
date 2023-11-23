# COLOR ESCAPE SEQUENCE INFO
# \x1b[38;5;{code}m - sets text color to {code}
# \x1b[1;5;{code}m - sets text color to {code} and makes it bold
# \x1b[3;5;{code}m - sets text color to {code} and makes it italic
# more info found here (scroll down a bit):
# https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797


class COLOR:
        RED = "\x1b[38;5;160m"
        DARKRED = "\x1b[38;5;88m"
        ORANGE = "\x1b[38;5;208m"
        YELLOW = "\x1b[38;5;226m"
        LIGHTGREEN = "\x1b[38;5;46m"
        GREEN = "\x1b[38;5;28m"
        LIGHTBLUE = "\x1b[38;5;45m"
        BLUE = "\x1b[38;5;26m"
        PINK = "\x1b[38;5;207m"
        PURPLE = "\x1b[38;5;93m"
        WHITE = "\x1b[38;5;15m"
        GRAY = "\x1b[38;5;239m"