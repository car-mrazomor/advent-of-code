package main

import (
	"fmt"
	"io"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	data, _ := io.ReadAll(os.Stdin)
	var crabs []int
	for _, field := range strings.Split(strings.TrimSpace(string(data)), ",") {
		n, _ := strconv.Atoi(field)
		crabs = append(crabs, n)
	}
	sort.Ints(crabs)
	median := crabs[len(crabs)/2]
	fuel := 0
	for _, c := range crabs {
		if c > median {
			fuel += c - median
		} else {
			fuel += median - c
		}
	}
	fmt.Println(fuel)
}
