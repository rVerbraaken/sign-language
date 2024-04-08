#Roel Verbraaken, Colin Harmsen, Creative Technology Year 2.

import cv2

def main():
    # Open the default camera
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the resulting frame
        cv2.imshow('frame', frame)

        # Wait for space key press to take a picture
        if cv2.waitKey(1) & 0xFF == ord(' '):
            label = input("Enter label for the image: ")  # Get label from user input
            file_name = f"{label}.jpg"  # File name for the image with label
            cv2.imwrite(file_name, frame)  # Save the image with the given label
            print(f"Image saved as {file_name}")

        # Wait for a letter key press to exit the loop
        if cv2.waitKey(1) & 0xFF != 255:
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
