package main

import (
	"fmt"
	"log"
	"net"
	"strings"
)

func main() {
	addr, err := net.ResolveUDPAddr("udp", "localhost:8080")
	if err != nil {
		log.Fatalln(err)
	}
	conn, err := net.ListenUDP("udp", addr)
	if err != nil {
		log.Println(err)
	}
	defer conn.Close()

	for {
		buf := make([]byte, 1024)
		n, clientAddr, err := conn.ReadFromUDP(buf)
		if err != nil {
			log.Println("Error reading:", err)
			continue
		}

		message := strings.TrimSpace(string(buf[:n]))
		fmt.Printf("Received from %s: %q\n", clientAddr, message)

		if message == "q" || message == "Q" {
			fmt.Println("Exit command received. Shutting down server.")
			break
		}

		_, err = conn.WriteToUDP([]byte("Hey client!"), clientAddr)
		if err != nil {
			log.Println("Error writing:", err)
		}
	}

	fmt.Println("Server stopped.")
}
