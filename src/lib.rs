use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

[#pyfunction]
fn say_hello() {
    println!("Saying hello from Rust!");
}

#[pymodule]
fn fib_rs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(say_hello));
    Ok(())
}
