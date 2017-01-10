# konics
This is an autocross simulation engine for MIT AFSAE. For most users, you should run `konics` using
Docker to ensure consistent behavior. On the other hand, if you need every bit of performance, this
**should** work out-of-the box on macOS and Windows 10; if you use some other OS, you will need to
compile POV-Ray yourself and make sure the `povray` binary can be found on your PATH.

Note: The new `proton` rendering engine is much, much faster than `povray`. However, it doesn't run
on headless servers yet and is still experimental - I'm releasing it early because some people want
to train RL agents and `povray` is far too slow. If you want to try it out, download the app from
the experimental directory and run it - `konics` will automatically use `proton`.

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
Now that we have the latest and greatest version of `konics`, let's try importing the Drive object
which provides a car-like interface for moving through the simulated world and the make_wt helper 
function which makes it easy to dynamically generate a world and track from a map id.

* Note: Another option is to import the World and Track objects and manually construct a world by 
dynamically importing the map that you want. However, since dynamic imports are tricky and annoying
to use, we provide this helper method for loading the 12 built-in maps. *

```
from konics.core import Drive
from konics.utils import make_wt
```

We make a world-track tuple from map "alfa" - see letters A-L in the NATO phonetic alphabet for the
other map ids - and then create a Drive object for moving around in our new world. We also get the 
pose/position at time 0 for the track and move our driver there.

* Note: The time parameter as used in the parametric equations is independent of the actual time it
takes to drive around a track. One is a mathematical convenience, the other is how you win. *

```
world, track = make_wt("alfa")
drive = Drive(world)
drive.set_pose(track.get_pose(0.0))
```

Now that our world is ready and our driver is in place, we can start driving through the track. The 
below code alternates between turning slightly left and right, driving forwards and taking pictures
after each movement.

```
from scipy.misc import imsave

drive.move(0.1)
for i in range(10):
    imsave(str(i) + ".png", drive.render())
    drive.move(-0.2 if i % 2 == 0 else 0.2)
```

The end.
