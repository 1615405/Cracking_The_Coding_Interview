class Solution {
public:
    string replaceSpaces(string S, int length) {
        int cnt = 0;
        for (int i = 0; i < length; i++) {
            if (S[i] == ' ') {
                cnt += 1;
            }
        }
        S.resize(length + cnt * 2);
        int i = length - 1, j = S.length() - 1;
        while (i >= 0 && i != j) {
            if (S[i] == ' ') {
                S[j--] = '0';
                S[j--] = '2';
                S[j--] = '%';
            } else {
                S[j--] = S[i];
            }
            i -= 1;
        }
        return S;
    }
};
