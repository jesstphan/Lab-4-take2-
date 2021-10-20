import cgi
import RPi.GPIO as GPIO
import json
import cgitb
cgitb.enable()

data = cgi.FieldStorage()
s1 = data.getvalue('slider1')
b = data.getvalue('option')
info = {"slider1":s1, "option":b}
with open('ledpwm.txt', 'w') as f:
  json.dump(info,f)    
    
   
print('Content-type: text/html\n\n')
print('<html>')
print('<form action="/cgi-bin/LEDControl.py" method="POST">')
if b == 'g':
  print('input type="radio" name="option" value="b" checked> LED Blue <br>')
 	print('<input type="radio" name="option" value="g"> LED Green <br>')
 	print('<input type="radio" name="option" value="w"> LED White <br>')
  
print('<input type="range" name="slider1" min="0" max="100" value="%s"><br>' % s1)
print('<input type="submit" value="Change LED brightness">')
print('</form>')
print('Brightness = %s' % s1)
print('</html>')
