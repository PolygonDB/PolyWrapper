use std::{process::{Stdio, Command}, io::{Write, Read}};

use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn execute(input: String) -> PyResult<String> {
    // Command to run a program (e.g., "echo" in this example)
    let mut cmd = Command::new("./polygondb.exe");

    // Set up stdin, stdout, and stderr
    cmd.stdin(Stdio::piped());
    cmd.stdout(Stdio::piped());

    // Start the command
    let mut child = cmd.spawn().expect("Failed to start command");

    // Write data to the program's stdin
    if let Some(mut stdin) = child.stdin.take() {
        stdin.write_all(input.as_bytes()).expect("Failed to write to stdin");
    }

    let mut output = String::new();

    // Read data from the program's stdout
    if let Some(mut stdout) = child.stdout.take() {
        output = String::new();
        stdout.read_to_string(&mut output).expect("Failed to read from stdout");
        println!("Program output: {}", output);
    }

    // Wait for the command to finish
    let status = child.wait().expect("Failed to wait for command");
    if status.success() {
        Ok(output)
    } else {
        Ok("Fail".to_string())
    }
}

/// A Python module implemented in Rust.
#[pymodule]
fn Polyutils(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(execute, m)?)?;
    Ok(())
}