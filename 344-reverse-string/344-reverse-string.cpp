class Solution {
public:
    
    void reverseString(vector<char>& name) {
        int len = name.size();
        int e = len-1;
        int i =0;
        while(i<e){
        swap(name[i++],name[e--]);

 }
        
    }
};