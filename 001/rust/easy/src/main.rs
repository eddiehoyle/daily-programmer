use std::io;

/// Asks user a question
///
/// # Example
///
/// ```
/// let name = read_input("What is your name?");
/// println!("Your name is: {}", name)
/// ```
fn read_input(question: &str) -> String {

    // Ask user a question
    println!("{}", question);

    // Accept input
    let mut stdin = io::stdin();
    let mut buffer = String::new();
    stdin.read_line(&mut buffer).unwrap();

    // Remove new lines...?
    buffer.replace("\n", "")
}

fn main() {

    // Ask questions
    let name = read_input("What is your name?");
    let age = read_input("How old are you?");
    let username = read_input("What is your Reddit username?");

    // Format sentence
    let sentence = format!("Your name is {name}, you are {age} year(s) old and your username is {username}", name=name, age=age, username=username);
    println!("{:?}", sentence);
}
