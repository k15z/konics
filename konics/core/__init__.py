from .track import *
from .drive import *
from .world import *

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(0.2)
try:
    s.connect(("localhost", 3000))
    print("Detected rendering server. Using hardware accelerated rendering engine.")
except:
    print("Failed to detect rendering server. Falling back to ray-tracing renderer.")
