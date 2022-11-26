/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry=0;     
        
        ListNode l3= l1;       

        
        while (l1.next != null && l2.next !=null){
            int sum = l1.val + l2.val +carry;
            String s = Integer.toString(sum);            
            int leng = s.length();            
            char ch=s.charAt(leng-1);            
            l1.val = Character.getNumericValue(ch);
            if (leng>1)
                carry = Integer.parseInt(s.substring(0, leng-1));
            else
                carry=0;
            
            l1 = l1.next;
            l2 = l2.next;          
            
        }
        int sum = l1.val + l2.val +carry;
        String s = Integer.toString(sum);            
        int leng = s.length();            
        char ch=s.charAt(leng-1);            
        l1.val = Character.getNumericValue(ch);
        if (leng>1)
            carry = Integer.parseInt(s.substring(0, leng-1));
        else
            carry=0;
        
        
        if(l1.next ==null && l2.next == null){
             // System.out.println(l1.val);
            if (leng>1) 
                l1.next = new ListNode(carry);
           return l3;                      
        }else if(l1.next ==null && l2.next != null){        
           l1.next=l2.next;  
        }
        l1=l1.next;
        while (l1.next !=null ){
            sum = l1.val +carry;
             s = Integer.toString(sum);            
             leng = s.length();            
             ch=s.charAt(leng-1);            
            l1.val = Character.getNumericValue(ch);
            if (leng>1)
                carry = Integer.parseInt(s.substring(0, leng-1));
            else
                carry=0;
            // System.out.println(l1.val);
            l1 = l1.next;

        }
        sum = l1.val +carry;
         s = Integer.toString(sum); 
        // System.out.println(sum);
         leng = s.length();
        
         ch=s.charAt(leng-1);            
        l1.val = Character.getNumericValue(ch);
        if (leng>1){
            carry = Integer.parseInt(s.substring(0, leng-1));
            l1.next = new ListNode(carry);
        }
        return l3;
        
        
        
    }
}