// UVA 10855 - Rotated square
// 2019.09.17
// Prog by AdcKi
// AC

#include<bits/stdc++.h>

using namespace std;

const int MAX_SIZE = 1000 + 5;

char BS[MAX_SIZE][MAX_SIZE], SS[MAX_SIZE][MAX_SIZE];

bool isSS(int y, int x, int m) {
	for (int i = 0; i < m ; i++) {
		for (int j = 0; j < m; j++) {
			if (BS[y + i][x + j] != SS[i][j]) {
				return false;
			}
		}
	}
	return true;
}

int main() {
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
	while (true) {
		int n, m;
		cin >> n >> m;
		if (n == 0 && m == 0) return 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				cin >> BS[i][j];
			}
		}
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < m; j++) {
				cin >> SS[i][j];
			}
		}
		for (int l = 0; l < 4; l++) {
			int cnt = 0;
			for (int i = 0; i < n - m + 1; i++) {
				for (int j = 0; j < n - m + 1; j++) {
					if (isSS(i, j, m)) cnt++;
				}
			}
			cout << cnt;
			if (l == 3) break;
			cout << " ";
			for (int i = 0; i < ceil(m / 2.0); i++) {
				for (int j = 0; j < floor(m / 2.0); j++) {
					char swap = SS[i][j];
					SS[i][j] = SS[m - 1 - j][i];
					SS[m - 1 - j][i] = SS[m - 1 - i][m - 1 - j];
					SS[m - 1 - i][m - 1 - j] = SS[j][m - 1 - i];
					SS[j][m - 1 - i] = swap;
				}
			}
		}
		cout << "\n";
	}
	return 0;
}
