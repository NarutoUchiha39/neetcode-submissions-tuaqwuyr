class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        head = dummy
        dummy1 = list1
        dummy2 = list2
        
        while(dummy1 and dummy2):
            if(dummy1.val > dummy2.val):
                new_node = ListNode(dummy2.val)
                dummy2 = dummy2.next
                dummy.next = new_node
                dummy = new_node
                
            else:
                new_node = ListNode(dummy1.val)
                dummy1 = dummy1.next
                dummy.next = new_node
                dummy = new_node
        
        while(dummy1):
            new_node = ListNode(dummy1.val)
            dummy.next = new_node
            dummy = new_node
            dummy1 = dummy1.next
            
        while(dummy2):
            new_node = ListNode(dummy2.val)
            dummy.next = new_node
            dummy = new_node
            dummy2 = dummy2.next
        
        return head.next
            
            
            
            
            
        
        