#include <iostream>
using namespace std;
int main()
{
    string data;
    string d;
    int n;
    cout << "Enter the number of bytes: ";
    cin >> n;
    data += "FLAG ";
    for (int i = 0; i < n; i++)
    {
        cout << "Enter the data: ";
        cin >> d;

        if (d == "ESC" || d == "FLAG")
        {
            data += "ESC ";
        }
        data += d;
        data += " ";
    }
    data += "FLAG ";

    cout << "Stuffed data:	" << data << endl;
    return 0;
}
