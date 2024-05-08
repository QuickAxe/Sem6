#include <iostream>
using namespace std;
string XOR(string a, string b)
{
    string result = "";
    int n = b.length();

    for (int i = 1; i < n; i++)
    {
        if (a[i] == b[i])
        {
            result += "0";
        }
        else
        {
            result += "1";
        }
    }
    return result;
}
void division(string data, string gen, int data_len, int gen_len)
{
    int len = gen_len;
    string temp = data.substr(0, len);
    int n = data_len;

    while (len < n)
    {
        if (temp[0] == '1')
        {
            temp = XOR(gen, temp) + data[len];
        }
        else
        {
            temp = XOR(string(len, '0'), temp) + data[len];
        }
        len += 1;
    }

    if (temp[0] == '1')
    {
        temp = XOR(gen, temp);
    }
    else
    {
        temp = XOR(string(len, '0'), temp);
    }
    cout << "\n\nRemainder is : " << temp;
    int new_len = data_len - gen_len + 1;
    string new_data = data;
    for (int i = new_len; i < data_len; i++)
    {
        new_data[i] = temp[i - new_len];
    }
    cout << "\n\nData to be sent is : " << new_data;
    cout << endl;
}

int main(void)
{
    string data, generator;
    cout << "Enter data to be sent : ";
    cin >> data;

    cout << "Enter Generator : ";
    cin >> generator;
    int gen_len = generator.length();
    for (int i = 0; i < gen_len - 1; i++)
    {
        data += '0';
    }
    int data_len = data.length();
    division(data, generator, data_len, gen_len);
}
