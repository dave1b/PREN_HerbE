from HerbE import HerbE
import sys
sys.path.insert(0, '/home/pi/Desktop/PREN/Button')
sys.path.insert(0, '../Button')
from Button import Button
 
def main():
    button = Button()
    button.startButtonListener()
    #herbE = HerbE()
    #herbE.initialStartOfHerbE()
    
if __name__ == '__main__':
    main()