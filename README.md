# konics
This is an autocross simulation engine for MIT AFSAE. For most users, you should run `konics` using
Docker to ensure consistent behavior. On the other hand, if you need every bit of performance, this
**should** work out-of-the box on macOS and Windows 10; if you use some other OS, you will need to
compile POV-Ray yourself and make sure the `povray` binary can be found on your PATH.

## setup
Let's break down the below commands. First we pull the latest build of konics from the Docker Hub - 
if it says not found, that's probably because it's private and you should email me for access. Next
we run the container with the `-p` flag which passes port 8888 in the image (jupyter) to port 8888 
on our local machine. We also add a shared volume using the `-v` flag so that our current directory
is available inside the machine as `/host`.

```
docker pull kevz/konics:v2
docker run -it -p 8888:8888 -v $(pwd):/host kevz/konics:v2
```

If you want to get back to basics, you can always run `docker run -it kevz/konics:v2 bash` and do 
linux-y things, just for fun. The `konics` library is on the PYTHONPATH so you should be able to 
import it from any script.

## usage
Now that we have the latest and greatest version of `konics`, let's expore a bit. We'll load one 
of the 12 built-in maps and drive through it manually. Let's start by importing the map as well as 
the core `konics` objects.

```
from konics.maps import alfa
from konics.core import World, Drive, Track
```

The World object holds information about the sky, ground, and cones. If not explicitly set, the sky 
and ground textures will be randomly chosen. The Drive object is tied to a specific world instance 
and provides a car-like interface for moving through the world. Finally, we use the Track object to
turn the alfa map into an autocross track with randomly generated cones and scenery.

```
world = World()
drive = Drive(world)

track = Track(alfa.x_t, alfa.y_t, alfa.e_t)
track.add_to(world)
```

Now let's get the initial position for this track and move our driver there. The Track provides a 
get_pose method which computes the value and angle of the parametric functions at a given time. Be
careful not to confuse the "time" as used by the parametric equations with the actual time it takes
to drive through the track - these are two completely independent quantities.

```
initial_pose = track.get_pose(0.0)
drive.set_pose(initial_pose)
```

Now that our driver is in place, we can start driving through the track. The below code alternates
between turning slightly left and right as it drives forwards.

```
from scipy.misc import imsave

drive.move(0.1)
for i in range(10):
    imsave(str(i) + ".png", drive.render())
    drive.move(-0.2 if i % 2 == 0 else 0.2)
```

The end.
