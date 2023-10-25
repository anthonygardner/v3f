from __future__ import annotations
from pathlib import Path

import ctypes


libc = ctypes.CDLL(
    Path().absolute() / "build" / "structs.so"
)


class Vector3f(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("z", ctypes.c_float),
    ]

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"[{self.x}, {self.y}, {self.z}]"

    def __add__(self, u: Vector3f) -> Vector3f:

        def add_v3f(self: Vector3f, v: Vector3f) -> Vector3f:
            c_add = libc.__getattr__('add_v3f')

            c_add.argtypes = (Vector3f, Vector3f)
            c_add.restype = Vector3f

            return c_add(self, u)

        return add_v3f(self, u)

    def __sub__(self, u: Vector3f) -> Vector3f:
        c_sub = libc.__getattr__('sub_v3f')

        c_sub.argtypes = (Vector3f, Vector3f)
        c_sub.restype = Vector3f

        return c_sub(self, u)


def add_v3f(u: Vector3f, v: Vector3f) -> Vector3f:
    c_add = libc.__getattr__('add_v3f')

    c_add.argtypes = (Vector3f, Vector3f)
    c_add.restype = Vector3f

    return c_add(u, v)


def sub_v3f(u: Vector3f, v: Vector3f) -> Vector3f:
    c_sub = libc.__getattr__('sub_v3f')

    c_sub.argtypes = (Vector3f, Vector3f)
    c_sub.restype = Vector3f

    return c_sub(u, v)


def cross_v3f(u: Vector3f, v: Vector3f) -> Vector3f:
    c_cross = libc.__getattr__('cross_v3f')

    c_cross.argtypes = (Vector3f, Vector3f)
    c_cross.restype = Vector3f

    return c_cross(u, v)


def dot_v3f(u: Vector3f, v: Vector3f) -> float:
    c_dot = libc.__getattr__('dot_v3f')

    c_dot.argtypes = (Vector3f, Vector3f)
    c_dot.restype = ctypes.c_float

    return c_dot(u, v)


def mag_v3f(v: Vector3f) -> float:
    c_mag = libc.__getattr__('mag_v3f')

    c_mag.argtypes = (Vector3f,)
    c_mag.restype = ctypes.c_float

    return c_mag(v)

