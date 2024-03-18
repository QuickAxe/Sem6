#include <iostream>
using namespace std;

int xorr(uint8_t a, uint8_t b)
{
    return (a and !b) or (!a and b);
}

int main()
{
    uint8_t binaryString[100], remainder[100];
    uint8_t generator[50];

    int binaryStringLen, generatorLen;

    // inputs ================================================================================
    cout << "enter length of binary string and generator:";
    cin >> binaryStringLen >> generatorLen;

    cout << "\nEnter Binary String :";
    for (int i = 0; i < binaryStringLen; i++)
        cin >> binaryString[i];

    cout << "\nEnter generator String :";
    for (int i = 0; i < generatorLen; i++)
        cin >> generator[i];

    // intitialise remainder
    for (int i = 0; i < generatorLen; i++)
        remainder[i] = binaryString[i];

    // main crc division loop: ================================================================
    for (int i = 0; i < binaryStringLen - generatorLen + 1; i++)
    {

        bool flag = true;
        // check if window value is greater than generator, and actually divisible
        for (int j = 0; j < generatorLen; j++)
        {
            if (binaryString[i + j] == 0 and generator[j] == 0)
                continue;
            if (binaryString[i + j] == 1)
            {
                flag = false;
                break;
            }
            if (binaryString[i + j] == 0 and generator[j] == 1)
                break;
        }

        // perform modulo 2 division by using xor on each digit
        if (flag)
            for (int j = 0; j < generatorLen; j++)
                remainder[i + j] = binaryString[i + j] ^ 0;
        else
            for (int j = 0; j < generatorLen; j++)
                remainder[i + j] = binaryString[i + j] ^ generator[j];
    }

    // print remiander:
    for (auto i : remainder)
        cout << i;

    cout << "\n\n";
    for (int i = 0; i < binaryStringLen; i++)
        cout << remainder[i];
}

// gen = 1 0 0 1 1
// bitstring = 1 1 0 1 0 1 1 0 1 1 0 0 0 0
// remainder = 1 1 1 0