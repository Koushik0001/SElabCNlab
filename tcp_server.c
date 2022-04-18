#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>

int main()
{
	//create TCP socket
	int server_socket = socket(AF_INET, SOCK_STREAM, 0);

	//specify an address for the server socket
	struct sockaddr_in server_address;
	server_address.sin_family = AF_INET;
	server_address.sin_port = htons(9002);
	server_address.sin_addr.s_addr = INADDR_ANY;

	//binding the server address to the socket
    bind(server_socket,(struct sockaddr *)&server_address,sizeof(server_address));

	//listening to the socket
    listen(server_socket,5);

	//accepting the connection request from the socket
    int client_socket = accept(server_socket,NULL, NULL);

	char message[256];//for storing the received message

	//receive data from the client
    int recv_status = recv(client_socket,message,sizeof(message),0);
	if(recv_status<0)
		printf("***Receive failure.***\n");
	else
		printf("***Receive success***\n");

	//print the received message
	printf("Received message : %s\n",message);

	//echo the data to the client
	int sending_status = send(client_socket,&message,sizeof(message),0);
	if(sending_status<0)
		printf("***Sending failure.***\n");
	else
		printf("***Sent successfully***\n");

	close(server_socket);
	return 0;
}