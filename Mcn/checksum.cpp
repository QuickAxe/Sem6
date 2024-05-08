#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int To_Decimal(string data)
{
    int n = data.length();
    int num = 0;
    for (int i = 0; i < n; i++)
    {
        num = num * 2 + (data[i] - '0');
    }
    return num;
}

string To_Binary(int num, int data_len)
{
    string data = "";
    while (num > 0)
    {
        data = to_string(num % 2) + data;
        num = num / 2;
    }
    int n = data.length();
    if (n < data_len)
    {
        data = string(data_len - n, '0') + data;
    }
    return data;
}

string complement(string data)
{
    int n = data.length();
    for (int i = 0; i < n; i++)
    {
        if (data[i] == '0')
        {
            data[i] = '1';
        }
        else
        {
            data[i] = '0';
        }
    }
    return data;
}
void errorcheck(string data1, string data2, string checksum)
{
    int Final = To_Decimal(data1) + To_Decimal(data2) + To_Decimal(checksum);
    if (Final > pow(2, data1.length()) - 1)
    {
        Final = Final - (pow(2, data1.length()) - 1);
    }
    string To_Send = To_Binary(Final, data1.length());
    To_Send = complement(To_Send);

    for (int i = 0; i < To_Send.length(); i++)
    {
        if (To_Send[i] != '0')
        {
            cout << "\nError in data\n";
            return;
        }
    }
    cout << "\nNo error in data\n";
}

int main(void)
{
    string data1, data2;
    int data_len = data1.length();

    cout << "Enter data 1 : ";
    cin >> data1;
    cout << "Enter data 2 : ";
    cin >> data2;

    int num1 = To_Decimal(data1);
    int num2 = To_Decimal(data2);
    int sum = num1 + num2;
    if (sum > pow(2, data_len) - 1)
    {
        sum = sum - (pow(2, data_len) - 1);
    }
    string data = To_Binary(sum, data_len);
    string checksum = complement(data);

    cout << "\nChecksum : " << checksum << endl;

    errorcheck(data1, data2, checksum);
    return 0;
}
