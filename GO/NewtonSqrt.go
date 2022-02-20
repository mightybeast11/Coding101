package main

import (
	"fmt"
	"math"
)

func Sqrt(x float64) float64 {
	z := 1.0
	for i := 1; math.Abs(z*z-x) >= 0.00000001; i++ {
		z -= (z*z - x) / (2 * z) // use derivative of z^2 to make adjustment on z
		fmt.Printf("Iteration %v\n", i)
	}
	return z
}

func main() {
	fmt.Println(Sqrt(2))
}
