import cv2
from ultralytics import YOLO


VIDEO_PATH = "video/video_input.mp4"
OUTPUT_PATH = "output_detected.mp4"

# Charger modèle
model = YOLO("yolov8n.pt")
CLASSES_TO_DETECT = ["person", "backpack", "handbag"]

# Couleurs plus variées (BGR)
CLASS_COLORS = {
    "person": (0, 255, 0),       # Vert
    "backpack": (255, 0, 255),   # Violet
    "handbag": (0, 255, 255)     # Jaune
}

# Lecture vidéo
cap = cv2.VideoCapture(VIDEO_PATH)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(OUTPUT_PATH, fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.track(
        frame,
        conf=0.3,
        iou=0.3,
        persist=True,
        tracker="botsort.yaml",
        classes=[0, 24, 26],  # IDs: person (0), backpack (24), handbag (26)
        verbose=False
    )

    if results[0].boxes.id is not None:
        boxes = results[0].boxes.xyxy.cpu().numpy()
        classes = results[0].boxes.cls.cpu().numpy()
        confs = results[0].boxes.conf.cpu().numpy()
        track_ids = results[0].boxes.id.cpu().numpy().astype(int)

        for box, cls, conf, track_id in zip(boxes, classes, confs, track_ids):
            class_name = model.names[int(cls)]
            if class_name in CLASSES_TO_DETECT:
                x1, y1, x2, y2 = map(int, box)
                color = CLASS_COLORS.get(class_name, (255, 255, 255))

                # Dessiner boîte
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

                # Label = class + ID + confiance
                label = f"{class_name} ID:{track_id} {conf:.2f}"
                cv2.putText(frame, label, (x1, y1 - 7),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    cv2.imshow("Détection", frame)
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

