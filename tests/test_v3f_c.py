from pathlib import Path

from structs import Vector3f as v3f

import ctypes
import pytest
import time

import structs


u = v3f(1, 2, 3)
v = v3f(3, 2, 1)

def test_timer():
    t0 = time.time()
    w = v3f(1, 2, 3)
    print(f"--- C vector: {time.time() - t0} seconds ---")

def test_v3f_assignments():
    assert u.x == 1
    assert u.y == 2
    assert u.z == 3

    assert v.x == 3
    assert v.y == 2
    assert v.z == 1


def test_add_v3f():
    w = structs.add_v3f(u, v)

    assert w.x == 4
    assert w.y == 4
    assert w.z == 4


def test_sub_v3f():
    w = structs.sub_v3f(u, v)

    assert w.x == -2
    assert w.y == 0
    assert w.z == 2


def test_cross_v3f():
    w = structs.cross_v3f(u, v)

    assert w.x == -4
    assert w.y == 8
    assert w.z == -4


def test_dot_v3f():
    s = structs.dot_v3f(u, v)

    assert s == 10


def test_mag_v3f():
    s = structs.mag_v3f(v)

    assert s == pytest.approx(3.7416575)


def test_add_operator():
    w = u + v

    assert w.x == 4
    assert w.y == 4
    assert w.z == 4

