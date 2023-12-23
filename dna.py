import sys
import time
from colorama import Fore, Style, init

# Initialize colorama to work on Windows as well
init()

class TextAnimation:
    def __init__(self):
        self.PAUSE = 0.50
        self.TEXT_ROWS = [
            '                                                            ',
            '  __/\\\\\\\\\\\\\\_______/\\\\\\\\\\_____/\\\\\\\\\\\\\\\\_/\\\\\\\\\\\\\\________/\\\\\\\\\\_____/\\\\\\\\\\\\\\\\\\_        ',
            ' _\\/\\\\/////////\\\\___/\\\\\\\\\\\\\\\\\\__\\/////////////\\\\_\\/\\\\////////\\\\\\____/\\\\\\\\\\\\\\\\\\__\\/////////////\\\\_       ',
            '  _\\/\\\\_______\\/\\\\__/\\\\/////////\\\\____________/\\\\\\/__\\/\\\\______\\//\\\\__/\\\\/////////\\\\____________/\\\\\\/__      ',
            '   _\\/\\\\\\\\\\\\\\\\\\\\\\/__\\/\\\\_______\\/\\\\__________/\\\\\\/____\\/\\\\_______\\/\\\\_\\/\\\\\\\\\\\\\\\\\\\\\\\\________/\\\\\\/____     ',
            '    _\\/\\\\/////////____\\/\\\\\\\\\\\\\\\\\\\\\\\\________/\\\\\\/______\\/\\\\_______\\/\\\\_\\/\\\\/////////\\\\______/\\\\\\/______   ',
            '     _\\/\\\\_____________\\/\\\\/////////\\\\______/\\\\\\/________\\/\\\\_______/\\\\__\\/\\\\_______\\/\\\\____/\\\\\\/________  ',
            '      _\\/\\\\_____________\\/\\\\_______\\/\\\\____/\\\\\\/__________\\/\\\\______\\/\\\\__\\/\\\\_______\\/\\\\__/\\\\\\/__________ ',
            '       _\\/\\\\_____________\\/\\\\_______\\/\\\\__/\\\\\\/____________\\/\\\\______\\/\\\\__\\/\\\\_______\\/\\\\/\\\\\\/___________ ',
            '        _\\///______________\\///________\\///__\\///______________\\////////////____\\///________\\///\\///____________',
            '                                                                        '
        ]
        self.rowIndex = 0
        self.animation_completed_once = False

    def run_animation(self):
        try:
            print("It's P@7D@7 Fellas!")
            #print('Press Ctrl-C to quit...')
            time.sleep(5)

            while True:  # Main program loop.
                self.rowIndex = self.rowIndex + 1
                if self.rowIndex == len(self.TEXT_ROWS):
                    self.rowIndex = 0
                    if not self.animation_completed_once:
                        self.animation_completed_once = True
                        self.display_progress_bar()

                print(self.TEXT_ROWS[self.rowIndex])
                time.sleep(self.PAUSE)
        except KeyboardInterrupt:
            sys.exit()

    def display_progress_bar(self):
        # Display a green progress bar when the animation completes once
        total_width = 50
        progress = 100.0
        block = int(round(total_width * progress))
        progress_bar = f"\r{Fore.GREEN}[{'#' * block}{' ' * (total_width - block)}]{Style.RESET_ALL} 100% Complete\n"
        sys.stdout.write(progress_bar)
        sys.stdout.flush()

if __name__ == '__main__':
    text_animation = TextAnimation()
    text_animation.run_animation()
