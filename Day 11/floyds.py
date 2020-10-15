#FLOYDS PRINCIPLE OF LOOP DETECTION

def detectLoop(head):
    
    p1 = head
    p2 = head
    
    while p1 and p2 and p2.next :
        
        p1 = p1.next
        p2 = p2.next.next
        
        if p1 == p2:
            return True
    return False


