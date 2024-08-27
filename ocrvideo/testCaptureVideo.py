import cv2
import threading
import os
from multiThreadResearch import search_state
from tesseractcommand import tesseractFunction 
from preprod import preprod
import json

name = 'data/input_image.jpg'
exit_event = threading.Event()
zoom_scale = 1

# Load the JSON file
file_path = 'C:/Users/paya/Desktop/FinalProject/yugiho/data.json'

with open(file_path, 'r', encoding='utf-8') as json_file:
    print(json_file)
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


        height, width = frame.shape[:2]

        # Calculate the new height and width based on the zoom scale
        new_height = int(height / zoom_scale)
        new_width = int(width / zoom_scale)

        # Center coordinates to crop the zoomed region
        y1 = int((height - new_height) / 2)
        y2 = y1 + new_height
        x1 = int((width - new_width) / 2)
        x2 = x1 + new_width

        # Crop the zoomed region
        zoomed_frame = frame[y1:y2, x1:x2]

        # Resize the cropped frame to the original frame size
        zoomed_frame = cv2.resize(zoomed_frame, (width, height), interpolation=cv2.INTER_LINEAR)

        # # Write the zoomed frame to the output video
        # out.write(zoomed_frame)

        # # Display the live video feed
        # cv2.imshow('Frame', zoomed_frame)


        if not ret:
            print("Error: Failed to capture a frame.")
            break

        # Put your custom processing code here
        # For example, you can perform some image processing on 'frame'
        reconizingText(zoomed_frame)

        # Display the frame in the main thread
        # cv2.imshow('Camera', zoomed_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()

    cv2.destroyAllWindows()


# Custom processing function (you can define your own processing logic here)
def reconizingText(frame):
    grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Processed Frame', grayscale_frame)

    cv2.imwrite(name, grayscale_frame)

    # try:
    #     preprod()

    # except:
    #     print("Erreur pendant le pre prod")

    try:
        tesseractFunction()
        myText = read_text_from_file('text.txt')
        state_found = search_state(objects_dict, myText)
        if(state_found != None):
            print(float(state_found['card_prices'].cardmarket_price))
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