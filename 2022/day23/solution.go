package main

import (
	"bufio"
	"fmt"
	"os"
)

type point struct{ x, y int }

func main() {
	elves := map[point]bool{}
	scanner := bufio.NewScanner(os.Stdin)
	for y := 0; scanner.Scan(); y++ {
		for x, c := range scanner.Text() {
			if c == '#' {
				elves[point{x, y}] = true
			}
		}
	}
	checks := [4][3]point{
		{{-1, -1}, {0, -1}, {1, -1}},
		{{-1, 1}, {0, 1}, {1, 1}},
		{{-1, -1}, {-1, 0}, {-1, 1}},
		{{1, -1}, {1, 0}, {1, 1}},
	}
	for round := 0; round < 10; round++ {
		proposals := map[point]point{}
		wanted := map[point]int{}
		for e := range elves {
			alone := true
			for dy := -1; dy <= 1 && alone; dy++ {
				for dx := -1; dx <= 1; dx++ {
					if (dx != 0 || dy != 0) && elves[point{e.x + dx, e.y + dy}] {
						alone = false
						break
					}
				}
			}
			if alone {
				continue
			}
			for k := 0; k < 4; k++ {
				side := checks[(round+k)%4]
				free := true
				for _, d := range side {
					if elves[point{e.x + d.x, e.y + d.y}] {
						free = false
					}
				}
				if free {
					target := point{e.x + side[1].x, e.y + side[1].y}
					proposals[e] = target
					wanted[target]++
					break
				}
			}
		}
		next := map[point]bool{}
		for e := range elves {
			if target, ok := proposals[e]; ok && wanted[target] == 1 {
				next[target] = true
			} else {
				next[e] = true
			}
		}
		elves = next
	}
	minX, minY, maxX, maxY := 1<<30, 1<<30, -1<<30, -1<<30
	for e := range elves {
		minX, maxX = min(minX, e.x), max(maxX, e.x)
		minY, maxY = min(minY, e.y), max(maxY, e.y)
	}
	fmt.Println((maxX-minX+1)*(maxY-minY+1) - len(elves))
}
