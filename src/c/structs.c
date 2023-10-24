#include <assert.h>
#include <math.h>

#include "structs.h"


Vector3f add_v3f(Vector3f u, Vector3f v) {
    Vector3f w = {
        u.x + v.x,
        u.y + v.y,
        u.z + v.z
    };

    return w;
}

Vector3f sub_v3f(Vector3f u, Vector3f v) {
    Vector3f w = {
        u.x - v.x,
        u.y - v.y,
        u.z - v.z
    };

    return w;
}

Vector3f cross_v3f(Vector3f u, Vector3f v) {
    Vector3f w = {
        u.y * v.z - u.z * v.y,
        u.z * v.x - u.x * v.z,
        u.x * v.y - u.y * v.x
    };

    return w;
}

float dot_v3f(Vector3f u, Vector3f v) {
    float d = u.x * v.x + u.y * v.y + u.z * v.z;
    return d;
}

float mag_v3f(Vector3f v) {
    float m = sqrt(v.x * v.x + v.y * v.y + v.z * v.z);
    return m;
}

