// Practical 1 :
// Write C++ Programs to demonstrate single and multilevel inheritance

// Program
#include<iostream>
#include<conio.h>

class circle {
private:
    float r, a;

public:
    void read() {
        std::cout << "Enter radius: ";
        std::cin >> r;
    }

    void compute() {
        a = 3.14 * r * r;
    }

    void display() {
        std::cout << "Area=" << a;
    }
};

int main() {
    clrscr(); // Note: clrscr() is non-standard and may not work in all compilers

    circle c;
    c.read();
    c.compute();
    c.display();

    getch(); // Note: getch() is non-standard and may not work in all compilers
    return 0;
}
