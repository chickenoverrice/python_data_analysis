import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    count = 0
    for _ in range(numTrials):
        balls = ['red','red','red','red','green','green','green','green']
        first_ball = balls.pop(random.randrange(8))       
        second_ball = balls.pop(random.randrange(7))
        third_ball = balls.pop(random.randrange(6))
        if first_ball == second_ball == third_ball:
            count += 1
            
    ans = float(count)/float(numTrials)
    return ans       
        
print drawing_without_replacement_sim(1000)
        
        