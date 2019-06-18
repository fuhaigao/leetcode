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
    ListNode* swapPairs(ListNode* head) {
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* l1 = dummy;
        ListNode* l2 = head;
        while(l2!=NULL && l2->next != NULL){
            // Ex. 1, 2, 3, 4
            //l1 = pointer before 1. l2 = porinter at 1
            ListNode* nextStart = l2->next->next;
            l1->next = l2->next;
            l2->next->next = l2;
            l2->next = nextStart;
            l1 = l2;
            l2 = l2->next;
        }
        return dummy->next;
    }
};
