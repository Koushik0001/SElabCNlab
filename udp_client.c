#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>

int main(int argc, char** argv)
{
    char *messege;
    char *received_messege;
    char terminate[] = "#end";

    int clientSocket = socket(AF_INET,SOCK_DGRAM,0);

    //filling up structure with server address
    struct sockaddr_in server_address;
    memset(&server_address, 0, sizeof(server_address));
    server_address.sin_port = htons(8080);
    inet_aton(argv[1],&server_address.sin_addr);

    unsigned int len = sizeof(server_address);

    while(1)
    {   
        received_messege = (char*) malloc(1024 * sizeof(char));
        messege = (char*)malloc(1024 * sizeof(char));

        printf("Me : ");
        gets(messege);;
        int n = sendto(clientSocket,(char*)messege,strlen(messege),0,(struct sockaddr*)&server_address,sizeof(server_address));
        if(n<0)
        {
            printf("Some Error Occurred, message could not be sent...\n");
        }

        recvfrom(clientSocket,(const char*)received_messege,1024,0,(struct sockaddr*)&server_address, NULL);
        
        if(strcmp(received_messege,"#end\nh") == 0)
            exit(0);
        printf("Server : %s\n",received_messege);
        free(received_messege);
        free(messege);
        
    }
    
    return 0;
}
