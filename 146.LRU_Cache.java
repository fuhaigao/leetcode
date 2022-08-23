class LRUCache {

    int capacity;
    Node head;
    Node tail;
    Map<Integer, Node> hm;
    
    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.hm = new HashMap<>();
        this.head = new Node(0, 0);
        this.tail = new Node(0, 0);
        this.head.next = this.tail;
        this.tail.prev = this.head;
    }
    
    public int get(int key) {
        if (hm.containsKey(key)) {
            Node curr = hm.get(key);
            remove(curr);
            insert(curr);
            return curr.value;
        }
        return -1;
    }
    
    public void put(int key, int value) {
        if (hm.containsKey(key)) {
            remove(hm.get(key));
        }
        Node newNode = new Node(key, value);
        hm.put(key, newNode);
        insert(newNode);
        if (hm.size() > this.capacity) {
            Node lastNode = this.head.next;
            remove(lastNode);
            hm.remove(lastNode.key);
        }
    }
    
    public void remove(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
    
    public void insert(Node node) {
        Node lastNode = this.tail.prev;
        lastNode.next = node;
        node.prev = lastNode;
        node.next = this.tail;
        this.tail.prev = node;
    }
    
}

class Node {
    int key;
    int value;
    Node prev;
    Node next;

    protected Node(int key, int value) {
        this.key = key;
        this.value = value;
    }
}



/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */