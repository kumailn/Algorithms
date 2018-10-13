function addTwoNumbers(l1, l2) {
    if (!l1 || !l2) return l1 ? l1 : l2
    let origin = new ListNode(null), num = origin, carry = 0, n1 = 0, n2 = 0;
    while(l1 || l2 || carry){
        n1 = l1 ? l1.val : 0;
        n2 = l2 ? l2.val : 0;
        num.next = new ListNode((n1 + n2 + carry) % 10);
        carry = Math.floor((n1 + n2 + carry)/10);
        if(l1) l1 = l1.next;
        if(l2) l2 = l2.next
        num = num.next
    };
    return origin.next;
};