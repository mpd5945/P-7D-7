import random
import time
from colorama import Fore, Style, init

# Initialize colorama to work on Windows as well
init()

BAR = chr(9608)  # Character 9608 is '█'

def main():
    # Simulate a download:
    print('Progress Bar')
    bytes_downloaded = 0
    download_size = 4096

    while bytes_downloaded < download_size:
        # "Download" a random amount of "bytes":
        bytes_downloaded += random.randint(0, 100)

        # Get the progress bar string for this amount of progress:
        bar_str = get_progress_bar(bytes_downloaded, download_size)

        # Print the colored progress bar and update it on the same line:
        print(bar_str, end='\r', flush=True)
        time.sleep(0.2)  # Pause for a little bit.

    print("\nDownload Complete!")

def get_progress_bar(progress, total, bar_width=40):
    """Returns a string representing a colored progress bar."""
    progress_bar = '['

    # Ensure progress is within the valid range:
    progress = min(total, max(0, progress))

    # Calculate the number of bars to display:
    number_of_bars = int((progress / total) * bar_width)

    # Add color to the progress bar based on the percentage completed:
    if progress / total < 0.5:
        progress_bar += Fore.RED
    elif progress / total < 0.8:
        progress_bar += Fore.YELLOW
    else:
        progress_bar += Fore.GREEN

    progress_bar += BAR * number_of_bars
    progress_bar += Style.RESET_ALL  # Reset color
    progress_bar += ' ' * (bar_width - number_of_bars)
    progress_bar += ']'

    # Calculate the percentage complete:
    percent_complete = round(progress / total * 100, 1)
    progress_bar += ' ' + str(percent_complete) + '%'

    # Add the numbers:
    progress_bar += ' ' + str(progress) + '/' + str(total)

    return progress_bar

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
