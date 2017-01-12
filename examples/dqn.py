"""
This example trains a DQN to drive through the tracks.
"""
from keras.models import Sequential, load_model
from keras.layers import *
from keras.optimizers import *
from qlearning4k import Agent

MY_DIR = path.dirname(path.abspath(__file__))
sys.path.insert(0, path.abspath(MY_DIR + '/..'))
from konics.rl import RLGame

nb_frames = 1
nb_actions = 5
COLD_START = True
if COLD_START:
    model = Sequential()
    model.add(Convolution2D(8, 3, 3, activation='relu', dim_ordering="th", input_shape=(nb_frames, 256, 256)))
    model.add(Convolution2D(8, 3, 3, subsample=(2,2), activation='relu', dim_ordering="th"))
    model.add(Convolution2D(16, 3, 3, subsample=(2,2), activation='relu', dim_ordering="th"))
    model.add(Convolution2D(16, 3, 3, subsample=(2,2), activation='relu', dim_ordering="th"))
    model.add(Convolution2D(32, 3, 3, subsample=(2,2), activation='relu', dim_ordering="th"))
    model.add(Convolution2D(32, 3, 3, subsample=(2,2), activation='relu', dim_ordering="th"))
    model.add(Convolution2D(32, 3, 3, subsample=(2,2), activation='relu', dim_ordering="th"))
    model.add(Flatten())
    model.add(Dense(nb_actions))
    model.compile(RMSprop(), 'MSE')
else:
    model = load_model("model.h5")

rlgame = RLGame()
agent = Agent(model=model, memory_size=10000, nb_frames=nb_frames)
agent.train(rlgame, batch_size=64, nb_epoch=200, gamma=0.7)
model.save("model.h5")
agent.play(rlgame)
