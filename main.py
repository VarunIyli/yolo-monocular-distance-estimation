from ultralytics import YOLO
import cv2

# Load image
image = cv2.imread("001259.png")

# Load YOLO model
model = YOLO("yolov8n.pt")

# Run detection
results = model(image)

# Loop through detected objects
for box in results[0].boxes:

    # Get coordinates
    x1, y1, x2, y2 = map(int, box.xyxy[0])

    # Compute height
    height_pixels = y2 - y1

    # Ignore very large nearby car
    if height_pixels < 30:

        # Distance estimation
        focal_length = 721
        real_height = 2.2

        distance = (focal_length * real_height) / height_pixels

        # Draw rectangle
        cv2.rectangle(image,
                      (x1, y1),
                      (x2, y2),
                      (0, 255, 0),
                      2)

        # Put text
        text = f"Van: {distance:.2f} m"

        cv2.putText(image,
                    text,
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    2)

        print("White Van Distance:", distance)

# Show image
cv2.imshow("Detected White Van", image)

# Save image
cv2.imwrite("output_detected.png", image)

cv2.waitKey(0)
cv2.destroyAllWindows()