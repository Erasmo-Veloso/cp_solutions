
class Solution {
public:
    #include<vector>;
    int maxProfit(vector<int>& prices) {
        int l = 0; /* Left representing buys */
        int r = 1; /* Rigth representing sells */
        int maxP = 0; 
        while (r < prices.size()){
            if(prices[l] < prices[r]){
                int sub = prices[r] - prices[l];
                maxP = max(sub, maxP);
            }else{
                l = r;
            }
            r+=1;
        }
        return maxP;
    }
};