# konics
This is a brand new simulator designed to replace `cone-world` and `csim-server`. It gets rid of 
the awkward javascript-electron-localhost relay and provides a simple Python API for specifying 
and rendering autocross tracks.

To get the best performance, you should get macOS, install Python 3, and run this natively. But if
you just want to play around with `konics`, you can use the Docker image I wrote and hope I didn't 
mess things up too badly.

## usage
The below commands will (1) pull the latest version of `kevz/konics` for Docker Hub and (2) start 
the container and create a new Jupyter notebook. You should be able to open http://localhost:8888/
and create a new Python notebook.

```
docker pull kevz/konics:v2
docker run -it -p 8888:8888 kevz/konics:v2 sh -c "jupyter notebook --ip='*' --no-browser"
```

Paste the below code into your Python notebook and hit `shift-enter` to run it. After a second or 
two - we are making some fairly high resolution images - it should show the three frames where we
drive forwards and turn left.

```
from konics import *
import matplotlib.pyplot as plt

# Build a track
track = Track(size=1024, sky="Shadow_Clouds", ground="Asphalt")
for i in range(10):
    track.add(Cone(-10, 20*i))
    track.add(Cone( 10, 20*i))
track.add(Cone(-15, 40, 0))
track.add(Cone( 15, 40, 180))

# Drive around on it
drive = Drive(track)
plt.imshow(drive.render())
plt.show()
drive.forward()
plt.imshow(drive.render())
plt.show()
drive.rotate(0.1)
plt.imshow(drive.render())
plt.show()
```

## tests
To run the tests, you need to be in the `tests` directory. Make sure to follow the instructions in
the console output and manually check the rendered images in `_output`.

```
cd konics/tests
python tests.py
```

## examples
![track_0.png](tests/_output/track_0.png)
![track_1.png](tests/_output/track_1.png)
![track_2.png](tests/_output/track_2.png)
