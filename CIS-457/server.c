/* A simple server in the internet domain using TCP
   The port number is passed as an argument */
#include <stdio.h>
#include <sys/types.h> 
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <strings.h>
#include <unistd.h>

void error(char *msg)
{
    perror(msg);
    exit(1);
}

int main(int argc, char *argv[])
{
     int sockfd, newsockfd, portno, clilen;
     char buffer[1001];
     struct sockaddr_in serv_addr, cli_addr;
     int n;
  /* end loop */
     if (argc < 2) {
         fprintf(stderr,"ERROR, no port provided\n");
         exit(1);
     }
     
     sockfd = socket(AF_INET, SOCK_STREAM, 0);

     if (sockfd < 0) 
        error("ERROR opening socket");

     bzero((char *) &serv_addr, sizeof(serv_addr)); 
	/* erases the data in the n bytes of the memory*/

     portno = atoi(argv[1]);
     serv_addr.sin_family = AF_INET;
     serv_addr.sin_addr.s_addr = INADDR_ANY;
     serv_addr.sin_port = htons(portno);
	/* Host to net byte order for short int*/

     if (bind(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0) 
              error("ERROR on binding");

     /* add loop */
    while(1){

     listen(sockfd,5);
	/* 5 outstanding connections*/

     clilen = sizeof(cli_addr);

     newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, &clilen);

     if (newsockfd < 0) 
          error("ERROR on accept");

     bzero(buffer,1001);
     n = read(newsockfd, buffer, 1001);

     if (n < 0) error("ERROR reading from socket");

     printf("Here is the message: %s\n",buffer);

     n = write(newsockfd, "I got your message", 18);

     if (n < 0) error("ERROR writing to socket");

     close(newsockfd);

     }
     
     /* end loop */

     return 0; 
}
