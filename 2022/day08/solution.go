package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	var grid []string
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		if line := strings.TrimSpace(scanner.Text()); line != "" {
			grid = append(grid, line)
		}
	}
	rows, cols := len(grid), len(grid[0])
	visible := 0
	for y := 0; y < rows; y++ {
		for x := 0; x < cols; x++ {
			h := grid[y][x]
			for _, d := range [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}} {
				ny, nx, clear := y+d[0], x+d[1], true
				for ny >= 0 && ny < rows && nx >= 0 && nx < cols {
					if grid[ny][nx] >= h {
						clear = false
						break
					}
					ny, nx = ny+d[0], nx+d[1]
				}
				if clear {
					visible++
					break
				}
			}
		}
	}
	fmt.Println(visible)
}
