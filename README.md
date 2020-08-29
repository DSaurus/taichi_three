Taichi THREE
============

[![Downloads](https://pepy.tech/badge/taichi-three)](https://pepy.tech/project/taichi-three)
[![Latest Release](https://img.shields.io/github/v/release/taichi-dev/taichi_three)](https://github.com/taichi-dev/taichi_three/releases)

Taichi THREE is an extension library of the [Taichi Programming Language](https://github.com/taichi-dev/taichi) to render 3D scenes into nice-looking 2D images in real-time (work in progress).


![Example](https://github.com/taichi-dev/taichi_three/raw/master/assets/example.png)


New in 0.0.3
------------

**Full camera control:** use `scene.camera.from_mouse(gui)` after a `gui.get_event()` call (without arguments) to control the camera with the mouse.
* Drag with the left mouse button pressed to orbit the camera.
* Drag with the right mouse button or use the wheel to zoom in and out.
* Drag with the middle mouse buttom to pan the camera.

Other updates:
* Support binding textures to models.
* Backface culling for perspective cameras.
* Used the area method to compute barycentric coordinates.
* Clip the triangle bounding box to prevent drawing outside the camera.



Installation
------------

1. Install Taichi THREE via `pip` for end-users:

```bash
# Python 3.6/3.7/3.8 (64-bit)
pip install taichi_three
```

2. Clone and install latest Taichi THREE from `dev` branch:

```bash
# Python 3.6/3.7/3.8 (64-bit)
pip install taichi taichi_glsl
python setup.py build install
```


How to play
-----------

First, import Taichi and Taichi THREE:
```py
import taichi as ti
import taichi_three as t3

ti.init(ti.cpu)
```

---

Then, create a scene using:
```py
scene = t3.Scene()
```

NOTE: scene creation should be put before any kernel invocation or host access,
i.e. before materialization, so that `Scene.__init__` could define its internal
tensors without an error.

TL;DR: Put this line as forward as possible! Ideally right below `ti.init()`.

---

After that, load the model(s), and feed them into `scene`:

```py
model = t3.Model(t3.readobj('assets/monkey.obj', scale=0.6))
scene.add_model(model)
```

If you want to add texture, read the texture image and feed it into `model`:

```py
texture = ti.imread('assets/cloth.jpg')
model = t3.Model(t3.readobj('assets/monkey.obj', scale=0.6), tex=texture)
```

NOTE: model creations should also be put as forward as possible too.

---

Then, create the camera(s), and put it into `scene`:

```py
camera = t3.Camera()
scene.add_camera(camera)
``` 

NOTE: camera creations should also be put as forward as possible.

---

Also don't forget to set the light:
```py
light = t3.Light()
scene.add_light(light)
```

---

Finally, create a GUI. And here goes the main loop:

```py
gui = ti.GUI('Monkey')
while gui.running:
    scene.render()            # render the model(s) into image
    gui.set_image(camera.img)  # display the result image
    gui.show()
```

---

Checkout the [`examples/`](https://github.com/taichi-dev/taichi_three/tree/master/examples) directory for more runnable examples.

Loading models
--------------
Taichi-three uses a **left-handed** coordinate system where the +Z axis points **from** the camera **towards** the object. Therefore when exporting meshes from a modeling software (e.g., Blender), the axis directions should be set as "+Z forward, +Y up" so that the model will be oriented corrected in the taichi-three camera.