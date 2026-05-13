import cv2
import numpy as np
import requests
import threading

# Configuration
ESP_URL = "http://192.168.4.1/shock"
WIDTH, HEIGHT = 640, 480

# Game Variables
paddle_w, paddle_h = 100, 20
paddle_x = (WIDTH - paddle_w) // 2
ball_pos = [WIDTH//2, HEIGHT//2]
ball_speed = [5, -5]
bricks = [[(x*70 + 35, y*30 + 50) for x in range(8)] for y in range(4)]
score = 0

def send_shock():
    # Run in a thread to prevent game stuttering
    threading.Thread(target=lambda: requests.get(ESP_URL, timeout=0.05)).start()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: break
    frame = cv2.flip(frame, 1)
    
    # 1. Motion Tracking (Computer Vision) [cite: 745, 798, 839]
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Track a specific color (like a bright shirt) or use brightness
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, _, _, max_loc = cv2.minMaxLoc(gray)
    
    # Smooth paddle movement
    target_x = max_loc[0] - (paddle_w // 2)
    paddle_x += (target_x - paddle_x) * 0.2 
    paddle_x = np.clip(paddle_x, 0, WIDTH - paddle_w)

    # 2. Game Logic (Brick Breaker Engine) [cite: 841, 843]
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Wall Collisions
    if ball_pos[0] <= 0 or ball_pos[0] >= WIDTH: ball_speed[0] *= -1
    if ball_pos[1] <= 0: ball_speed[1] *= -1

    # Paddle Collision
    if (paddle_x < ball_pos[0] < paddle_x + paddle_w) and (HEIGHT - 40 < ball_pos[1] < HEIGHT - 20):
        ball_speed[1] *= -1

    # Brick Collision
    for row in bricks:
        for b in row:
            if (b[0]-30 < ball_pos[0] < b[0]+30) and (b[1]-15 < ball_pos[1] < b[1]+15):
                row.remove(b)
                ball_speed[1] *= -1
                score += 1

    # Game Over Condition (Ball Falls) [cite: 730, 787, 845]
    if ball_pos[1] > HEIGHT:
        print("Ball Dropped! Sending Physical Feedback...")
        send_shock()
        ball_pos = [WIDTH//2, HEIGHT//2] # Reset ball
        ball_speed = [5, -5]

    # 3. Rendering [cite: 846]
    game_layer = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
    # Draw Paddle
    cv2.rectangle(game_layer, (int(paddle_x), HEIGHT-30), (int(paddle_x+paddle_w), HEIGHT-10), (0, 255, 0), -1)
    # Draw Ball
    cv2.circle(game_layer, (int(ball_pos[0]), int(ball_pos[1])), 10, (255, 255, 255), -1)
    # Draw Bricks
    for row in bricks:
        for b in row:
            cv2.rectangle(game_layer, (b[0]-30, b[1]-10), (b[0]+30, b[1]+10), (0, 0, 255), -1)
            
    # Combine Camera and Game
    output = cv2.addWeighted(frame, 0.5, game_layer, 0.5, 0)
    cv2.putText(output, f"Score: {score}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow("Interactive Brick Breaker", output)

    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
