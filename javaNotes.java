Math.max();

int[] array = new int[size];

HashSet<Character> hs = new HashSet();
!hs.add();

List<Integer> arr = new ArrayList<int>();
ArrayList<ArrayList<Integer>> arr = new ArrayList<>() / ArrayList();
Arrays.sort(arr, (a,b) -> a[0]-b[0])
Collections.reverse(arr);

arr.add()
arr.remove(index);  //arr.remove(arr.size()-1) == pop_back
arr.get(index)

List<> vs. ArrayList<>
Almost always the first one is preferred over the second one. The first has the advantage that the implementation of the List can change (to a LinkedList for example), without affecting the rest of the code. This will be a difficult task to do with an ArrayList, not only because you will need to change ArrayList to LinkedList everywhere, but also because you may have used ArrayList specific methods.

56. Merge Intervals

string:
charAt(index)
str.length()
str.isEmpty()

StringBuilder sb = new StringBuilder();
sb.append(val)  //val 可以是任何type

obj.toString() / String.valueOf(obj) //唯一区别在：when obj == null, String.valueOf return "null"

char to int: 'a' - '0' / Character.getNumericValue(c)

Stack<TreeNode> stack = new Stack();
stack.add();
stack.pop();
stack.peek();
stack.empty();


char[] c = s.toCharArray();
Character.isLetterOrDigit(c);
Character.toLowerCase(c);

Integer.MAX_VALUE / Integer.MIN_VALUE
