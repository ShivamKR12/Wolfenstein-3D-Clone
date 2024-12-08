import numpy as np
from meshes.quad_mesh import QuadMesh
from game_objects.game_object import GameObject
from settings import *


class Item(GameObject):
    def __init__(self, level_map, tex_id, x, z):
        super().__init__(level_map, tex_id, x, z)

        self.scale = np.array([ITEM_SETTINGS[tex_id]['scale']], dtype=np.float32)
        #
        self.m_model = self.get_model_matrix()
