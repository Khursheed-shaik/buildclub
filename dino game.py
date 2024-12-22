import cv2
import numpy as np

# Game parameters
width, height = 600, 400
ball_radius = 15
obstacle_width, obstacle_height = 40, 20
ball_x, ball_y = 100, height - ball_radius
ball_y_velocity = 0
gravity = 0.5
jump_strength = -10
obstacle_speed = 5
score = 0
game_over = False

# Initialize obstacles
obstacles = [{'x': width, 'y': height - obstacle_height}]

def draw_ball(image):
    cv2.circle(image, (ball_x, int(ball_y)), ball_radius, (0, 255, 0), -1)

def draw_obstacles(image):
    for obs in obstacles:
        cv2.rectangle(image, (obs['x'], obs['y']),
                      (obs['x'] + obstacle_width, obs['y'] + obstacle_height),
                      (0, 0, 255), -1)

def draw_score(image):
    cv2.putText(image, f'Score: {score}', (width - 120, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

def check_collision():
    global game_over
    for obs in obstacles:
        if (ball_x + ball_radius > obs['x'] and
            ball_x - ball_radius < obs['x'] + obstacle_width and
            ball_y + ball_radius > obs['y'] and
            ball_y - ball_radius < obs['y'] + obstacle_height):
            game_over = True

def main():
    global ball_y, ball_y_velocity, game_over, score
    cv2.namedWindow('Dino Game')
    
    while True:
        image = np.zeros((height, width, 3), dtype=np.uint8)
        
        if not game_over:
            # Update ball position
            ball_y_velocity += gravity
            ball_y += ball_y_velocity
            
            if ball_y >= height - ball_radius:
                ball_y = height - ball_radius
                ball_y_velocity = 0
            
            # Update obstacles
            for obs in obstacles:
                obs['x'] -= obstacle_speed
            
            # Add new obstacle
            if obstacles[-1]['x'] < width - 200:
                obstacles.append({'x': width, 'y': height - obstacle_height})
            
            # Remove off-screen obstacles
            if obstacles[0]['x'] < -obstacle_width:
                obstacles.pop(0)
                score += 1
            
            # Draw everything
            draw_ball(image)
            draw_obstacles(image)
            draw_score(image)
            
            # Check for collisions
            check_collision()
        
        # Display "Game Over" message
        if game_over:
            cv2.putText(image, 'Game Over', (width // 3, height // 2),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3, cv2.LINE_AA)
        
        cv2.imshow('Dino Game', image)
        
        key = cv2.waitKey(30)
        if key == ord('q'):
            break
        elif key == 32 and not game_over:  # Space bar
            if ball_y == height - ball_radius:
                ball_y_velocity = jump_strength
    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
