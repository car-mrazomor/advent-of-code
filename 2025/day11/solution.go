package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	outputs := map[string][]string{}
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		if name, rest, ok := strings.Cut(scanner.Text(), ":"); ok {
			outputs[name] = strings.Fields(rest)
		}
	}
	paths := map[string]int{"out": 1}
	var count func(string) int
	count = func(device string) int {
		if n, ok := paths[device]; ok {
			return n
		}
		total := 0
		for _, next := range outputs[device] {
			total += count(next)
		}
		paths[device] = total
		return total
	}
	fmt.Println(count("you"))
}
