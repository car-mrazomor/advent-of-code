package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	parent := map[string]string{}
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		if pair := strings.Split(strings.TrimSpace(scanner.Text()), ")"); len(pair) == 2 {
			parent[pair[1]] = pair[0]
		}
	}
	total := 0
	for object := range parent {
		for p, ok := parent[object]; ok; p, ok = parent[p] {
			total++
		}
	}
	fmt.Println(total)
}
