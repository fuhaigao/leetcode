/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
    public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(0);
        int sum = 0;
        ListNode* curr  = dummy;
        
        while (l1 != NULL || l2 != NULL){
            if (l1 != NULL){
                sum += l1->val;
                l1 = l1->next;
            }
            if (l2 != NULL){
                sum += l2->val;
                l2 = l2->next;
            }
            ListNode* tmp = new ListNode(sum%10);
            curr->next = tmp;
            curr = curr->next;
            sum /= 10;
        }
        if (sum == 1){
            curr->next = new ListNode(1);
        }
        return dummy->next;
    }
};
