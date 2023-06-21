import cv2
import mysql.connector

db = mysql.connector.connect(
    host="your_hostname",
    user="your_userid",
    password="your_pwd",
    database="open_camera_links"
)

cursor = db.cursor()

query = "SELECT http_link FROM links"
cursor.execute(query)
uris = cursor.fetchall()

def connect_to_camera(uri):
    cap = cv2.VideoCapture(uri)
    
    if not cap.isOpened():
        print("Failed to connect to the camera")
        return
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("Failed to retrieve frame from the camera")
            break
        
        cv2.imshow("Camera Stream", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()


for uri in uris:
    uri = uri[0]  
    connect_to_camera(uri)
