import numpy as np
from settings import H_WALL_SIZE


class GameObject:
    def __init__(self, level_map, tex_id, x, z):
        self.eng = level_map.eng
        self.app = self.eng.app
        self.tex_id = tex_id
        #
        self.pos = np.array([x + H_WALL_SIZE, 0, z + H_WALL_SIZE], dtype=np.float32)  # center of the tile
        self.rot = 0
        self.scale = np.array([1, 1, 1], dtype=np.float32)
        #
        self.m_model = None

    def get_model_matrix(self):
        m_model = np.eye(4, dtype=np.float32)
        m_model[:3, 3] = self.pos
        m_model = self.rotate(m_model, self.rot, np.array([0, 1, 0], dtype=np.float32))
        m_model = self.scale_matrix(m_model, self.scale)
        return m_model

    @staticmethod
    def rotate(matrix, angle, axis):
        c, s = np.cos(angle), np.sin(angle)
        axis = axis / np.linalg.norm(axis)
        temp = (1 - c) * axis

        rot = np.array([
            [c + temp[0] * axis[0], temp[0] * axis[1] + s * axis[2], temp[0] * axis[2] - s * axis[1], 0],
            [temp[1] * axis[0] - s * axis[2], c + temp[1] * axis[1], temp[1] * axis[2] + s * axis[0], 0],
            [temp[2] * axis[0] + s * axis[1], temp[2] * axis[1] - s * axis[0], c + temp[2] * axis[2], 0],
            [0, 0, 0, 1]
        ], dtype=np.float32)

        return np.dot(matrix, rot)

    @staticmethod
    def scale_matrix(matrix, scale):
        scale_matrix = np.eye(4, dtype=np.float32)
        scale_matrix[0, 0] = scale[0]
        scale_matrix[1, 1] = scale[1]
        scale_matrix[2, 2] = scale[2]
        return np.dot(matrix, scale_matrix)
