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
GetData()   //get data from network layer
MakeFrame() //make frame
SendFrame() //sedFrame to receiver
*/
#define frameSize 13
#define ackSize 2
#define dataSize 10

char frames[25][frameSize];
char data[100];
void getData()
{
    printf("Enter Data : ");
    scanf("%[^\n]s",data);
}
void MakeFrame(int* numberOfFrames)
{
    int len = strlen(data);
    int i = 0;
    int frameIndex= 0;
    int numberOfChars = 0;
    while(data[i] != '\0')
    {   
        numberOfChars = 0;
        frames[frameIndex][0] = (char)frameIndex;
        int j;
        for(j=2; j<dataSize+2; j++)
        {
            if(data[i]!= '\0')
            {
                frames[frameIndex][j] = data[i];
                i++;
                numberOfChars++;
            }
            else
                break;
        }
	    frames[frameIndex][1] = (char)(dataSize+3);
	    if(i>len-1)
	    {
	    	frames[frameIndex][dataSize+2] = '1';
	    	frames[frameIndex][1] =  (char)(3 + numberOfChars);
	    	break;
	    }
	    else
	    {
	    	frames[frameIndex][12] = '0';
            frameIndex++;
	    }
    }
    *numberOfFrames = frameIndex+1;
}

int main(int argc, char **argv)
{
    char server_message[256] = "Hi,I am from server.";
	//create a socket
	int server_socket = socket(AF_INET, SOCK_STREAM, 0);

	//specify an address for the server socket
	struct sockaddr_in server_address;
	server_address.sin_family = AF_INET;
	server_address.sin_port = htons(5500);
	server_address.sin_addr.s_addr = INADDR_ANY;

   	int bind_status = bind(server_socket,(struct sockaddr *)&server_address,sizeof(server_address));
	if(bind_status<0)
		printf("Problem in binding\n");
    listen(server_socket,5);


    int client_socket = accept(server_socket,NULL, NULL);
    if(client_socket < 0)
	printf("There is problem in accepting the connction...\n");
	
    getData();
    int numberOfFrames = 1;
	
    MakeFrame(&numberOfFrames);

    for(int i=0;i<numberOfFrames;i++)
    {
        if(send(client_socket,frames[i],frameSize,MSG_WAITALL)<0)
            printf("Facing problem in sending the message...\n");
        char *ack = malloc(0);
        recv(client_socket,ack,ackSize,0);
        if(ack[0] == '1')
            printf("%c th frame acknoledged.\n",ack[1]);
        else
            printf("%c th frame lost.\n",ack[1]);
    }
	close(server_socket);
	return 0;
}
