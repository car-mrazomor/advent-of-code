use std::collections::HashMap;
use std::io::Read;

type Recipes = HashMap<String, (i64, Vec<(i64, String)>)>;

fn parse_term(term: &str) -> (i64, String) {
    let mut it = term.trim().split_whitespace();
    let amount = it.next().unwrap().parse().unwrap();
    (amount, it.next().unwrap().to_string())
}

fn ore_for(recipes: &Recipes, fuel: i64) -> i64 {
    let mut need: HashMap<String, i64> = HashMap::new();
    need.insert("FUEL".into(), fuel);
    let mut ore = 0;
    while let Some((name, amount)) = need.iter().find(|(n, a)| **a > 0 && n.as_str() != "ORE").map(|(n, a)| (n.clone(), *a)) {
        let (made, inputs) = &recipes[&name];
        let batches = (amount + made - 1) / made;
        *need.get_mut(&name).unwrap() -= batches * made;
        for (count, input) in inputs {
            if input == "ORE" {
                ore += count * batches;
            } else {
                *need.entry(input.clone()).or_insert(0) += count * batches;
            }
        }
    }
    ore
}

fn main() {
    let mut text = String::new();
    std::io::stdin().read_to_string(&mut text).unwrap();
    let mut recipes: Recipes = HashMap::new();
    for line in text.lines().filter(|l| l.contains("=>")) {
        let (left, right) = line.split_once("=>").unwrap();
        let (made, name) = parse_term(right);
        recipes.insert(name, (made, left.split(',').map(parse_term).collect()));
    }
    println!("{}", ore_for(&recipes, 1));
}
