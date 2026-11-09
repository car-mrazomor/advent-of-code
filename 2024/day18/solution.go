package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	size, count := 70, 1024
	if len(os.Args) > 2 {
		size, _ = strconv.Atoi(os.Args[1])
		count, _ = strconv.Atoi(os.Args[2])
	}
	blocked := map[[2]int]bool{}
	scanner := bufio.NewScanner(os.Stdin)
	for i := 0; i < count && scanner.Scan(); i++ {
		var x, y int
		if _, err := fmt.Sscanf(scanner.Text(), "%d,%d", &x, &y); err == nil {
			blocked[[2]int{x, y}] = true
		}
	}
	dist := map[[2]int]int{{0, 0}: 0}
	queue := [][2]int{{0, 0}}
	for len(queue) > 0 {
		p := queue[0]
		queue = queue[1:]
		if p == [2]int{size, size} {
			fmt.Println(dist[p])
			return
		}
		for _, d := range [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}} {
			q := [2]int{p[0] + d[0], p[1] + d[1]}
			if q[0] < 0 || q[1] < 0 || q[0] > size || q[1] > size || blocked[q] {
				continue
			}
			if _, seen := dist[q]; !seen {
				dist[q] = dist[p] + 1
				queue = append(queue, q)
			}
		}
	}
}
