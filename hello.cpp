// #include <iostream>
// using namespace std;

// int main() {
//     int age=18;
//     float gpa=3.5;
//     string name="Abhinav";
//     char grade='A';
//     bool isMale=true;

//     cout << "Name: " << name << "Age; " << age << "GPA :" << gpa << endl;

//     int a=10 , b=5;
//     cout << a+b << endl;
//     cout << a-b << endl;

//     int r;
//     cout << "Enter radius: ";
//     cin >> r ;
//     cout << "Area of circle; " << 3.14*r*r << endl;
    


//     if (age == 18) {
//         cout << "nice";

//     }
//     else if (age <= 18){
//         cout << "minorrrrrr";
//     }
//     else {
    
//     cout << "budeeeee";
//     }
//     return 0;
// }

#include <iostream>
using namespace std;

int main(){
    int a;
    cout << "Enter a number;"; 
    cin >> a; 
    cout << endl;
    string c="YES";
    for (int i=2; i<=a-1; i++){
        if (a%i==0){
            cout << "Not prime" << endl;
            c="NO";
            break;
        }
    }
    if (c!="NO"){
        cout << "Prime" << endl;
    }
    

    return 0;
}
