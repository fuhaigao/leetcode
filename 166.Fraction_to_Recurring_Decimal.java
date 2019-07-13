class Solution {
    public String fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0) return "0";
        StringBuilder sb = new StringBuilder();
        // sign: + / -
        if ((numerator<0 && denominator>0) || (numerator>0 && denominator<0)) sb.append("-");
        
        // change to abs long value
        // 要先变成long 再转换abs
        long num = Math.abs((long)numerator);
        long den = Math.abs((long)denominator);
        
        // 整数 integral part
        sb.append(num/den);
        num = num % den;
        if (num == 0) return sb.toString();
        
        // 分数 factorial part
        sb.append(".");
        Map<Long, Integer> map = new HashMap();     // Map use to check repeating digits, and store index
        map.put(num, sb.length());
        // 每次得到新的num 先判断是否repeat，再存进map 然后进入下一个循环
        while (num != 0){
            // 循环开始先append，因为上一个循环已经判断过这个digit是否repeat了
            num *= 10;
            sb.append(num/den);
            num %= den;
            if (map.containsKey(num)) {
                int index = map.get(num);
                sb.insert(index, "(");
                sb.append(")");
                return sb.toString();
            }
            // 另一种判断是否 existed 的方法， 不用containsKey， 如果get() return 的是null，代表还没有repeat
            // 注意： 要用Integer， int 不可以判断是否等于 null
            
            // Integer reminderIndex = map.get(num);
            // if (reminderIndex != null){
            //     sb.insert(reminderIndex, "(");
            //     sb.append(")");
            //     return sb.toString();
            // }
            map.put(num, sb.length());
        }
        return sb.toString();
    }
}
