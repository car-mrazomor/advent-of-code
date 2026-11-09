package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	total := 0
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		colon := strings.Index(line, ":")
		if colon < 0 {
			continue
		}
		halves := strings.Split(line[colon+1:], "|")
		winning := map[string]bool{}
		for _, n := range strings.Fields(halves[0]) {
			winning[n] = true
		}
		points := 0
		for _, n := range strings.Fields(halves[1]) {
			if winning[n] {
				if points == 0 {
					points = 1
				} else {
					points *= 2
				}
			}
		}
		total += points
	}
	fmt.Println(total)
}
