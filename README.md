# konics
This is a brand new simulator designed to replace `cone-world` and `csim-server`. It gets rid of 
the awkward javascript-electron-localhost relay and provides a simple Python API for specifying 
and rendering autocross tracks.

## usage
```
from konics import *
from scipy.misc import imsave

track = Track()
for i in range(10):
    track.add(Cone(-10, 20*i))
    track.add(Cone( 10, 20*i))
track.add(Cone(-15, 40, 0))
track.add(Cone( 15, 40, 180))

look_at = (0, 100)
location = (0, i*10 - 10)
image = track.render(location, look_at)
imsave("result.png", image)
```

## examples
![front.png](examples/front.png)
![angle.png](examples/angle.png)
