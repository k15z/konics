# konics
This is a brand new simulator designed to replace `cone-world` and `csim-server`. It gets rid of 
the awkward javascript-electron-localhost relay and provides a simple Python API for specifying 
and rendering autocross tracks. The easiest way to try it out is to spin up a Docker container 
and open a Jupyter notebook - this has been tested on macOS, Windows 10, and Ubuntu 16.

![right_cone.png](tests/_output/right_cone.png)
![track_0.png](tests/_output/track_0.png)
![parametrics.png](tests/_output/parametrics.png)

## usage
The below commands will (1) pull the latest version of `kevz/konics` from Docker Hub and (2) start 
the container and launch a new Jupyter instance on port 8888.

```
docker pull kevz/konics:v3
docker run -it -p 8888:8888 kevz/konics:v3 sh -c "jupyter notebook --ip='*' --no-browser"
```

If you navigate to `http://localhost:8888` in any web browser, you should see the standard Jupyter 
interface. For inspiration, check out the demo notebooks in the `examples` directory.

## tests
To run the tests, you need to be in the `tests` directory. Make sure to follow the instructions in
the console output and manually check the rendered images in `_output`.

```
cd konics/tests
python tests.py
```

## compatibility
It should work out-of-the-box on macOS and Windows 10 if you have the scipy stack installed. If you
don't have scipy, you should install it regardless of whether you intend to use `konics` or not 
just because it's awesome. If you are on some Linux varient, you will need to compile POV-Ray (or 
MegaPOV) yourself and make sure the `povray` binary can be found on the PATH. Finally, although the
simulator should work with both Python 2.7+ and Python 3, I only regularly test it on Python 3 so 
if somethings broken, let me know and I'll take a look.
