extern crate getopts;
use getopts::{Options, Matches};
use std::env;

// fn do_work(inp: &str, out: Option<String>) {
//     println!("{}", inp);
//     match out {
//         Some(x) => println!("{}", x),
//         None => println!("No Output"),
//     }
// }

// fn print_usage(program: &str, opts: Options) {
//     let brief = format!("Usage: {} FILE [options]", program);
//     print!("{}", opts.usage(&brief));
// }

/// Parse command line options
fn parse_opts(args: &Vec<String>) -> Matches {
    let mut opts = Options::new();
    opts.optopt("w", "", "Say some words", "WORDS");
    opts.optflag("h", "help", "print this help menu");

    let matches = match opts.parse(&args[1..]) {
        Ok(m) => { m }
        Err(f) => { panic!(f.to_string()) }
    };

    matches
}
fn main() {
    let args: Vec<String> = env::args().collect();
    // let program = args[0].clone();

    let opts = parse_opts(&args);
    if opts.opt_present("w") {
        let words = opts.opt_str("w");
        match words {
            Some(x) => println!("Words: {}", x),
            None => (),
        }
    }

    // if matches.opt_present("h") {
    //     print_usage(&program, opts);
    //     return;
    // }
    // let output = matches.opt_str("o");
    // let input = if !matches.free.is_empty() {
    //     matches.free[0].clone()
    // } else {
    //     print_usage(&program, opts);
    //     return;
    // };
    // do_work(&input, output);
}