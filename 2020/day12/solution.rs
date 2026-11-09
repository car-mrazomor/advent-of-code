use std::io::Read;

fn main() {
    let mut text = String::new();
    std::io::stdin().read_to_string(&mut text).unwrap();
    let (mut x, mut y, mut dx, mut dy) = (0i64, 0i64, 1i64, 0i64);
    for line in text.lines().filter(|l| !l.is_empty()) {
        let (action, value) = line.split_at(1);
        let v: i64 = value.parse().unwrap();
        match action {
            "N" => y += v,
            "S" => y -= v,
            "E" => x += v,
            "W" => x -= v,
            "F" => {
                x += dx * v;
                y += dy * v;
            }
            "L" | "R" => {
                for _ in 0..v / 90 {
                    (dx, dy) = if action == "L" { (-dy, dx) } else { (dy, -dx) };
                }
            }
            _ => unreachable!(),
        }
    }
    println!("{}", x.abs() + y.abs());
}
