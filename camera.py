import numpy as np
from settings import *


class Camera:
    def __init__(self, position, yaw, pitch):
        self.position = np.array(position, dtype=np.float32)
        self.yaw = np.radians(yaw)
        self.pitch = np.radians(pitch)

        self.up = np.array([0, 1, 0], dtype=np.float32)
        self.right = np.array([1, 0, 0], dtype=np.float32)
        self.forward = np.array([0, 0, -1], dtype=np.float32)

        self.m_proj = self.perspective(V_FOV, ASPECT_RATIO, NEAR, FAR)
        self.m_view = np.eye(4, dtype=np.float32)

    def update(self):
        self.update_vectors()
        self.update_view_matrix()

    def update_view_matrix(self):
        self.m_view = self.look_at(self.position, self.position + self.forward, self.up)

    def update_vectors(self):
        self.forward[0] = np.cos(self.yaw) * np.cos(self.pitch)
        self.forward[1] = np.sin(self.pitch)
        self.forward[2] = np.sin(self.yaw) * np.cos(self.pitch)

        self.forward = self.normalize(self.forward)
        self.right = self.normalize(np.cross(self.forward, np.array([0, 1, 0], dtype=np.float32)))
        self.up = self.normalize(np.cross(self.right, self.forward))

    def rotate_pitch(self, delta_y):
        self.pitch -= delta_y
        self.pitch = np.clip(self.pitch, -PITCH_MAX, PITCH_MAX)

    def rotate_yaw(self, delta_x):
        self.yaw += delta_x

    def move_left(self, velocity):
        return -self.right[:2] * velocity

    def move_right(self, velocity):
        return self.right[:2] * velocity

    def move_up(self, velocity):
        self.position += self.up * velocity

    def move_down(self, velocity):
        self.position -= self.up * velocity

    def move_forward(self, velocity):
        return self.forward[:2] * velocity

    def move_back(self, velocity):
        return -self.forward[:2] * velocity

    @staticmethod
    def perspective(fov, aspect, near, far):
        tan_half_fov = np.tan(fov / 2)
        return np.array([
            [1 / (aspect * tan_half_fov), 0, 0, 0],
            [0, 1 / tan_half_fov, 0, 0],
            [0, 0, -(far + near) / (far - near), -1],
            [0, 0, -(2 * far * near) / (far - near), 0]
        ], dtype=np.float32)

    @staticmethod
    def look_at(eye, center, up):
        f = Camera.normalize(center - eye)
        s = Camera.normalize(np.cross(f, up))
        u = np.cross(s, f)

        result = np.eye(4, dtype=np.float32)
        result[0, :3] = s
        result[1, :3] = u
        result[2, :3] = -f
        result[:3, 3] = -np.dot(result[:3, :3], eye)
        return result

    @staticmethod
    def normalize(v):
        norm = np.linalg.norm(v)
        if norm == 0:
            return v
        return v / norm
