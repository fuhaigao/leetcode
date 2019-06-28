// G[n] = F(1,n) + F(2,n) + ... + F(n,n)
// F(i,n) = G[i-1] * G[n-i]
// G(n) = G(0)*G(n-1) + G(1)*G(n-2) + ... + G(n-1)*G(0)
// G(2) = G(0)*G(1) + G(1)*G(0)
class Solution {
    public int numTrees(int n) {
        int[] nodes = new int [n+1];
        nodes[0] = nodes[1] = 1; //when n=0/1: only one unique way
        for (int i=2; i<=n; i++) {      //iteratively calculate the number of uniqe trees with i nodes
            for (int j=1; j<=i; j++) {      //j represents the jth node is the root
                nodes[i] += nodes[j-1] * nodes[i-j];
            }
        }
        return nodes[n];
    }
}
