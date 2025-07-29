#include <iostream>
#include <utility>
#include <iomanip>

using namespace std;


int T;

struct Line
{
    int x1, y1, x2, y2;
    Line(int x1, int y1, int x2, int y2) : x1(x1), y1(y1), x2(x2), y2(y2) {}
    Line() : x1(0), y1(0), x2(0), y2(0) {}
    friend istream& operator>>(istream& is, Line& l) {
        return is >> l.x1 >> l.y1 >> l.x2 >> l.y2;
    }
};


int intersect(const Line& a, const Line& b, double& x, double& y) {
    
    // 평행여부 확인
    if((a.x1 - a.x2) * (b.y1 - b.y2) == (a.y1 - a.y2) * (b.x1 - b.x2)) {
        // 평행한 경우
        if ((a.x1 - a.x2) * (b.y1 - a.y1) == (a.y1 - a.y2) * (b.x1 - a.x1)) {
            x = y = 0; 
            return 2;
        }
        return 0; 
    }

    int down = (a.x1 - a.x2) * (b.y1 - b.y2) - (a.y1 - a.y2) * (b.x1 - b.x2);
    x = ((a.x1 * a.y2 - a.y1 * a.x2) * (b.x1 - b.x2) - (a.x1 - a.x2) * (b.x1 * b.y2 - b.y1 * b.x2)) / (double)(down);
    y = ((a.x1 * a.y2 - a.y1 * a.x2) * (b.y1 - b.y2) - (a.y1 - a.y2) * (b.x1 * b.y2 - b.y1 * b.x2)) / (double)(down);

    return 1;
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    Line a,b;
    cin >> T;
    while(T--){
        
        cin >> a >> b;
        double x, y;
        int result = intersect(a, b, x, y);
        if(result == 0){
            cout << "NONE" << endl;
        } else if(result == 1){
            cout << fixed << setprecision(2);
            cout << "POINT " << x << " " << y << endl;
        } else if(result == 2){
            cout << "LINE" << endl;
        }
    }
}