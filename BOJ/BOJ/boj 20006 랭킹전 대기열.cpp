#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cstdlib>

using namespace std;

int P, M;


struct Player{
    int lv;
    string name;

    bool operator<(const Player& other) const {
        return name < other.name;
    }

    friend ostream& operator<<(ostream& os, const Player& player) {
        os << player.lv << " " << player.name;
        return os;
    }
};

struct Room{
    int lv;
    vector<Player> players;
};

vector<Room> rooms;

Room& getRoom(int lv) {
    for(int i = 0; i < rooms.size(); i++) {
        if(abs(rooms[i].lv - lv) <= 10) {
            if(rooms[i].players.size() < M) {
                return rooms[i];
            }
        }   
    }
    rooms.push_back({lv, {}});
    return rooms.back();
}

int main(){
    cin >> P >> M;

    for(int i = 0; i < P; i++) {
        Player player;
        cin >> player.lv >> player.name;
        Room& room = getRoom(player.lv);
        if(room.players.size() < M) {
            room.players.push_back(player);
        }
    }

    for(Room& room : rooms) {
        sort(room.players.begin(), room.players.end());
        if(room.players.size() == M){
            cout << "Started!" << endl;
            for(const Player& player : room.players) {
                cout << player << endl;
            }
        } else {
            cout << "Waiting!" << endl;
            for(const Player& player : room.players) {
                cout << player << endl;
            }
        }
    }


    return 0;
}