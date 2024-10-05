import pi3d
from rotatingCamera import RotatingCamera

#Create display
DISPLAY = pi3d.Display.create()
DISPLAY.set_background(0.0,0.0,0.0,1)

#Create mouse object
mymouse = pi3d.Mouse(restrict = False)
mymouse.start()

#Create camera
CAM = RotatingCamera(5,mymouse)

#Create shader
shader = pi3d.Shader('uv_light')
marsimg = pi3d.Texture('mars.jpg')

#Create sphere
ball = pi3d.Sphere()

#Listen for keystrokes
mykeys = pi3d.Keyboard()

#Start the display loop:
while DISPLAY.loop_running():
	#store keystrokes:
	k = mykeys.read()
	if k == 27:
		mykeys.close()
		DISPLAY.destroy()
		break
	CAM.update(mymouse)
	ball.draw(shader, [marsimg])
