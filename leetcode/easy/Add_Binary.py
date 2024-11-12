class Solution:
    def addBinary(self, a: str, b: str) -> str:
        print(a, b)
        a = list(a)
        b = list(b)
        
        list_rev_a = list(reversed(a))
        list_rev_b = list(reversed(b))
        print(list_rev_a)
        print(list_rev_b)
        
        if len(list_rev_a) < len(list_rev_b):
            row = len(list_rev_b) - len(list_rev_a)
            #print(row)
            #z = input('sdfsdfsf')
            for i in range(row):
                list_rev_a.append('0')
        elif len(list_rev_a) > len(list_rev_b):
            row = len(list_rev_a) - len(list_rev_b)
            for i in range(row):
                list_rev_b.append('0')
        
        print()
        print(list_rev_a)
        print(list_rev_b)

        k = 0
        result = []
        print()
        print('x', ' - ', 'a', 'b', 's', 'k')
        print('x', ' - ', '0', '0', '0', '0')
        for x, rev_a in enumerate(list_rev_a):
            sum_num = int(rev_a) + int(list_rev_b[x]) + k
            if sum_num == 2:                
                sum_num = 0 #+ k
                k = 1
            elif sum_num > 2:
                sum_num = 0 + k
                k = 1
            else:
                #sum_num += k
                k = 0
            result.append(sum_num)
            print(x, ' - ', rev_a, list_rev_b[x], sum_num, k)
        if k !=0:
            result.append(k)
        print(result)
        result = "".join(str(element) for element in reversed(result))
        return result
        
    

sol = Solution()
a = "11"
b = "1"
#11110
print(sol.addBinary(a=a, b=b))