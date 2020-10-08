package main

import (
	"fmt"
)

func main() {
	n := 1345679
	breakDown(n)
}

func breakDown(m int) {
	result := make([]int, 0)
	mult := 1
	
	for m > 0 {
		last_digit := m % 10
		result = append(result, last_digit * mult)
		
		m /= 10
		mult *= 10
	}
	
	for i := len(result) - 1; i >= 0; i-- {
		fmt.Println(result[i])
	}
}