use std::collections::HashSet;
use std::io::Read;

fn main() {
    let row: i64 = std::env::args().nth(1).map_or(2_000_000, |a| a.parse().unwrap());
    let mut text = String::new();
    std::io::stdin().read_to_string(&mut text).unwrap();
    let mut spans = Vec::new();
    let mut beacons = HashSet::new();
    for line in text.lines() {
        let n: Vec<i64> = line
            .split(|c: char| !(c.is_ascii_digit() || c == '-'))
            .filter_map(|s| s.parse().ok())
            .collect();
        if n.len() < 4 {
            continue;
        }
        let reach = (n[0] - n[2]).abs() + (n[1] - n[3]).abs() - (n[1] - row).abs();
        if reach >= 0 {
            spans.push((n[0] - reach, n[0] + reach));
        }
        if n[3] == row {
            beacons.insert(n[2]);
        }
    }
    spans.sort();
    let (mut covered, mut end) = (0i64, i64::MIN);
    for (a, b) in spans {
        let start = a.max(end + 1);
        if b >= start {
            covered += b - start + 1;
            end = b;
        }
    }
    println!("{}", covered - beacons.len() as i64);
}
