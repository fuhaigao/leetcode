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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(0);
        ListNode* curr = dummy;
        while (l1 != NULL && l2 != NULL){
            if (l1->val < l2->val){
                ListNode* tmp = new ListNode(l1->val);
                curr->next = tmp;
                l1 = l1->next;
            }
            else {
                ListNode* tmp = new ListNode(l2->val);
                curr->next = tmp;
                l2 = l2->next;
            }
            curr = curr->next;
        }
        if (l1 != NULL){
            curr->next = l1;
        }else {
            curr->next = l2;
        }
        return dummy->next;
    }
};
