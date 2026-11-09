package main

import (
	"bufio"
	"fmt"
	"os"
)

type instruction struct {
	op  string
	arg int
}

func run(program []instruction) (int, bool) {
	acc, ip := 0, 0
	seen := make([]bool, len(program))
	for ip < len(program) {
		if seen[ip] {
			return acc, false
		}
		seen[ip] = true
		switch in := program[ip]; in.op {
		case "acc":
			acc += in.arg
			ip++
		case "jmp":
			ip += in.arg
		default:
			ip++
		}
	}
	return acc, true
}

func main() {
	var program []instruction
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		var in instruction
		if _, err := fmt.Sscanf(scanner.Text(), "%s %d", &in.op, &in.arg); err == nil {
			program = append(program, in)
		}
	}
	acc, _ := run(program)
	fmt.Println(acc)
	swap := map[string]string{"jmp": "nop", "nop": "jmp"}
	for i, in := range program {
		if other, ok := swap[in.op]; ok {
			program[i].op = other
			if acc, done := run(program); done {
				fmt.Println(acc)
				return
			}
			program[i].op = in.op
		}
	}
}
