// bidirectional BFS
// 用2个hashSet分别存begin 和 end
// 注意每次swap下  把少的hashset作为beginSet
public class Solution {
    
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        if (!wordList.contains(endWord)) return 0;
        Set<String> beginSet = new HashSet<String>(), endSet = new HashSet<String>();
        
        int len = 1;
        int strLen = beginWord.length();
        HashSet<String> visited = new HashSet<String>();
        
        beginSet.add(beginWord);
        endSet.add(endWord);
        while (!beginSet.isEmpty() && !endSet.isEmpty()) {
            if (beginSet.size() > endSet.size()) {
                Set<String> set = beginSet;
                beginSet = endSet;
                endSet = set;
            }
            
            Set<String> temp = new HashSet<String>();
            // loop beginSet 里每一个word
            for (String word : beginSet) {
                char[] chs = word.toCharArray();
                
                // 遍历改变当前word的 ith letter
                for (int i = 0; i < chs.length; i++) {
                    char old = chs[i];
                    // letter 可改为 a~z
                    for (char c = 'a'; c <= 'z'; c++) {
                        chs[i] = c;
                        String target = String.valueOf(chs);
                        // 如果endSet存在改变后的单词，意味着找到了 return len+!
                        if (endSet.contains(target)) {
                            return len + 1;
                        }
                        // 如果没有变成过这个word, 且这个word 在wordList里:
                        if (!visited.contains(target) && wordList.contains(target)) {
                            temp.add(target);
                            visited.add(target);
                        }
                        // 记得revert changed letter back
                        chs[i] = old;
                    }
                }
            }
            
            beginSet = temp;
            len++;
        }
        
        return 0;
    }
}
