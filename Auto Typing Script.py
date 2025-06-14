import keyboard
import time
import pyperclip
import re
import sys

print(r"""
---------------------------------------------------------------------------------------
    _         _          _____            _               ____            _       _   
   / \  _   _| |_ ___   |_   _|   _ _ __ (_)_ __   __ _  / ___|  ___ _ __(_)_ __ | |_ 
  / _ \| | | | __/ _ \    | || | | | '_ \| | '_ \ / _` | \___ \ / __| '__| | '_ \| __|
 / ___ \ |_| | || (_) |   | || |_| | |_) | | | | | (_| |  ___) | (__| |  | | |_) | |_ 
/_/   \_\__,_|\__\___/    |_| \__, | .__/|_|_| |_|\__, | |____/ \___|_|  |_| .__/ \__|
                              |___/|_|            |___/                    |_|        

                                                        Coded By Abineeethan

--------------------------------------------------------------------------------------- 
""")

def get_user_input():
    """Get input from the user for the text to type and other parameters."""
    
    # Get the text to type
    base_text = input("\nEnter the text you want to type (default: 'hi'): ") or "hi"
    
    # Get output format
    print("\nHow should the output be formatted?")
    print("1. After each text, press Enter (e.g., 'hi' [Enter] 'hi' [Enter])")
    print("2. Continuous text (e.g., 'hihihi')")
    format_choice = input("Enter choice (1 or 2, default: 1): ") or "1"
    
    # Get the number of iterations
    iterations = input("\nHow many times should the text be repeated? (default: 5): ") or "5"
    try:
        iterations = int(iterations)
        if iterations < 1:
            iterations = 5
    except ValueError:
        iterations = 5
    
    # Get typing speed
    speed = input("\nEnter typing speed (seconds between characters, default: 0.01): ") or "0.01"
    try:
        speed = float(speed)
        if speed <= 0:
            speed = 0.01
    except ValueError:
        speed = 0.01
    
    # Get initial delay
    delay = input("\nHow many seconds to wait before starting? (default: 5): ") or "5"
    try:
        delay = int(delay)
        if delay < 0:
            delay = 5
    except ValueError:
        delay = 5
    
    # Format the full paragraph based on user choice
    if format_choice == "1":
        paragraph = (base_text + "\n") * iterations
    else:
        paragraph = base_text * iterations
    
    return base_text, paragraph, iterations, speed, delay, format_choice

def simulate_paragraph_typing(text, char_delay):
    """Simulate typing each character with proper handling of special cases."""
    emoji_pattern = re.compile("[\U0001F600-\U0001F64F"
                               "\U0001F300-\U0001F5FF"
                               "\U0001F680-\U0001F6FF"
                               "\U0001F700-\U0001F77F"
                               "\U0001F780-\U0001F7FF"
                               "\U0001F800-\U0001F8FF"
                               "\U0001F900-\U0001F9FF"
                               "\U0001FA00-\U0001FA6F"
                               "\U0001FA70-\U0001FAFF"
                               "\U00002700-\U000027BF"
                               "\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)

    total_chars = len(text)
    for i, char in enumerate(text, 1):
        if char.isupper():
            keyboard.press('shift')
            keyboard.press_and_release(char.lower())
            keyboard.release('shift')
        elif char == '\n':
            keyboard.press_and_release('enter')
        elif char == ' ':
            keyboard.press_and_release('space')
        elif char == '\t':
            keyboard.press_and_release('tab')
        elif emoji_pattern.match(char):
            pyperclip.copy(char)
            keyboard.press_and_release('ctrl+v')
        else:
            keyboard.press_and_release(char)
        
        # Calculate and display progress
        progress = i / total_chars * 100
        remaining_chars = total_chars - i
        sys.stdout.write(f"\rTyping progress: {progress:.1f}% | Remaining: {remaining_chars} chars")
        sys.stdout.flush()
        
        time.sleep(char_delay)

def start_typing_paragraph():
    """Main function to start the typing process."""
    base_text, paragraph, iterations, speed, delay, format_choice = get_user_input()
    
    print(f"\nScript is starting... Typing will begin in {delay} seconds.")
    print(f"Text sample: '{base_text.strip()}'")
    print(f"Number of repetitions: {iterations}")
    print(f"Output format: {'With Enter after each' if format_choice == '1' else 'Continuous'}")
    print(f"Typing speed: {speed} seconds per character")
    print(f"Total characters to type: {len(paragraph)}")
    print("\nSwitch to your target window now!")
    
    time.sleep(delay)
    
    print("\nTyping started...")
    simulate_paragraph_typing(paragraph, speed)
    
    print("\n\nFinished typing!")

if __name__ == "__main__":
    try:
        start_typing_paragraph()
    except KeyboardInterrupt:
        print("\n\nScript stopped by user.")
    except Exception as e:
        print(f"\n\nAn error occurred: {e}")
    finally:
        print("Goodbye!")