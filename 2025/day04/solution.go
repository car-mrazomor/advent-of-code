package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	var grid [][]byte
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		if line := strings.TrimSpace(scanner.Text()); line != "" {
			grid = append(grid, []byte(line))
		}
	}
	accessible := func() [][2]int {
		var found [][2]int
		for y := range grid {
			for x := range grid[y] {
				if grid[y][x] != '@' {
					continue
				}
				around := 0
				for dy := -1; dy <= 1; dy++ {
					for dx := -1; dx <= 1; dx++ {
						ny, nx := y+dy, x+dx
						if (dy != 0 || dx != 0) && ny >= 0 && ny < len(grid) && nx >= 0 && nx < len(grid[ny]) && grid[ny][nx] == '@' {
							around++
						}
					}
				}
				if around < 4 {
					found = append(found, [2]int{y, x})
				}
			}
		}
		return found
	}
	first := accessible()
	fmt.Println(len(first))
	removed := 0
	for batch := first; len(batch) > 0; batch = accessible() {
		for _, p := range batch {
			grid[p[0]][p[1]] = '.'
		}
		removed += len(batch)
	}
	fmt.Println(removed)
}
