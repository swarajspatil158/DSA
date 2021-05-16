    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        merge_list = []
        
        for ele in intervals:
            
            if not merge_list or merge_list[-1][1] < ele[0]:
                merge_list.append(ele)
            
            else:
                merge_list[-1][1] = max(merge_list[-1][1], ele[1])
        
        return merge_list
