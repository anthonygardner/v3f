from pathlib import Path

from structs import Vector3f as v3f

import ctypes
import pytest
import time

import tabulate

import numpy as np

import structs


log = {}

def make_v3f(x, y, z):
    return v3f(x, y, z)

u = v3f(1, 2, 3)
v = v3f(3, 2, 1)

def test_make_v3f():
    t =[]
    for _ in range(1_000):
        t0 = time.time()
        w = make_v3f(1, 2, 3)
        t.append(time.time() - t0)

    log["make_v3f"] = np.mean(np.asarray(t))

def test_set_v3f():
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


def test_add_op():
    t = []
    for _ in range(1_000):
        t0 = time.time()
        w = u + v
        t.append(time.time() - t0)

    log["add_op"] = np.mean(np.asarray(t))

    assert w.x == 4
    assert w.y == 4
    assert w.z == 4


def test_sub_op():
    t = []
    for _ in range(1_000):
        t0 = time.time()
        w = u - v
        t.append(time.time() - t0)

    log["sub_op"] = np.mean(np.asarray(t))

    assert w.x == -2
    assert w.y == 0
    assert w.z == 2

    table = tabulate.tabulate(
        [log],
        headers="keys",
        tablefmt="pipe",
    )

    with open("README.md", "a") as f:
        f.write("# C\n")
        f.write(table)
        f.write("\n")

