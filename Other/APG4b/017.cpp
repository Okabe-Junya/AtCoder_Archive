#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, S;
    int cnt = 0;
    cin >> N >> S;
    vector<int> A(N), P(N);
    for (int i = 0; i < N; i++) {
        cin >> A.at(i);
    }
    for (int i = 0; i < N; i++) {
        cin >> P.at(i);
    }
    for (int i : A) {
        for (int j : P) {
            if (i + j == S) {
                cnt++;
            }
        }
    }
    cout << cnt << endl;

    // リンゴ・パイナップルをそれぞれ1つずつ購入するとき合計S円になるような買い方が何通りあるか
    // ここにプログラムを追記
}
