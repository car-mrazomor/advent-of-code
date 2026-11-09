use std::io::Read;

fn next_value(values: &[i64]) -> i64 {
    if values.iter().all(|&v| v == 0) {
        return 0;
    }
    let diffs: Vec<i64> = values.windows(2).map(|w| w[1] - w[0]).collect();
    values[values.len() - 1] + next_value(&diffs)
}

fn main() {
    let mut text = String::new();
    std::io::stdin().read_to_string(&mut text).unwrap();
    let total: i64 = text
        .lines()
        .filter(|l| !l.trim().is_empty())
        .map(|l| next_value(&l.split_whitespace().map(|n| n.parse().unwrap()).collect::<Vec<i64>>()))
        .sum();
    println!("{}", total);
}
