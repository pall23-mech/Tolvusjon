import cv2

# Start video capture
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Webcam not accessible")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if frame is read correctly
    if not ret:
        print("Error: Can't receive frame (stream end?). Exiting ...")
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Find the brightest spot
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)

    # Mark the brightest spot
    cv2.circle(frame, maxLoc, 10, (255, 0, 0), 2)

    # Display the resulting frame
    cv2.imshow('Frame with Brightest Spot', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
