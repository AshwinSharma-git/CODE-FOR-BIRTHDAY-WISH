import time
import pyttsx3

# Function to print "Happy Birthday" in big letters with animation
def birthday_animation():
    big_birthday = [
        " H   H   AAAAA  PPPPP  PPPPP  Y   Y       BBBB   III  RRRR   TTTTT  DDDD   AAAAA   Y   Y",
        " H   H  A     A P   P  P   P   Y Y        B   B   I   R   R    T   D   D  A     A   Y Y ",
        " HHHHH  AAAAAAA PPPPP  PPPPP    Y         BBBBB   I   RRRR     T   D   D  AAAAAAA    Y  ",
        " H   H  A     A P      P        Y         B   B   I   R  R     T   D   D  A     A    Y  ",
        " H   H  A     A P      P        Y         BBBB   III  R   R    T   DDDD   A     A    Y  "
    ]
    
    # Print the big "Happy Birthday" with animation effect
    for line in big_birthday:
        print(line)
        time.sleep(0.5)

# Function to pronounce "Happy Birthday" using text-to-speech
def birthday_song():
    engine = pyttsx3.init()  # Initialize the TTS engine
    
    # Birthday message
    message = "MAY THIS YEAR BRINGS ENDLESS REASONS TO SMILE, HAPPY  BIRTHDAY  ( YOUR FRND NAME)!  "

    # Pronounce the birthday message
    engine.say(message)
    engine.runAndWait()

# Main function to execute the animation and speech
def main():
    birthday_animation()  # Big letter animation
    birthday_song()       # Pronounce the birthday message

# Run the program
main()