# Simple script to account number of times someone jumps in a mario game

from inputs import get_gamepad

def main():
    total_a_presses = 0
    while True:
        events = get_gamepad()
        for event in events:
            if event.code == "BTN_SOUTH":
                if event.state == 1:
                    total_a_presses -= -1
                    print("Jumping...")
        if total_a_presses > 9:
            break
    print("Total times that Mario jumped while playing:", total_a_presses)

if __name__ == "__main__":
    main()