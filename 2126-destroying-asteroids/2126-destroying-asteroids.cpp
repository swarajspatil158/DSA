class Solution {
public:
    bool asteroidsDestroyed(int mass, vector<int>& asteroids) {
        long long wt = mass;
        int len = asteroids.size();
        sort(asteroids.begin(),asteroids.end());
        
        for(int it:asteroids){
            if(it<=wt){
                wt+=it;
                
            }
            else{
                return 0;
            }
        }
        
            return 1;
        }
    
};