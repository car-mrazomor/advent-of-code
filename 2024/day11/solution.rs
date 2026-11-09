use std::collections::HashMap;
use std::io::Read;

fn main() {
    let mut text = String::new();
    std::io::stdin().read_to_string(&mut text).unwrap();
    let mut stones: HashMap<u64, u64> = HashMap::new();
    for n in text.split_whitespace() {
        *stones.entry(n.parse().unwrap()).or_insert(0) += 1;
    }
    for _ in 0..25 {
        let mut next = HashMap::new();
        for (&stone, &count) in &stones {
            let digits = stone.to_string();
            let split = if stone == 0 {
                vec![1]
            } else if digits.len() % 2 == 0 {
                let (a, b) = digits.split_at(digits.len() / 2);
                vec![a.parse().unwrap(), b.parse().unwrap()]
            } else {
                vec![stone * 2024]
            };
            for s in split {
                *next.entry(s).or_insert(0) += count;
            }
        }
        stones = next;
    }
    println!("{}", stones.values().sum::<u64>());
}
