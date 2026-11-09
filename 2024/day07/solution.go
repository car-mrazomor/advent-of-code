package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func possible(target int, values []int, acc int) bool {
	if len(values) == 0 {
		return acc == target
	}
	if acc > target {
		return false
	}
	return possible(target, values[1:], acc+values[0]) || possible(target, values[1:], acc*values[0])
}

func main() {
	total := 0
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		parts := strings.SplitN(scanner.Text(), ":", 2)
		if len(parts) != 2 {
			continue
		}
		target, _ := strconv.Atoi(parts[0])
		var values []int
		for _, field := range strings.Fields(parts[1]) {
			n, _ := strconv.Atoi(field)
			values = append(values, n)
		}
		if possible(target, values[1:], values[0]) {
			total += target
		}
	}
	fmt.Println(total)
}
