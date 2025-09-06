import cv2
import numpy as np
import time
from collections import Counter
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image

# Load the pre-trained MobileNetV2 model
model = MobileNetV2(weights='imagenet')

# Initialize analytics
class_counts = Counter()
prediction_times = []

# Start webcam
cap = cv2.VideoCapture(0)
print("SmartVision AI: Real-time Image Recognition & Analytics Demo\nPress 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess the frame
    img = cv2.resize(frame, (224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    # Predict
    start_time = time.time()
    preds = model.predict(x)
    elapsed = time.time() - start_time
    prediction_times.append(elapsed)

    # Decode predictions
    decoded = decode_predictions(preds, top=1)[0][0]
    label = f"{decoded[1]} ({decoded[2]*100:.2f}%)"
    class_counts[decoded[1]] += 1

    # Annotate frame
    cv2.putText(frame, label, (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
    cv2.putText(frame, f"Avg Prediction Time: {np.mean(prediction_times):.2f}s", (10,60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0),2)
    cv2.putText(frame, f"Top Classes: {class_counts.most_common(3)}", (10,90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255),2)
    cv2.imshow('SmartVision AI Demo', frame)

    # Quit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Print summary analytics
print("\nSession Analytics:")
print("Top 5 detected classes:", class_counts.most_common(5))
print(f"Average prediction time: {np.mean(prediction_times):.2f} seconds")
