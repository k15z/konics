# konics
This is a brand new simulator designed to replace `cone-world` and `csim-server`. It gets rid of 
the awkward javascript-electron-localhost relay and provides a simple Python API for specifying 
and rendering autocross tracks.

![track_0.png](tests/_output/track_0.png)
![track_1.png](tests/_output/track_1.png)
![track_2.png](tests/_output/track_2.png)

To get the best performance, you should get macOS, install Python 3, and run this natively. But if
you just want to play around with `konics`, you can use the Docker image I wrote and hope I didn't 
mess things up too badly.

## usage
The below commands will (1) pull the latest version of `kevz/konics` from Docker Hub and (2) start 
the container and start a new Jupyter instance on `http://localhost:8888`.

```
docker pull kevz/konics:v2
docker run -it -p 8888:8888 kevz/konics:v2 sh -c "jupyter notebook --ip='*' --no-browser"
```

If you navigate to `http://localhost:8888` in any web browser, you should see the standard Jupyter 
interface. For inspiration, check out the demo notebooks in the root directory.

## tests
To run the tests, you need to be in the `tests` directory. Make sure to follow the instructions in
the console output and manually check the rendered images in `_output`.

```
cd konics/tests
python tests.py
```
