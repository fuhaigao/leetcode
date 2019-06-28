class Solution {
    public List<String> restoreIpAddresses(String s) {
        List<String> res = new ArrayList();
        restoreIpAddressesHelper(res, "", s, 4);
        return res;
    }
    private void restoreIpAddressesHelper(List<String> res, String curr, String s, int target) {
        if (s.isEmpty() || target == 0) {
            if (s.isEmpty() && target==0)
                res.add(curr.substring(1));
            return;
        }
        else {
            int range = s.charAt(0)=='0' ? 1 : 3;
            for (int i=1; i<=s.length()&& i<=range; i++) {
                String tmp = s.substring(0,i);
                if (Integer.valueOf(tmp) <= 255)
                    restoreIpAddressesHelper(res, curr + "." + tmp, s.substring(i), target-1);
            }
        }
    }
}
