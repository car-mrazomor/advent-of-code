use std::collections::{HashMap, HashSet};
use std::io::Read;

fn longest(at: usize, goal: usize, edges: &Vec<Vec<(usize, usize)>>, seen: &mut Vec<bool>) -> Option<usize> {
    if at == goal {
        return Some(0);
    }
    seen[at] = true;
    let mut best = None;
    for &(next, len) in &edges[at] {
        if !seen[next] {
            if let Some(rest) = longest(next, goal, edges, seen) {
                best = best.max(Some(len + rest));
            }
        }
    }
    seen[at] = false;
    best
}

fn main() {
    let mut text = String::new();
    std::io::stdin().read_to_string(&mut text).unwrap();
    let grid: Vec<Vec<u8>> = text.lines().filter(|l| !l.is_empty()).map(|l| l.bytes().collect()).collect();
    let (rows, cols) = (grid.len() as i32, grid[0].len() as i32);
    let open = |y: i32, x: i32| y >= 0 && y < rows && x >= 0 && x < cols && grid[y as usize][x as usize] != b'#';
    let dirs = [(0, 1, b'>'), (0, -1, b'<'), (1, 0, b'v'), (-1, 0, b'^')];
    let start = (0, grid[0].iter().position(|&c| c == b'.').unwrap() as i32);
    let end = (rows - 1, grid[rows as usize - 1].iter().position(|&c| c == b'.').unwrap() as i32);
    let mut nodes = vec![start, end];
    for y in 0..rows {
        for x in 0..cols {
            if open(y, x) && dirs.iter().filter(|(dy, dx, _)| open(y + dy, x + dx)).count() >= 3 {
                nodes.push((y, x));
            }
        }
    }
    let index: HashMap<(i32, i32), usize> = nodes.iter().enumerate().map(|(i, &p)| (p, i)).collect();
    let mut edges = vec![Vec::new(); nodes.len()];
    for (i, &(sy, sx)) in nodes.iter().enumerate() {
        let mut stack = vec![(sy, sx, 0usize)];
        let mut seen = HashSet::from([(sy, sx)]);
        while let Some((y, x, d)) = stack.pop() {
            if d > 0 {
                if let Some(&j) = index.get(&(y, x)) {
                    edges[i].push((j, d));
                    continue;
                }
            }
            let here = grid[y as usize][x as usize];
            for &(dy, dx, slope) in &dirs {
                let (ny, nx) = (y + dy, x + dx);
                if !open(ny, nx) || seen.contains(&(ny, nx)) || (here != b'.' && here != slope) {
                    continue;
                }
                seen.insert((ny, nx));
                stack.push((ny, nx, d + 1));
            }
        }
    }
    let mut seen = vec![false; nodes.len()];
    println!("{}", longest(0, 1, &edges, &mut seen).unwrap());
}
