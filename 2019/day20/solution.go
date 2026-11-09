package main

import (
	"bufio"
	"fmt"
	"os"
)

type point struct{ x, y int }

func main() {
	var grid []string
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		grid = append(grid, scanner.Text())
	}
	at := func(x, y int) byte {
		if y < 0 || y >= len(grid) || x < 0 || x >= len(grid[y]) {
			return ' '
		}
		return grid[y][x]
	}
	letter := func(c byte) bool { return c >= 'A' && c <= 'Z' }
	portals := map[string][]point{}
	for y := range grid {
		for x := 0; x < len(grid[y]); x++ {
			if !letter(at(x, y)) {
				continue
			}
			if letter(at(x+1, y)) {
				name := string([]byte{at(x, y), at(x+1, y)})
				if at(x+2, y) == '.' {
					portals[name] = append(portals[name], point{x + 2, y})
				} else {
					portals[name] = append(portals[name], point{x - 1, y})
				}
			}
			if letter(at(x, y+1)) {
				name := string([]byte{at(x, y), at(x, y+1)})
				if at(x, y+2) == '.' {
					portals[name] = append(portals[name], point{x, y + 2})
				} else {
					portals[name] = append(portals[name], point{x, y - 1})
				}
			}
		}
	}
	jump := map[point]point{}
	for _, ends := range portals {
		if len(ends) == 2 {
			jump[ends[0]], jump[ends[1]] = ends[1], ends[0]
		}
	}
	start, goal := portals["AA"][0], portals["ZZ"][0]
	dist := map[point]int{start: 0}
	queue := []point{start}
	for len(queue) > 0 {
		p := queue[0]
		queue = queue[1:]
		if p == goal {
			fmt.Println(dist[p])
			return
		}
		next := []point{{p.x + 1, p.y}, {p.x - 1, p.y}, {p.x, p.y + 1}, {p.x, p.y - 1}}
		if q, ok := jump[p]; ok {
			next = append(next, q)
		}
		for _, q := range next {
			if _, seen := dist[q]; !seen && at(q.x, q.y) == '.' {
				dist[q] = dist[p] + 1
				queue = append(queue, q)
			}
		}
	}
}
