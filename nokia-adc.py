#!/usr/bin/python3
#新規作成時はlFで保存すること 
#MCP3008のCH0,1,2,3の値をNOKIA5110に表示する
from gpiozero import MCP3008,LED
from time import sleep
from signal import pause
import board
import busio
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_pcd8544
#import ambient
##LCD初期化
# Parameters to Change
BORDER = 5
FONTSIZE = 10

spi = busio.SPI(board.SCK, MOSI=board.MOSI)
dc = digitalio.DigitalInOut(board.D6)  # data/command
cs = digitalio.DigitalInOut(board.CE0)  # Chip select
reset = digitalio.DigitalInOut(board.D5)  # reset
display = adafruit_pcd8544.PCD8544(spi, dc, cs, reset)
display.bias = 4
display.contrast = 40
backlight = digitalio.DigitalInOut(board.D13)  # backlight
backlight.switch_to_output()
backlight.value = True
display.fill(0)
display.show()
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 11)
#Vref = 3.29476
adc = MCP3008(channel=0,device=1)
adc1 = MCP3008(channel=1,device=1)
adc2 = MCP3008(channel=2,device=1)
adc3 = MCP3008(channel=3,device=1)
SensorPower0=LED(20)
SensorPower1=LED(21)
SensorPower2=LED(22)
SensorPower3=LED(23)
while True:
  image = Image.new("1", (display.width, display.height))
  draw = ImageDraw.Draw(image)
  SensorPower0.on() #GPIO20(pin#38)
  SensorPower1.on() #GPIO21(pin#40)
  SensorPower2.on() #GPIO22(pin#15)
  SensorPower3.on() #GPIO23(pin#16)
  sleep(0.1)
  v0=adc.value*1000
  v1=adc1.value*1000
  v2=adc2.value*1000
  v3=adc3.value*1000
  SensorPower0.off()
  SensorPower1.off()
  SensorPower2.off()
  SensorPower3.off()
  print("{:>4.0f},{:>4.0f},{:>4.0f},{:>4.0f}".format(v0,v1,v2,v3))
  draw.text( (0,0), "CH0={:>3.0f}".format(v0), font=font, fill=255)
  draw.text( (0,10), "CH1={:>3.0f}".format(v1), font=font, fill=255)
  draw.text( (0,20), "CH2={:>3.0f}".format(v2), font=font, fill=255)
  draw.text( (0,30), "CH3={:>3.0f}".format(v3), font=font, fill=255)
  display.image(image)
  display.show()

#am=ambient.Ambient(21906,"50151d84188104a6")
#r=am.send({"d1":v})
#pause()
