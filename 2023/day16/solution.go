package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type beam struct{ x, y, dx, dy int }

func main() {
	var grid []string
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		if line := strings.TrimSpace(scanner.Text()); line != "" {
			grid = append(grid, line)
		}
	}
	seen := map[beam]bool{}
	energized := map[[2]int]bool{}
	stack := []beam{{-1, 0, 1, 0}}
	for len(stack) > 0 {
		b := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		x, y := b.x+b.dx, b.y+b.dy
		if y < 0 || y >= len(grid) || x < 0 || x >= len(grid[y]) {
			continue
		}
		var next []beam
		switch grid[y][x] {
		case '/':
			next = []beam{{x, y, -b.dy, -b.dx}}
		case '\\':
			next = []beam{{x, y, b.dy, b.dx}}
		case '|':
			if b.dx != 0 {
				next = []beam{{x, y, 0, 1}, {x, y, 0, -1}}
			} else {
				next = []beam{{x, y, b.dx, b.dy}}
			}
		case '-':
			if b.dy != 0 {
				next = []beam{{x, y, 1, 0}, {x, y, -1, 0}}
			} else {
				next = []beam{{x, y, b.dx, b.dy}}
			}
		default:
			next = []beam{{x, y, b.dx, b.dy}}
		}
		energized[[2]int{x, y}] = true
		for _, n := range next {
			if !seen[n] {
				seen[n] = true
				stack = append(stack, n)
			}
		}
	}
	fmt.Println(len(energized))
}
