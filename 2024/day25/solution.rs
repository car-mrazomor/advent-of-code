use std::io::Read;

fn main() {
    let mut text = String::new();
    std::io::stdin().read_to_string(&mut text).unwrap();
    let (mut locks, mut keys) = (Vec::new(), Vec::new());
    for block in text.trim().split("\n\n") {
        let rows: Vec<&[u8]> = block.lines().map(|l| l.as_bytes()).collect();
        let heights: Vec<usize> = (0..rows[0].len())
            .map(|c| rows.iter().filter(|r| r[c] == b'#').count() - 1)
            .collect();
        if rows[0].iter().all(|&b| b == b'#') {
            locks.push(heights);
        } else {
            keys.push(heights);
        }
    }
    let fits = locks
        .iter()
        .flat_map(|l| keys.iter().map(move |k| l.iter().zip(k).all(|(a, b)| a + b <= 5)))
        .filter(|&ok| ok)
        .count();
    println!("{}", fits);
}
