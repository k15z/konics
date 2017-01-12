from random import choice
from konics.maps import *
from konics.core import *
from konics.utils import *

fout = open("rewards.txt", "wt")
fout1 = open("moves.txt", "wt")

class RLGame(object):
    
    def __init__(self):
        self.mapid = ""
        self.total_moves = 0.0
        self.total_reward = 0.0
        self.reset()

    @property
    def name(self):
        return "kGame"
    
    @property
    def nb_actions(self):
        return 5
    
    def reset(self):
        fout.write(str(self.total_reward) + "\n")
        fout.flush()
        fout1.write(str(self.total_moves) + "\n")
        fout1.flush()

        self.total_moves = 0.0
        self.total_reward = 0.0
        self.mapid = choice(MAP_IDS)

        world, self.track = make_wt(self.mapid)
        self.drive = Drive(world)
        self.drive.set_pose(self.track.get_pose(0.1))
        self.on_track, self.right_dir, self.d, _ = self.track.evaluate(self.drive.pose)

    def play(self, action):
        if action == 0:
            self.drive.move(-0.1)
        elif action == 1:
            self.drive.move(-0.05)
        elif action == 2:
            self.drive.move(0.0)
        elif action == 3:
            self.drive.move(0.05)
        elif action == 4:
            self.drive.move(0.1)
        else:
            raise "Uh oh..."
        self.total_moves += 1
        self.total_reward += self.get_score()
        self.on_track, self.right_dir, self.d, _ = self.track.evaluate(self.drive.pose)

    def get_state(self):
        result = self.drive.render()[:,:,0]
        return result

    def get_score(self):
        if self.on_track and self.right_dir:
            return 1.0 / (self.d + 1.0)
        return 0.0

    def is_over(self):
        if self.is_won():
            return True
        if self.on_track and self.right_dir:
            return False
        return True

    def is_won(self):
        e_x, e_y, _ = self.track.get_pose(self.track.e_t)
        m_x, m_y, _ = self.drive.pose
        if abs(e_x - m_x) + abs(e_y - m_y) < 15.0:
            return True
        return False

    def get_frame(self):
        return self.get_state()

    def draw(self):
        return self.get_state()

    def get_possible_actions(self):
        return range(self.nb_actions)
