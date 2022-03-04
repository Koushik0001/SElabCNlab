#include<stdio.h>
#define bit_size 8
float MSE = 0 , PSNR; 
char *decimal_to_bin(int decimal);
int bin_to_decimal(char binary[]);
int extract_num(char c);
void Embed(FILE* matrixFile,FILE* secretFile, FILE* newMatrixFile);
int last_bit(char* bin);
char* f_1LSB(char *binary, int secretInfo);

float logf(float x);
float power(float base, int expo);
void strrevf(char *string);
int main()
{
    FILE *secretFile,*matrixFile,*newMatrixFile;
    secretFile = fopen("Secret_info1.txt","rb");
    matrixFile = fopen("256x256_cover1.txt","rb");
    newMatrixFile = fopen("newMatrix.pgm","wb");

    Embed(matrixFile,secretFile,newMatrixFile);

    fclose(newMatrixFile);
    fclose(secretFile);
    fclose(matrixFile);

    printf("MSE = %f\n",MSE);
    printf("PSNR = %f\n",PSNR);

    return 0;
}
void Embed(FILE* matrixFile,FILE* secretFile, FILE* newMatrixFile)
{
    fprintf(newMatrixFile,"P2\n");
    fprintf(newMatrixFile,"%d %d\n",256,256);
    fprintf(newMatrixFile,"%d\n",255);
    for(int i=0; i<256; i++)
    {
        for(int j=0; j<256; j++)
        {
            int secretInfo, matrixElement, newElement ;

            fscanf(secretFile,"%d",&secretInfo);
            fscanf(matrixFile,"%d",&matrixElement);

            newElement = bin_to_decimal(f_1LSB(decimal_to_bin(matrixElement),secretInfo));
            MSE += power((matrixElement-newElement),2);
            fprintf(newMatrixFile,"%d ",newElement);
        }
    }
    MSE  = MSE/(256*256);
    PSNR = 10 * logf(256*256/MSE)/2.303;
}

char* f_1LSB(char *binary, int secretInfo)
{
    if(binary[bit_size-1] != (char)(secretInfo+48))
        binary[bit_size-1] = (char)(secretInfo+48);

    return binary;
}
int bin_to_decimal(char binary[])
{
    int decimal=0;

    for(int i=0;i<bit_size;i++)
        decimal += (extract_num(binary[i]) * power(2,bit_size-i-1));
    return(decimal);
}
char *decimal_to_bin(int decimal)
{
    int  i=0;
    float temp;
    static char result[bit_size+1];

    while(decimal != 0 )
    {
        result[i] = (char)((decimal % 2)+48);
        decimal /= 2;
        i++;
    }

    result[bit_size] ='\0';
    if(i<bit_size)
    {
        for(int k=i; k<bit_size;k++)
            result[k] = '0';
    }
    strrevf(result);
    return result;
}
int last_bit(char *bin)
{
    int lbit = bin[bit_size-1] - '0';
    return lbit;
}
int extract_num(char c)
{
    int num;
    if(c < 58 && c > 47)
        num = c - '0';
    else
        num = c - 'A' + 10;
    return(num);
}
float logf(float x)
{
    float result = 0;
    float previous, current;
    float count = 5;
    previous = (x-1)/(x+1);
    current = previous + (1/3)*power((x-1)/(x+1),3);
    for(int i=0; i<50000;i++)
    {
        previous = current;
        current += (1/count)*power((x-1)/(x+1),count);
        count += 2;
    }
    current *= 2;
    return current;
}
void strrevf(char *string)
{
    int i;
    for(i=0; i<bit_size/2; i++)
    {
        char c = string[i];
        string[i] = string[bit_size-i-1];
        string[bit_size-i-1] = c;
    }
}
float power(float base, int expo)
{
    float result = 1;
    int i;
    for(i=0; i<expo; i++)
        result *= base;
    
    return result;
}