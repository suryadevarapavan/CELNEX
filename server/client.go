package main

import (
	"fmt"
	"log"
	"net"
	"time"
)

func getmsg() (string, bool) {
  var message string
  fmt.Print("Enter Message {Enter q or Q to exit}: ")
  fmt.Scanln(&message)

  if message == "q" || message == "Q" {
    return message , false
  } else {
    return message, true
		}
}

func main() {
	// Create UDP connection
	conn, err := net.Dial("udp", "localhost:8080")
	if err != nil {
		log.Fatalln(err)
	}
	defer conn.Close()

	for {
		message, ok := getmsg()
		if !ok {
			fmt.Println("Exiting...")
			break
		}

		// Send message to the server
		_, err := conn.Write([]byte(message))
		if err != nil {
			log.Fatalln("Error sending message:", err)
		}
		fmt.Println("Sent:", message)

		// Set read deadline to avoid blocking indefinitely
		conn.SetReadDeadline(time.Now().Add(5 * time.Second))

		// Receive response from server
		buf := make([]byte, 1024)
		n, err := conn.Read(buf)
		if err != nil {
			log.Println("Error reading from server:", err)
			continue // just continue to next iteration instead of exit
		}

		// Print the server's response
		fmt.Println("Received:", string(buf[:n]))
	}
}

