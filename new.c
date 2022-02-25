#include<stdio.h>
#include<math.h>
#include<string.h>
#define bit_size 8
char *decimal_to_bin(int decimal);
int bin_to_decimal(char binary[]);
int extract_num(char c);
void Embed(FILE* matrixFile,FILE* secretFile, FILE* newMatrixFile);
//void Extract(FILE* EmbeddedInfoFile,FILE* secretExtractedFile);
int last_bit(char* bin);
char* f_1LSB(char *binary, int secretInfo);
int main()
{
    FILE *secretFile,*matrixFile,*newMatrixFile;
    secretFile = fopen("Secret_info8.txt","rb");
    matrixFile = fopen("256x256_cover1.txt","rb");
    newMatrixFile = fopen("newMatrix.pgm","wb");

    Embed(matrixFile,secretFile,newMatrixFile);

    fclose(newMatrixFile);
    fclose(secretFile);
    fclose(matrixFile);
/*
    FILE* secretExtractedFile;
    secretExtractedFile = fopen("secretExtractedFile.txt","wb");
    newMatrixFile = fopen("newMatrix.pgm","r");
    if(newMatrixFile == NULL)
        printf("not opened...\n");
    Extract(newMatrixFile,secretExtractedFile);
*/
/*
    matrixFile = fopen("256x256_cover1.txt","rb");
    int matrixElement;
    for(int i=0; i<50; i++)
    {
        fscanf(newMatrixFile,"%d",&matrixElement);
        printf("%d ",matrixElement);
    }

    fclose(secretExtractedFile);
    fclose(newMatrixFile);
*/
    return 0;
}
void Embed(FILE* matrixFile,FILE* secretFile, FILE* newMatrixFile)
{
    fprintf(newMatrixFile,"P2\n");
    fprintf(newMatrixFile,"%d %d\n",256,256);
    fprintf(newMatrixFile,"255\n");
    for(int i=0; i<256; i++)
    {
        for(int j=0; j<256; j++)
        {
            int secretInfo, matrixElement, newElement ;

            fscanf(secretFile,"%d",&secretInfo);
            fscanf(matrixFile,"%d",&matrixElement);

            newElement = bin_to_decimal(f_1LSB(decimal_to_bin(matrixElement),secretInfo));

            fprintf(newMatrixFile,"%d ",newElement);
        }
    }
}
/*void Extract(FILE *newMatrixFile,FILE *secretExtractedFile)
{
    for(int i=0; i<256; i++)
    {
        for(int j=0; j<256; j++)
        {
            int secretInfo, matrixElement;

            fscanf(newMatrixFile,"%d",&matrixElement);

            secretInfo = last_bit(decimal_to_bin(matrixElement));
            fprintf(secretExtractedFile,"%d ",secretInfo);
        }
    }
}*/
char* f_1LSB(char *binary, int secretInfo)
{
    if(binary[bit_size-1] != (char)(secretInfo+48));
        binary[bit_size-1] = (char)(secretInfo+48);

    return binary;
}
int bin_to_decimal(char binary[])
{
    int decimal=0;

    for(int i=0;i<bit_size;i++)
        decimal += (extract_num(binary[i]) * pow(2,bit_size-i-1));
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
    strrev(result);
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
