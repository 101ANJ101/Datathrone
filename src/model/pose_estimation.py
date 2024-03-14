import dlib
import cv2
import numpy as np
import os 
def calculate_eye_angle(left_eye_center, focal_point):
  vector1 = left_eye_center - focal_point
  vector2 = np.array([0, -1]) 

  if np.linalg.norm(vector1) == 0:
    return 0  

  angle = np.arccos(np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2)))
  return np.degrees(angle)


def process_image(image_path, detector, predictor):
  img = cv2.imread(image_path)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  gray = cv2.equalizeHist(gray)

  faces = detector(gray)

  for face in faces:
    landmarks = predictor(gray, face)
    landmarks = np.array([(landmarks.part(i).x, landmarks.part(i).y) for i in range(68)])

    left_eye_center = np.mean(landmarks[36:42], axis=0)
    right_eye_center = np.mean(landmarks[42:48], axis=0)

    eyes_center = (left_eye_center + right_eye_center) / 2

    focal_point = np.array([img.shape[1] / 2, img.shape[0] / 2])

    angle = calculate_eye_angle(left_eye_center, focal_point)

    cv2.putText(img, f"Angle: {angle:.2f} degrees", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

  cv2.imshow("Image", img)
  cv2.waitKey(0) 


if __name__ == "__main__":
  image_folder = "src/model/eye_detection_output"

  detector = dlib.get_frontal_face_detector()
  predictor = dlib.shape_predictor('src/model/shape_predictor_68_face_landmarks.dat')

  for filename in os.listdir(image_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
      image_path = os.path.join(image_folder, filename)
      process_image(image_path, detector, predictor)

  # Release resources
  cv2.destroyAllWindows()
