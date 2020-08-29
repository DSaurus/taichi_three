import taichi as ti
import taichi_three as t3
import numpy as np

ti.init(ti.cpu)

scene = t3.Scene()
model = t3.Model(obj=t3.readobj('assets/monkey.obj', scale=0.8))
scene.add_model(model)
camera = t3.Camera()
scene.add_camera(camera)

light = t3.Light([0.4, -1.5, 1.8])
scene.add_light(light)
gui = ti.GUI('Model', camera.res)
while gui.running:
    gui.get_event(None)
    gui.running = not gui.is_pressed(ti.GUI.ESCAPE)
    camera.from_mouse(gui)
    #model.L2W.from_mouse(gui)
    scene.render()
    gui.set_image(camera.img)
    gui.show()