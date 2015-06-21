
extern crate getopts;
use getopts::{Options, Matches};
use std::env;

fn process(short_name: &str, default: &str, matches: &Matches) -> i32 {

    // Get value from options
    let result = match matches.opt_str(short_name) {
        Some(s) => s,
        None => String::from(default), 
    };

    // Convert to i32
    let num = match result.parse().ok() {
        Some(n) => n,
        None => { 0 },
    };

    // Return
    num
}

fn main() {
    let args: Vec<String> = env::args().collect();

    let mut opts = Options::new();
    opts.optopt("m", "mass", "Mass in kg", "");
    opts.optopt("a", "accel", "Acceleration in km/h", "");
    let matches = match opts.parse(&args[1..]) {
        Ok(m) => { m }
        Err(f) => { panic!(f.to_string()) }
    };

    // Process args, do some math
    let mass = process("m", "0", &matches);
    let accel = process("a", "0", &matches);
    let force = mass * accel;

    // Output!
    println!("F=M*A: {}={}*{}", force, mass, accel);

}
