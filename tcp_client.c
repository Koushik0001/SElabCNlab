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
    //create a socket
	int client_socket = socket(AF_INET, SOCK_STREAM, 0);

	//specify an address for the server socket
	struct sockaddr_in server_address;
	server_address.sin_family = AF_INET;
	server_address.sin_port = htons(9002);
	server_address.sin_addr.s_addr = INADDR_ANY;

	//Connection request to server
	int connection_status = connect(client_socket,(struct sockaddr*) &server_address,sizeof(server_address));
	if(connection_status <0)// check for any error in making the connection
		printf("There is a problem in making connection\n");

	char text[] = "abcde";	//character array to store sending message
	char rtext[100];		//character array to store received message

	//send data to server
	int sending_status = send(client_socket,&text,sizeof(text),0);
	if(sending_status<0)
		printf("***Sending failure.***\n");
	else
		printf("***Sent successfully***\n");

	//receive data from the server
	int recv_status = recv(client_socket, &rtext, sizeof(rtext),0);
	if(recv_status<0)
		printf("***Receive failure.***\n");
	else
		printf("***Receive success***\n");

	//print the data that we got
	printf("Echoed Message : %s\n",rtext);

	//close the socket
	close(client_socket);
	return 0;
}
