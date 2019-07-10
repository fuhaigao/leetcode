class LRUCache {
    Map<Integer, DListNode> cache;
    int capacity;
    DListNode head = null;
    DListNode tail = null;
    public LRUCache(int capacity) {
        cache = new HashMap<Integer, DListNode>();
        this.capacity = capacity;
    }
    
    public int get(int key) {
        if (this.cache.containsKey(key)){
            DListNode target = cache.get(key);
            int value = target.val;
            target.update();
            return value;
        }
        return -1;
    }
    
    public void put(int key, int value) {
        if (cache.containsKey(key)) {
            DListNode target = cache.get(key);
            target.val = value;
            target.update();
        }
        else {
            if (cache.size() == capacity){
                cache.remove(head.key);
                head.pop();
            }
            DListNode newNode = new DListNode(key, value);
            newNode.append();
            cache.put(key, newNode);
        }
    }
    class DListNode {
        int val;
        int key;
        DListNode next = null;
        DListNode prev = null;
        
        public DListNode(int key, int val){
            this.key = key;
            this.val = val;
        }
        
        private void append(){
            // inseting the first node
            if (tail == null){
                tail = this;
                head = this;
            }
            // appned as tail and update tail reference.
            else {
                this.next = null;
                tail.next = this;
                this.prev = tail;
                tail = tail.next;
            }
        }
        private void update() {
            // no need to update if accessing the most revently used value.
            if (this == tail) return;
            else {
                if (this == head)
                    head = head.next;
                else
                    this.prev.next = this.next;
                this.next.prev = this.prev;
                this.append();
            }
        }
        private void pop() {
            // if 'this' is the only node, set both head and tail to null.
            if (tail == this) {
                head = null;
                tail = null;
            }
            else {
                head = this.next;
                this.next.prev = null;
            }
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
