#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
int newCIDR(int oldCIDR, int subnet);
int modifyBit(int oct, int pos, int bit);
void netModifier(int netOcts[], int position, int firstOct);
void bcModifier(int netOcts[], int position, int bit);

int main(){
    //IP input
    char networkMessage[] = "Enter network address: ";
    unsigned int oct1, oct2, oct3, oct4;
    printf("%s", networkMessage);
    scanf("%d.%d.%d.%d", &oct1, &oct2, &oct3, &oct4);
    int netOcts[4] = {oct1, oct2, oct3, oct4};
    //CIDR input
    char cidrMessage[] = "Enter CIDR: ";
    unsigned int cidr;
    printf("%s", cidrMessage);
    scanf("%d", &cidr);
    // Subnet input
    char subnetNumMessage[] = "Number of subnets: ";
    unsigned int subnet;
    printf("%s", subnetNumMessage);
    scanf("%d", &subnet);

    int nextCIDR = newCIDR(cidr, subnet);
    int position = 32-nextCIDR;
    int netSize = pow(2,position);
    int subCounter = 0;
    int printingOrder = 2;
    //first subnet
    printf("1) Subnet\n");
    netModifier(netOcts, 0,1);
    bcModifier(netOcts,position,1);
    printf("Size of the network: %d\n", netSize);
    printf("CIDR prefix: /%d\n", nextCIDR);
    //other subnets
    while(subCounter < subnet-1){
        printf("%d) Subnet\n", printingOrder);
        netModifier(netOcts, position,0);
        printf("Size of the network: %d\n", netSize);
        printf("CIDR prefix: /%d\n", nextCIDR);
        printingOrder++;
        subCounter++;
    }
   
}

int newCIDR(int oldCIDR,int subnet){
    int expo1 = 32 - oldCIDR;
    int powerValue = pow(2,expo1);
    float divisor = floor(log2(powerValue/subnet));
    int floorDivisor = divisor;
    int newCIDR = 32 - floorDivisor;
    return newCIDR;
}

int modifyBit(int oct, int pos, int bit)
{
    int mask = 1 << pos;
    return ((oct & ~mask) | (bit << pos));
}

void netModifier(int netOcts[], int position, int firstOct)
{
    //find what oct to modify
    int octSelector = 3;
    int octModifier = 0;
    if(position > 8){
        octSelector -= 1;
        octModifier = pow(2,position - 8);
    }else{
        if(position != 0 ){
            octModifier = pow(2,position);
        }
    }
    netOcts[octSelector] += octModifier;
    printf("Network address: ");
    printf("%d.%d.%d.%d\n", netOcts[0],netOcts[1],netOcts[2],netOcts[3]);
    //call bcModifier
    if(firstOct == 0){
        bcModifier(netOcts, position, 1);
    }

}

void bcModifier(int netOcts[], int position, int bit){
    //change all of the newly modified network bits to 1
    int tempOct[] = {netOcts[0], netOcts[1], netOcts[2], netOcts[3]};
    int posCounter = 0;
    int octSelector = 3;
    int tempPosition = 0;
    while(posCounter < position){
        if(tempPosition > 7){
            tempPosition -= 8;
            octSelector -= 1;
        }
        tempOct[octSelector] = modifyBit(tempOct[octSelector], tempPosition, bit);
        //printf("%d\n", tempPosition);
        tempPosition++;
        posCounter++;
    }
    printf("Broadcast address: ");
    printf("%d.%d.%d.%d\n", tempOct[0],tempOct[1],tempOct[2],tempOct[3]);
    
}



