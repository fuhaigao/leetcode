// 1. if sum of gas is more than sum of cost, then there must be a solution. And the question guaranteed that the solution is unique(The first one I found is the right one).
// 2, The tank should never be negative, so restart whenever there is a negative number.
class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int sumGas=0, sumCost=0, currStart=0, tank=0;
        for (int i=0; i<gas.length; i++) {
            sumCost += cost[i];
            sumGas += gas[i];
            tank = tank + gas[i] - cost[i];
            if (tank < 0) {
                currStart = i+1;
                tank = 0;
            }
        }
        if (sumGas < sumCost) return -1;
        return currStart;
    }
}
