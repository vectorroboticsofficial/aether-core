import pyautogui

def execute_command(text):
    text = text.lower()
    
    if "open calculator" in text:
        print("System: Opening Calculator...")
        pyautogui.press('win')
        pyautogui.write('calculator')
        pyautogui.press('enter')
        
    elif "volume up" in text:
        pyautogui.press('volumeup')
        print("System: Increasing Volume")

    else:
        print(f"System: Command '{text}' not recognized.")

# Test it manually for now
if __name__ == "__main__":
    user_input = input("Lead, enter a test command: ")
    execute_command(user_input)