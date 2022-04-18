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
#define frameSize 13
#define ackSize 2
#define dataSize 10
/*
ReceiveFrame(), //Receive frame from sender
ExtractData()   //Extrct data from received frame
DeliverData()   //Deliver data to transport layer
*/
int sequenceNumber = 0;
void ReceiveFrame(int receiver_socket,char* received_data)
{
    //static char received_data[1028];
    if(recv(receiver_socket,received_data,13,0)<0)
	printf("\n");
}
int ExtractData(int* sequenceNumber,char* receivedFrame,char* received_Data)
{
    //static char received_Data[1028];
    *sequenceNumber = (int)(receivedFrame[0]);
    
    for(int i=2; i<12; i++)    
   	 received_Data[i-2] = receivedFrame[i];
 	
    received_Data[10] = '\0'; 
    return receivedFrame[12];
}
void deliverData(char* receivedData)
{
    printf("%s",receivedData);
}
int main(int argc, char **argv)
{
    //create a socket
	int receiver_socket = socket(AF_INET, SOCK_STREAM, 0);

	//specify an address for the sender socket
	struct sockaddr_in sender_address;
	sender_address.sin_family = AF_INET;
	sender_address.sin_port = htons(5500);
	sender_address.sin_addr.s_addr = INADDR_ANY;

	int connection_status = connect(receiver_socket,(struct sockaddr*) &sender_address,sizeof(sender_address));
	if(connection_status <0)// check for any error in making the connection
    {
		printf("There is a problem in making connection\n");
        exit(1);
    }
	char ack[2];
	ack[0] = '1';

	char nack[2];
	nack[0] = '0';

    while(1)
    {
		int sequenceNumber_received = 0;
        char *receivedFrame = (char*)malloc(frameSize);

        ReceiveFrame(receiver_socket,receivedFrame);
       	char *extractedData = (char*) malloc(dataSize); 
        char isLastFrame = ExtractData(&sequenceNumber_received,receivedFrame,extractedData);
        deliverData(extractedData);
		if(sequenceNumber == sequenceNumber_received)
		{
			ack[1] = (char)(sequenceNumber+'0');
			send(receiver_socket,ack,ackSize,0);
		}
		else
		{
			nack[1] = (char)(sequenceNumber+'0');
			send(receiver_socket,nack,ackSize,0);
		}
		if(isLastFrame == '1')
			break;
		sequenceNumber++;
    }
	close(receiver_socket);
	return 0;
}
