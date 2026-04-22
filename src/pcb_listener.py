import serial
from music_interface import music

# Replace 'COM3' with the actual port your PCB connects to
# You can find this in Device Manager later
try:
    ser = serial.Serial('COM3', 9600, timeout=1)
    print("Aether: PCB Connected and Listening...")
except:
    print("Aether Warning: PCB not found. Integration ready for hardware.")

def listen_to_pcb():
    while True:
        if 'ser' in locals() and ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            
            if line == "PLAY_PAUSE":
                music.play()
            elif line == "NEXT":
                music.next_track()
            elif line == "VOL_UP":
                # Logic to increase volume in steps
                pass

if __name__ == "__main__":
    listen_to_pcb()