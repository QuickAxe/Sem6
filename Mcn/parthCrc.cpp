// #include <bits/stdc++.h>

#include <iostream>
#include <vector>
using namespace std;

void print(vector<unsigned int> a)
{
    for (auto i : a)
        cout << i << " ";
    cout << endl;
}

int main()
{

    vector<unsigned int> binaryString;
    vector<unsigned int> generator;

    int binaryStringLen, generatorLen, temp;

    cout << "Generator String Length = ";
    cin >> generatorLen;
    cout << "Generator String input : (0/1)";
    for (int i = 0; i < generatorLen; i++)
    {
        cin >> temp;
        generator.push_back(temp);
    }

    cout << "Binary String Length = ";
    cin >> binaryStringLen;
    cout << "Binary String input : (0/1)";
    for (int i = 0; i < binaryStringLen; i++)
    {
        cin >> temp;
        binaryString.push_back(temp);
    }

    for (int i = 0; i < binaryStringLen - generatorLen + 1; i++)
    {

        bool flag = true;

        for (int k = 0; k < generatorLen; k++)
        {
            if (binaryString[i + k] == 0 and generator[k] == 0)
                continue;
            if (binaryString[i + k] == 1)
            {
                flag = false;
                break;
            }
            if (binaryString[i + k] == 0 and generator[k] == 1)
                break;
        }

        if (flag)
            for (int j = 0; j < generatorLen; j++)
                binaryString[i + j] = binaryString[i + j] ^ 0;
        else
            for (int j = 0; j < generatorLen; j++)
                binaryString[i + j] = binaryString[i + j] ^ generator[j];
    }

    print(binaryString);

    // gen = 1 0 0 1 1
    // bitstring = 1 1 0 1 0 1 1 0 1 1 0 0 0 0
}