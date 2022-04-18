#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>

#include <sys/time.h>
#include <sys/select.h>

/*
WaitForEvent()  //wait for frame arrival
ReceiveFrame(), //Receive frame from sender
ExtractData()   //Extrct data from received frame
DeliverData()   //Deliver data to transport layer
*/
//int WaitForEvent(int receiver_socket)
//{
//    fd_set current_sockets;
//    FD_ZERO(&current_sockets);
//    FD_SET(receiver_socket,&current_sockets);
//
//    if(select(1,&current_sockets,NULL,NULL,NULL)>0)
//        return 1;
//    else
//	return 0;
//}
void ReceiveFrame(int receiver_socket,char* received_data)
{
    //static char received_data[1028];
    if(recv(receiver_socket,received_data,11,0)<0)
	printf("problem in receiving data\n");
}
void ExtractData(char* receivedFrame,char* received_Data)
{
    //static char received_Data[1028];
    received_Data[0] = receivedFrame[3];
    received_Data[1] = receivedFrame[4];
    received_Data[2] = receivedFrame[5];
    received_Data[3] = receivedFrame[6];
}
void deliverData(char* receivedData)
{
    printf("Received Data : %s\n",receivedData);
}
int main(int argc, char **argv)
{
    //create a socket
	int receiver_socket = socket(AF_INET, SOCK_STREAM, 0);

	//specify an address for the sender socket
	struct sockaddr_in sender_address;
	sender_address.sin_family = AF_INET;
	sender_address.sin_port = htons(5500);
	inet_aton(argv[1],&sender_address.sin_addr);

	int connection_status = connect(receiver_socket,(struct sockaddr*) &sender_address,sizeof(sender_address));
	if(connection_status <0)// check for any error in making the connection
    {
		printf("There is a problem in making connection\n");
        exit(1);
    }
	int i=0;
    while(i<4)
    {
        char *receivedFrame = (char*)malloc(11);
        ReceiveFrame(receiver_socket,receivedFrame);
       	char *extractedData = (char*) malloc(11); 
        ExtractData(receivedFrame,extractedData);
        deliverData(extractedData);
	    i++;
    }
	close(receiver_socket);
	return 0;
}
