#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int cidrFinder(int oct);
int modifyBit(int oct, int pos, int bit);
void netAndbc(int inputoct[],int hostbits, int bit);

int main(){
    char decision = 'y';
    while(decision == 'y'){
        //Enter your address
        char addressMessage[] = "Enter your IP address: ";
        int placementLimit = 1;
        int assignmentLimit = 4;
        unsigned char oct1,oct2,oct3,oct4;
        printf("%s",addressMessage);
        scanf("%hhu.%hhu.%hhu.%hhu", &oct1,&oct2,&oct3,&oct4);
        int ipOcts[4] = {oct1,oct2,oct3,oct4};
        
        //Enter your subnet mask
        char subnetMessage[] = "Enter your Subnet Mask: ";
        printf("%s",subnetMessage);
        scanf("%hhu.%hhu.%hhu.%hhu", &oct1,&oct2,&oct3,&oct4);
        int subOcts[4] = {oct1,oct2,oct3,oct4};
        
        //find cidr
        int oneCounter = 0;
        for(int aCounter = 0; aCounter < assignmentLimit; aCounter++){
            oneCounter += cidrFinder(subOcts[aCounter]);
        }
        
        // Network address
        int hostbits = 32 - oneCounter;
        int netSize = pow(2, hostbits);
        int octCounter = 3;
        int posCounter = 0;
        int net1=ipOcts[0],net2=ipOcts[1],net3=ipOcts[2],net4=ipOcts[3];
        int netOcts[4] = {net1,net2,net3,net4};
        printf("Network address: ");
        netAndbc(netOcts, hostbits, 0);
        // Broadcast address
        int bc1=ipOcts[0],bc2=ipOcts[1],bc3=ipOcts[2],bc4=ipOcts[3];
        int bcOcts[4] = {bc1,bc2,bc3,bc4};
        printf("Broadcast address: ");
        netAndbc(bcOcts, hostbits, 1);
        
        //Size of the network
        printf("Size of the network: %d\n", netSize );
        
        //First usuable ip address:
        printf("First usuable IP address: ");
        netAndbc(netOcts, 1,1);
        
        //Last usuable ip address:
        printf("Last usuable IP address: ");
        netAndbc(bcOcts, 1,0);
        
        //CIDR prefix: EX:/23
        printf("CIDR prefix: /%d\n", oneCounter);
        
        //Do you wish to continue (y/n)?:y
        printf("Do you wish to continue (y/n)?:\n");
        scanf(" %c",&decision);
    }
    
    return 0;
}

int cidrFinder(int oct){
    int bin = 0, rem = 0, place = 1, oneCounter = 0;
    while(oct){
        rem = oct % 2;
        oct = oct / 2;
        bin = bin + (rem * place);
        place = place * 10;
        if(place * rem > 0){
            oneCounter += 1;
        }
    }
    return oneCounter; 
}

int modifyBit(int oct, int pos, int bit){
    int mask = 1 << pos;
    return ((oct & ~mask) | (bit << pos));
}

void netAndbc(int inputoct[],int hostbits, int bit){
    int octCounter = 3;
    int posCounter = 0;
   
    for(int hbCounter = 0; hbCounter < hostbits; hbCounter++){
        if(hbCounter != 0 && hbCounter % 8 == 0){
            octCounter -= 1;
            posCounter = 0;
        }
        inputoct[octCounter] = modifyBit(inputoct[octCounter],posCounter,bit);
        posCounter++;
    }
    printf("%d.%d.%d.%d\n",inputoct[0],inputoct[1],inputoct[2],inputoct[3]);
}

