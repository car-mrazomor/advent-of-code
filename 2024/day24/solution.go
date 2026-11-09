package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strings"
)

type gate struct{ a, op, b string }

func main() {
	values := map[string]int{}
	gates := map[string]gate{}
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		if name, v, ok := strings.Cut(line, ": "); ok {
			values[name] = int(v[0] - '0')
		} else if left, out, ok := strings.Cut(line, " -> "); ok {
			f := strings.Fields(left)
			gates[out] = gate{f[0], f[1], f[2]}
		}
	}
	var value func(string) int
	value = func(name string) int {
		if v, ok := values[name]; ok {
			return v
		}
		g := gates[name]
		a, b := value(g.a), value(g.b)
		switch g.op {
		case "AND":
			values[name] = a & b
		case "OR":
			values[name] = a | b
		default:
			values[name] = a ^ b
		}
		return values[name]
	}
	var zs []string
	for name := range gates {
		if strings.HasPrefix(name, "z") {
			zs = append(zs, name)
		}
	}
	sort.Strings(zs)
	result := 0
	for i := len(zs) - 1; i >= 0; i-- {
		result = result*2 + value(zs[i])
	}
	fmt.Println(result)
}
