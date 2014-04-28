# Implementation of classic arcade game Pong
  
import simplegui
import random
  
  
# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
score1 = 0
score2 = 0
  
# initialize paddle1_pos paddle2_pos  for new game  ([4, 240], [4, 280])  ([596, 240],[596, 280])
paddle1_pos = [[PAD_WIDTH/2, HEIGHT/2 - PAD_HEIGHT/2], [PAD_WIDTH/2, HEIGHT/2 + PAD_HEIGHT/2]]
paddle2_pos = [[WIDTH - PAD_WIDTH/2, HEIGHT/2-PAD_HEIGHT/2], [WIDTH - PAD_WIDTH/2, HEIGHT/2+PAD_HEIGHT/2]] 

paddle1_vel = 0
paddle2_vel = 0

# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos =[WIDTH/2, HEIGHT/2]
ball_vel = [0,0]
  
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos =[WIDTH/2, HEIGHT/2]
    if direction == LEFT :
       ball_vel = [3, -3]
    if direction == RIGHT:
       ball_vel = [-3, -3]
        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
      
    paddle1_pos = [[PAD_WIDTH/2, HEIGHT/2 - PAD_HEIGHT/2], [PAD_WIDTH/2, HEIGHT/2 + PAD_HEIGHT/2]]
    paddle2_pos = [[WIDTH - PAD_WIDTH/2, HEIGHT/2-PAD_HEIGHT/2], [WIDTH - PAD_WIDTH/2, HEIGHT/2+PAD_HEIGHT/2]] 
    spawn_ball(RIGHT)
      
def button_handler():
    new_game()
  
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global  paddle1_vel  , paddle2_vel 
   
          
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
          
    # update ball
         
    if   (ball_pos[0] <= BALL_RADIUS +PAD_WIDTH):
        if (paddle1_pos[0][1] <= ball_pos[1] <= paddle1_pos[1][1]) :
            ball_vel[0] = - 1.15 * ball_vel[0]
        else:
            score2 += 1
            print "score2 =",score2
            spawn_ball(RIGHT)
            
    if (ball_pos[0] >=  WIDTH - BALL_RADIUS-PAD_WIDTH) :
        if (paddle2_pos[0][1] <= ball_pos[1] <= paddle2_pos[1][1]):
            ball_vel[0] = - 1.15 * ball_vel[0]
        else:
            score1 += 1
            print "score1 =",score1
            spawn_ball(LEFT)     
            
    if ball_pos[1] <= BALL_RADIUS :
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] >= HEIGHT - BALL_RADIUS :
        ball_vel[1] = - ball_vel[1]
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS , 4, "Red", "White")
      
      
      # update paddle's vertical position, keep paddle on the screen
    

    if (  paddle1_pos[0][1]<0):
        paddle1_pos = [[4, 0] , [4, 80]]
    elif (  paddle1_pos[1][1]> 400) :
        paddle1_pos = [[4, 320], [4, 400]]
    else:
        paddle1_pos[0][1] += paddle1_vel
        paddle1_pos[1][1] += paddle1_vel 
        
    if (  paddle2_pos[0][1]<0):
        paddle2_pos = [[596, 0] , [596, 80]]
    elif (  paddle2_pos[1][1]> 400) :
        paddle2_pos = [[596, 320], [596, 400]]
    else:
        paddle2_pos[0][1] += paddle2_vel
        paddle2_pos[1][1] += paddle2_vel 
      
    # draw paddles
 
    #canvas.draw_polyline([(PAD_WIDTH/2, HEIGHT/2 - PAD_HEIGHT/2), (PAD_WIDTH/2, HEIGHT/2 + PAD_HEIGHT/2)], PAD_WIDTH, 'White')
    #canvas.draw_polyline([(WIDTH - PAD_WIDTH/2, HEIGHT/2-PAD_HEIGHT/2), (WIDTH - PAD_WIDTH/2, HEIGHT/2+PAD_HEIGHT/2)], PAD_WIDTH, 'White')
    canvas.draw_polyline(paddle1_pos, PAD_WIDTH, 'White')
    canvas.draw_polyline(paddle2_pos, PAD_WIDTH, 'White')
    
    # draw scores
    canvas.draw_text(str(score1), (200, 100), 50, 'White') 
    canvas.draw_text(str(score2), (400, 100), 50, 'White') 
def keydown(key):
    
    global paddle1_vel, paddle2_vel, ball_vel
    acc = 10

    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel += acc
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc
          

   # print ball_pos
     
def keyup(key):
    global paddle1_vel, paddle2_vel
 
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
  
 # create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button('New Game', button_handler)
  
  
# start frame
new_game()
frame.start()
  
