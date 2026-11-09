use std::io::Read;

fn main() {
    let mut text = String::new();
    std::io::stdin().read_to_string(&mut text).unwrap();
    let tiles: Vec<(i64, i64)> = text
        .lines()
        .filter_map(|l| l.split_once(','))
        .map(|(x, y)| (x.trim().parse().unwrap(), y.trim().parse().unwrap()))
        .collect();
    let mut best = 0;
    for (i, &(x1, y1)) in tiles.iter().enumerate() {
        for &(x2, y2) in &tiles[i + 1..] {
            best = best.max(((x1 - x2).abs() + 1) * ((y1 - y2).abs() + 1));
        }
    }
    println!("{}", best);
}
