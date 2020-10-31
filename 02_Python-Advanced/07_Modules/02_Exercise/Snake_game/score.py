current_score = 0
score_pos = (10 , 25)
score_text = "Score: "


def draw_score():
    fill(255)
    textSize(20)
    text(score_text + str(current_score),
         score_pos[0],
         score_pos[1])

def increase():
    global current_score
    current_score += 1 
