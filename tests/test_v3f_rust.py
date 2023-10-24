from plant_rs import Vector3f

import time


def test_timer():
    t0 = time.time()
    v = Vector3f(1, 2, 3)
    print(f"--- Rust vector: {time.time() - t0} seconds ---")


def test_elements():
    v = Vector3f(1, 2, 3)

    assert v.x == 1
    assert v.y == 2
    assert v.z == 3

