# Script will make use of image recognition to check where you are
# within the menu. This is just to start learning about image recognition;
# nothing big will be done here, yet.

from inputs import get_gamepad

def main():
    while True:
        events = get_gamepad()
        for event in events:
            if event.code == "BTN_SOUTH":
                if event.state == 1:
                    total_a_presses -= -1
                    print("Interacting with something...")

if __name__ == "__main__":
    main()