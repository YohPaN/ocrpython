import cv2
import threading
import subprocess
import os
from multiThreadResearch import search_state
from tesseractcommand import tesseractFunction 
from preprod import preprod
import json

name = 'data/input_image.jpg'
exit_event = threading.Event()

# Load the JSON file
file_path = 'objects_data.json'
with open(file_path, 'r') as json_file:
    objects_dict = json.load(json_file)


def read_text_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text_content = file.read()
            return text_content
    except FileNotFoundError:
        print("File not found or path is incorrect.")
        return None
    except IOError as e:
        print(f"Error reading the file: {e}")
        return None
    
# Function to continuously capture frames from the camera
def capture_frames():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Unable to access the camera.")
        return

    while not exit_event.is_set():
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture a frame.")
            break

        # Put your custom processing code here
        # For example, you can perform some image processing on 'frame'
        reconizingText(frame)

        # Display the frame in the main thread
        cv2.imshow('Camera', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()

    cv2.destroyAllWindows()


# Custom processing function (you can define your own processing logic here)
def reconizingText(frame):
    grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Processed Frame', grayscale_frame)

    cv2.imwrite(name, grayscale_frame)

    try:
        preprod()

    except:
        print("Erreur pendant le pre prod")

    try:
        tesseractFunction()
        myText = read_text_from_file('text.txt')
        state_found = search_state(objects_dict, myText)
        if(state_found != None):
            print('Great !!!')
            exit_event.set()
        else:
            os.remove('/data/input_image.jpg')
        
    except:
        True

# Create a thread for capturing frames
capture_thread = threading.Thread(target=capture_frames)

# Start the capture thread
capture_thread.start()

# Continue with your main thread or any other processing here
# For this example, we'll just wait for the capture thread to finish and then close the window
capture_thread.join()

print('Done')