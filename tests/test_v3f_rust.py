from plant_rs import Vector3f

import time

import tabulate

import numpy as np


log = {}


def make_v3f(x, y, z):
    return Vector3f(x, y, z)


def test_make_v3f():
    t = []
    for _ in range(1_000):
        t0 = time.time()
        v = make_v3f(1, 2, 3)
        t.append(time.time() - t0)

    log["make_v3f"] = np.mean(np.asarray(t))


def test_set_v3f():
    v = Vector3f(1, 2, 3)

    assert v.x == 1
    assert v.y == 2
    assert v.z == 3


def test_add_op():
    u = make_v3f(1, 2, 3)
    v = make_v3f(3, 2, 1)

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
    u = make_v3f(1, 2, 3)
    v = make_v3f(3, 2, 1)

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
        f.write("\n# Rust\n")
        f.write(table)
        f.write("\n")

