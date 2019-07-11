// Can be done use one stack:
// When pop: if (min == stack.pop()) min = stack.peek() (Updating min)
class MinStack {
    Stack<Integer> stack = new Stack();
    Stack<Integer> minStack = new Stack();
    
    /** initialize your data structure here. */
    public MinStack() {
        stack = new Stack<Integer>();
        minStack = new Stack<Integer>();
    }
    
    public void push(int x) {
        stack.push(x);
        if (minStack.isEmpty()) minStack.push(x);
        else {
            if (x < minStack.peek()) minStack.push(x);
            else minStack.push(minStack.peek());
        }
        
    }
    
    public void pop() {
        stack.pop();
        minStack.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
