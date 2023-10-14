use std::{process::{Stdio, Command, Child}, io::{Write, Read}};

use pyo3::{prelude::*, types::PyList, PyNativeType};

#[pyclass]
struct Polygon {
    exechh: Child
}


#[pymethods]
impl Polygon {
    #[new]
    fn new(targetfile: String) -> Self {
        
        Polygon { exechh: setup(targetfile) }
    }

    fn execute(&mut self, input: String) -> PyResult<String>{
        if let Some(mut stdin) = self.exechh.stdin.take() {
            stdin.write_all(input.as_bytes()).expect("Failed to write to stdin");
        }
    
        let mut output = String::new();
    
        // Read data from the program's stdout
        if let Some(mut stdout) = self.exechh.stdout.take() {
            output = String::new();
            stdout.read_to_string(&mut output).expect("Failed to read from stdout");
        }
        Ok(output)
    }
}

fn setup (t: String) -> Child {
    let mut cmd = Command::new(t);
    cmd.stdin(Stdio::piped());
    cmd.stdout(Stdio::piped());
    cmd.stderr(Stdio::null());
    return cmd.spawn().expect("Failed to start command");
}

/// A Python module implemented in Rust.
#[pymodule]
fn Polyutils(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Polygon>()?;
    Ok(())
}