import serial
import time

class DFRobotA02Distance:

  ## Board status 
  STA_OK = 0x00
  STA_ERR_CHECKSUM = 0x01
  STA_ERR_SERIAL = 0x02
  STA_ERR_CHECK_OUT_LIMIT = 0x03
  STA_ERR_CHECK_LOW_LIMIT = 0x04
  STA_ERR_DATA = 0x05

  last_operate_status = STA_OK
  ## variable 
  distance = 0

  ## Maximum range
  distance_max = 4500
  distance_min = 0
  range_max = 4500

  def __init__(self):
    self._ser = serial.Serial("/dev/ttyAMA0", 9600)
    if self._ser.isOpen() != True:
      self.last_operate_status = self.STA_ERR_SERIAL

  def set_dis_range(self, min, max):
    self.distance_max = max
    self.distance_min = min

  def getDistance(self):
    self._measure()
    return self.distance
  
  def _check_sum(self, l):
    return (l[0] + l[1] + l[2])&0x00ff

  def _measure(self):
    data = []
    i = 0
    while self._ser.inWaiting() > 0:
      rlt = self._ser.read()
      try:
        data.append(ord(rlt))
      except:
        data.append(rlt[0])
      i += 1
      if data[0] != 0xff:
        i = 0
        data = []
      if i == 4:
        break
    if i == 4:
      sum = self._check_sum(data)
      if sum != data[3]:
        self.last_operate_status = self.STA_ERR_CHECKSUM
      else:
        self.distance = data[1]*256 + data[2]
        self.last_operate_status = self.STA_OK