use std::{process::{Stdio, Command, Child}, io::{Write, Read}};

use pyo3::prelude::*;

#[pyclass]
struct Polygon {
    exechh: Command
}


#[pymethods]
impl Polygon {
    #[new]
    fn new(targetfile: String, debug: bool) -> Self {
        
        Polygon { exechh: setup(targetfile, debug) }
    }

    fn execute(&mut self, input: String) -> PyResult<String>{

        let mut run = self.exechh.spawn().expect("Failed to start command");
        
        if let Some(ref mut stdin) = run.stdin.take() {
            stdin.write_all(input.as_bytes()).expect("Failed to write to stdin");
        }
    
        let mut output = String::new();
    

        if let Some(ref mut stdout) = run.stdout.take() {
            output = String::new();
            stdout.read_to_string(&mut output).expect("Failed to read from stdout");
        }
        
        Ok(output)
    }
}

fn setup (t: String, d: bool) -> Command {
    let mut cmd = Command::new(t);
    cmd.stdin(Stdio::piped());
    cmd.stdout(Stdio::piped());
    if d { //debug mode
        cmd.stderr(Stdio::piped());
    } else {
        cmd.stderr(Stdio::null());
    }

    return cmd;
}

/// A Python module implemented in Rust.
#[pymodule]
fn Polyutils(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Polygon>()?;
    Ok(())
}