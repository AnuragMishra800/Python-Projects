import cv2
import numpy as np
import pyautogui
import keyboard  # Import the keyboard module

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('screen_recording.avi', fourcc, 8.0, (1920, 1080))

# Start recording message
print("Recording started. Press 'q' to quit.")

while True:
    # Take a screenshot
    img = pyautogui.screenshot()

    # Convert the screenshot to a numpy array
    frame = np.array(img)

    # Convert it from RGB (used by PyAutoGUI) to BGR (used by OpenCV)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Write the frame to the video file
    output.write(frame)

    # Check if 'q' key is pressed to quit recording
    if keyboard.is_pressed('q'):
        break

# Release the video writer and close all OpenCV windows
output.release()
cv2.destroyAllWindows()

# Recording finished message
print("Recording finished.")
