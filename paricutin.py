import pi3d
from rotatingCamera import RotatingCamera

#Create display
DISPLAY = pi3d.Display.create()
lights = pi3d.Light(lightamb = (0.8,0.8,0.8))
DISPLAY.set_background(0.0,0.0,0.0,1)

#Create mouse object
mymouse = pi3d.Mouse(restrict = False)
mymouse.start()

#Create camera
CAM = RotatingCamera(2,mymouse)

#Create shader
shader = pi3d.Shader('uv_light')

#Load textures
diftex = pi3d.Texture("model/dif.png")

#Load model
mymodel = pi3d.Model(file_string='model/pariCubic.obj', name='paricutin')
mymodel.set_shader(shader)

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
	mymodel.draw(shader)
