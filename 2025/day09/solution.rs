use std::collections::VecDeque;
use std::io::Read;

fn area(a: (i64, i64), b: (i64, i64)) -> i64 {
    ((a.0 - b.0).abs() + 1) * ((a.1 - b.1).abs() + 1)
}

fn sorted_unique(mut v: Vec<i64>) -> Vec<i64> {
    v.sort();
    v.dedup();
    v
}

fn main() {
    let mut text = String::new();
    std::io::stdin().read_to_string(&mut text).unwrap();
    let tiles: Vec<(i64, i64)> = text
        .lines()
        .filter_map(|l| l.split_once(','))
        .map(|(x, y)| (x.trim().parse().unwrap(), y.trim().parse().unwrap()))
        .collect();

    let mut best = 0;
    for (i, &a) in tiles.iter().enumerate() {
        for &b in &tiles[i + 1..] {
            best = best.max(area(a, b));
        }
    }
    println!("{}", best);

    // Part 2: the rectangle has to stay inside the loop. Compress the coordinates (each used x/y
    // becomes an odd index, the gaps between them even ones, with padding at both ends), draw the
    // loop, flood-fill the outside, then check every rectangle with a prefix sum of outside cells.
    let xs = sorted_unique(tiles.iter().map(|t| t.0).collect());
    let ys = sorted_unique(tiles.iter().map(|t| t.1).collect());
    let (w, h) = (2 * xs.len() + 1, 2 * ys.len() + 1);
    let pts: Vec<(usize, usize)> = tiles
        .iter()
        .map(|&(x, y)| (2 * xs.binary_search(&x).unwrap() + 1, 2 * ys.binary_search(&y).unwrap() + 1))
        .collect();

    let mut wall = vec![vec![false; w]; h];
    for i in 0..pts.len() {
        let (a, b) = (pts[i], pts[(i + 1) % pts.len()]);
        for y in a.1.min(b.1)..=a.1.max(b.1) {
            for x in a.0.min(b.0)..=a.0.max(b.0) {
                wall[y][x] = true;
            }
        }
    }

    let mut outside = vec![vec![false; w]; h];
    let mut queue = VecDeque::from([(0usize, 0usize)]);
    outside[0][0] = true;
    while let Some((x, y)) = queue.pop_front() {
        for (nx, ny) in [(x.wrapping_sub(1), y), (x + 1, y), (x, y.wrapping_sub(1)), (x, y + 1)] {
            if nx < w && ny < h && !outside[ny][nx] && !wall[ny][nx] {
                outside[ny][nx] = true;
                queue.push_back((nx, ny));
            }
        }
    }

    // sum[y][x] = number of outside cells in rows 0..y and columns 0..x
    let mut sum = vec![vec![0i32; w + 1]; h + 1];
    for y in 0..h {
        for x in 0..w {
            sum[y + 1][x + 1] = sum[y][x + 1] + sum[y + 1][x] - sum[y][x] + outside[y][x] as i32;
        }
    }

    let mut best = 0;
    for i in 0..pts.len() {
        for j in i + 1..pts.len() {
            let (a, b) = (pts[i], pts[j]);
            let (x0, x1) = (a.0.min(b.0), a.0.max(b.0) + 1);
            let (y0, y1) = (a.1.min(b.1), a.1.max(b.1) + 1);
            if sum[y1][x1] - sum[y0][x1] - sum[y1][x0] + sum[y0][x0] == 0 {
                best = best.max(area(tiles[i], tiles[j]));
            }
        }
    }
    println!("{}", best);
}
