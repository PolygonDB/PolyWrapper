use std::{process::{Stdio, Command, Child}, io::{Write, Read}, thread};

use pyo3::prelude::*;

#[pyclass]
struct Polygon {
    exechh: Child
}


#[pymethods]
impl Polygon {
    #[new]
    fn new(targetfile: String, debug: bool) -> Self {
        
        Polygon { exechh: setup(targetfile, debug) }
    }

    fn execute(&mut self, input: String) -> PyResult<String>{

        
        if let Some(ref mut stdin) = self.exechh.stdin.take() {
            stdin.write_all(input.as_bytes()).expect("Failed to write to stdin");
        }
    
        let mut output = String::new();
    

        if let Some(ref mut stdout) = self.exechh.stdout.take() {
            output = String::new();
            stdout.read_to_string(&mut output).expect("Failed to read from stdout");
        }
        

        Ok(output)
    }
}

fn setup (t: String, d: bool) -> Child {

    let child = Command::new(t)
        .stdin(Stdio::piped())
        .stdout(Stdio::piped())
        .stderr(Stdio::null())
        .spawn()
        .expect("Failed to start command");

    return child;
}

/// A Python module implemented in Rust.
#[pymodule]
fn Polyutils(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Polygon>()?;
    Ok(())
}