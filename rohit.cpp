class Solution {
public:
    bool isPalindrome(int x) {
     string str = to_string(x);
     int i = 0;
     int j = str.size()-1;
     while(i<j){
         if(str[i]!=str[j]){
             return false;
         }
         else{

         }
     }
     return true;
    }
};
