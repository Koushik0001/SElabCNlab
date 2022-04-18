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
    int server_socket = socket(AF_INET,SOCK_DGRAM,0);

    char *message; 
    char *received_message;
    char terminate[] = "#end";
    //filling up structure for server socket address
    struct sockaddr_in server_address;
    memset(&server_address, 0, sizeof(server_address));
    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(8080);
    inet_aton(argv[1],&server_address.sin_addr);

    //binding server socket to the socket address
    bind(server_socket,(const struct sockaddr*)&server_address,sizeof(server_address));

    struct sockaddr_in client_address;
    memset(&client_address, 0, sizeof(client_address));

    int len = sizeof(client_address);
    
    while(1)
    {
        received_message = (char*)malloc(1024 * sizeof(char));
        message = (char*)malloc(1024 * sizeof(char));

        int n = recvfrom(server_socket,(char *)received_message,1024,0,(struct sockaddr*)&client_address,&len);
        printf("\nCleint : %s\n",received_message);

        if(strcmp(received_message,"#end\n")==0)
            exit(1);


        printf("Me : ");
        gets(message);
    
        sendto(server_socket,(const char*)message, strlen(message),0,(const struct sockaddr*)&client_address,sizeof(client_address));
        free(message);
        free(received_message);
    }
    return 0;
}
