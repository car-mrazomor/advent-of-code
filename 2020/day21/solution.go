package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	type food struct {
		ingredients map[string]bool
		allergens   []string
	}
	var foods []food
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		if line == "" {
			continue
		}
		parts := strings.SplitN(strings.TrimSuffix(line, ")"), " (contains ", 2)
		f := food{ingredients: map[string]bool{}}
		for _, ingredient := range strings.Fields(parts[0]) {
			f.ingredients[ingredient] = true
		}
		if len(parts) == 2 {
			f.allergens = strings.Split(parts[1], ", ")
		}
		foods = append(foods, f)
	}
	candidates := map[string]map[string]bool{}
	for _, f := range foods {
		for _, allergen := range f.allergens {
			if candidates[allergen] == nil {
				candidates[allergen] = map[string]bool{}
				for ingredient := range f.ingredients {
					candidates[allergen][ingredient] = true
				}
				continue
			}
			for ingredient := range candidates[allergen] {
				if !f.ingredients[ingredient] {
					delete(candidates[allergen], ingredient)
				}
			}
		}
	}
	risky := map[string]bool{}
	for _, set := range candidates {
		for ingredient := range set {
			risky[ingredient] = true
		}
	}
	count := 0
	for _, f := range foods {
		for ingredient := range f.ingredients {
			if !risky[ingredient] {
				count++
			}
		}
	}
	fmt.Println(count)
}
