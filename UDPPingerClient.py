
import socket
import time

def main():
    # Server details
    server_host = '127.0.0.1'  # localhost
    server_port = 12000
    
    # Create UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Set socket timeout to 1 second
    client_socket.settimeout(1.0)
    
    # Send 10 ping messages
    for sequence_number in range(1, 11):
        # Record the time when sending the message
        send_time = time.time()
        
        # Create the ping message
        message = f"Ping {sequence_number} {send_time}"
        
        try:
            # Send the ping message to the server
            client_socket.sendto(message.encode(), (server_host, server_port))
            
            # Try to receive the response from the server
            response, server_address = client_socket.recvfrom(1024)
            
            # Record the time when receiving the response
            receive_time = time.time()
            
            # Calculate round-trip time (RTT)
            rtt = receive_time - send_time
            
            # Print the response and RTT
            print(f"Reply from {server_address[0]}: {response.decode()}")
            print(f"RTT: {rtt:.6f} seconds")
            
        except socket.timeout:
            # Handle timeout - packet was lost
            print(f"Request {sequence_number} timed out")
        
        except Exception as e:
            # Handle any other exceptions
            print(f"Error occurred: {e}")
    
    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    main()