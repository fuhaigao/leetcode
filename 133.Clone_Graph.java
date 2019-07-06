/*
 // Definition for a Node.
 class Node {
 public int val;
 public List<Node> neighbors;
 
 public Node() {}
 
 public Node(int _val,List<Node> _neighbors) {
 val = _val;
 neighbors = _neighbors;
 }
 };
 */

//avoid copying the same node for multiple times
//dfs clone all nodes
class Solution {
    public Node cloneGraph(Node node) {
        HashMap<Integer, Node> visited = new HashMap<Integer,Node>();
        return cloneGraphHelper(node, visited);
    }
    private Node cloneGraphHelper(Node node, HashMap<Integer, Node> visited) {
        if (node == null) return null;
        if (visited.containsKey(node.val)){
            return visited.get(node.val);
        }
        else {
            Node tmp = new Node(node.val, new ArrayList());
            visited.put(node.val, tmp);
            for (int i=0; i<node.neighbors.size(); i++) {
                tmp.neighbors.add(cloneGraphHelper(node.neighbors.get(i),visited));
            }
            return tmp;
        }
    }
}
