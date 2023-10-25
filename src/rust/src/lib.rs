use pyo3::prelude::*;

#[derive(Clone)]
#[pyclass]
struct Vector3f {
    #[pyo3(get, set)]
    x: f64,
    #[pyo3(get, set)]
    y: f64, 
    #[pyo3(get, set)]
    z: f64,
}

#[pymethods]
impl Vector3f {
    #[new]
    fn new(x: f64, y: f64, z: f64) -> Self {
        Vector3f {
            x: x,
            y: y,            
            z: z,
        }
    }

    #[pyo3(name = "__repr__")]
    fn repr(&self) -> String {
        format!("[{}, {}, {}]", self.x, self.y, self.z).to_string()
    }

    #[pyo3(name = "__add__")]
    fn add(&self, v: Vector3f) -> Self {
        return Vector3f {
            x: self.x + v.x,
            y: self.y + v.y,
            z: self.z + v.z,
        }
    }

    #[pyo3(name = "__sub__")]
    fn sub(&self, v: Vector3f) -> Self {
        return Vector3f {
            x: self.x - v.x,
            y: self.y - v.y,
            z: self.z - v.z,
        }
    }
}

#[pymodule]
fn plant_rs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Vector3f>()?;

    Ok(())
}
