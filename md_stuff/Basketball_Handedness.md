# Basketball Handedness 
## q.11 difficult

A professional basketball organization is interested in handedness (right-handed vs. left-handed) among basketball 
players. The organization takes the starting five basketball players on a team and gives each player 1 if they are 
right-handed and 0 if they are left-handed. The five digits for a teams' starters are expressed as a 5-digit binary 
number. The positions are listed in order from left to right: point guard, shooting guard, small forward, power 
forward, center. The professional basketball organization stores the information (the 5-digit binary number) about a 
teams' starting five as a decimal number. One particular team's decimal representation is 19. Which starting positions 
are left-handed for this team?

## Explanation:

for each of the 5 players a 1 or 0 is asighned based on if they are right-handed or left-handed their digits are ordered 
from left to right based on their positions: point guard, shooting guard, small forward, power forward and center.
These ordered values can be represented as a decimal number in the standard fasion. The question requires you to reverse
engineer this process


## Answer:
1. to start represent the number 19 as a 5 digit binary number
    * 10000 represents 16
    * 00011 represents 3
    * final value is 10011
2. see how these digits represent players 
    * positions are listed in order from left to right
    * point guard, shooting guard, small forward, power forward, center
    * point guard = 1, shoot guard = 0, small forward = 0, power forward = 1, center = 1
    * point guard = Right, shoot guard = Left, small forward = Left, power forward = Right, center = Right
3. final answer 
    * "which starting positions are left-handed for this team?"
    * shoot gaurd and small forward
    * answer is B