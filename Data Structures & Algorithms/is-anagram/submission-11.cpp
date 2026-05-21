class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int>v(26);
        for(char &i:s){
            v[i-'a']++;
        }
        for(char&i: t){
            v[i-'a']--;
        }
        for(int&i:v)if(i!=0)return false;
        return true;
    }
};
