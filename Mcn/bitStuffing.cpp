#include <iostream>
using namespace std;

void bitStuff(string data)
{
    int i = 0, j = 0, count = 0;
    string stuffed_data;

    while (i < data.length())
    {
        if (data[i] == '1')
        {
            count++;
        }
        else
        {
            count = 0;
        }
        stuffed_data += data[i];
        if (count == 5 && data[i + 1] == '1')
        {
            stuffed_data += '0';
            count = 0;
        }
        i++;
    }
    cout << "Stuffed data:	" << stuffed_data << endl;
}

int main()
{
    string data;
    cout << "Enter the data: ";
    cin >> data;
    bitStuff(data);
}
