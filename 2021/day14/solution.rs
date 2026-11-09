use std::collections::HashMap;
use std::io::Read;

fn main() {
    let mut text = String::new();
    std::io::stdin().read_to_string(&mut text).unwrap();
    let mut lines = text.lines();
    let template: Vec<char> = lines.next().unwrap().trim().chars().collect();
    let rules: HashMap<(char, char), char> = lines
        .filter_map(|l| l.split_once(" -> "))
        .map(|(pair, insert)| {
            let p: Vec<char> = pair.chars().collect();
            ((p[0], p[1]), insert.chars().next().unwrap())
        })
        .collect();
    let mut pairs: HashMap<(char, char), u64> = HashMap::new();
    for w in template.windows(2) {
        *pairs.entry((w[0], w[1])).or_insert(0) += 1;
    }
    for _ in 0..10 {
        let mut next = HashMap::new();
        for (&(a, b), &n) in &pairs {
            match rules.get(&(a, b)) {
                Some(&c) => {
                    *next.entry((a, c)).or_insert(0) += n;
                    *next.entry((c, b)).or_insert(0) += n;
                }
                None => *next.entry((a, b)).or_insert(0) += n,
            }
        }
        pairs = next;
    }
    let mut counts: HashMap<char, u64> = HashMap::new();
    for (&(a, _), &n) in &pairs {
        *counts.entry(a).or_insert(0) += n;
    }
    *counts.entry(*template.last().unwrap()).or_insert(0) += 1;
    println!("{}", counts.values().max().unwrap() - counts.values().min().unwrap());
}
