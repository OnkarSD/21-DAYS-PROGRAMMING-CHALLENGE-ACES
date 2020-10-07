#274. H-Index   

     citations.sort(reverse=True)
        
        for i,v in enumerate(citations):
            
            if i >= v:
                return i
        return len(citations)

	
#406. Queue reconstruction by height	

        r = []
        people = sorted(people, key = lambda x: (-x[0],x[1]))
        
            
        for i in people:
            r.insert(i[1], i)
        return r
        
