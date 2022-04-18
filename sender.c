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
char frames[25][11];
char data[100];
void getData()
{
    //char data[100];
    printf("Enter Data : ");
    gets(data);
}
void MakeFrame(int* numberOfFrames)
{
    //char frames[25][10];
    int len = strlen(data);
    int i = 0;
    int frameIndex= 0;
    while(data[i] != '\0')
    {   
        frames[frameIndex][0] = '*';
        frames[frameIndex][1] = '*';
        frames[frameIndex][2] = '*';
        frames[frameIndex][7] = '*';
        frames[frameIndex][8] = '*';
        frames[frameIndex][9] = '*';
        int j;
        for(j=3; j<7; j++)
        {
            frames[frameIndex][j] = data[i];
            i++;
        }
        frames[frameIndex][j] = '\0';
	if(i>len)
		break;
	else
        	frameIndex++;
    }
    *numberOfFrames = frameIndex+1;
}

void SendFrame(int client_socket,int numberOfFrames)
{
    for(int i=0;i<numberOfFrames;i++)
    {
        if(send(client_socket,data,11,MSG_WAITALL)<0)
		printf("Facing problem in sending the message...\n");
    }
	printf("number of frames : %d\n",numberOfFrames);
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
	inet_aton(argv[1],&server_address.sin_addr);

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
        if(send(client_socket,frames[i],11,MSG_WAITALL)<0)
                printf("Facing problem in sending the message...\n");

    }
	//SendFrame(client_socket,numberOfFrames);

	close(server_socket);
	return 0;
}
