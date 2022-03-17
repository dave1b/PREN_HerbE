'''!
  @n Connect board with raspberryPi.
  @n --------------------------------------------
  @n sensor pin |         raspberry pi          |
  @n     VCC    |            5V/3V3             |
  @n     GND    |             GND               |
  @n     RX     |          (BCM)14 TX           |
  @n     TX     |          (BCM)15 RX           |
  @n --------------------------------------------
'''

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from DFRobot_RaspberryPi_A02YYUW import DFRobot_A02_Distance as Board

if __name__ == "__main__":
  board = Board()
  dis_min = 0 #Minimum ranging threshold: 0mm
  dis_max = 4500 #Highest ranging threshold: 4500mm  
  board.set_dis_range(dis_min, dis_max)
  while True:
    distance = board.getDistance()
    #Delay time < 0.6s
    #time.sleep(0.3) 