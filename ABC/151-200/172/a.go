package main

import "fmt"

func main() {
	var a int
	fmt.Scan(&a)
	fmt.Printf("%d\n", a+a*a+a*a*a)
}
