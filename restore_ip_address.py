class Solution:
    def restore_ip_addresses(self, s):
        res = []

        # IP address lenght cannot be more that 12 digits
        if len(s) > 12:
            return res
        
        # i for index
        # dots to track how many dots we have inserted (max 4)
        # curr_ip to store built IP ADDR
        def backtrack(i, dots, cur_ip):
            # if reached to the end then return
            if dots == 4 and i == len(s):
                res.append(cur_ip[:-1])  # remove last dot at the end
                return

            # if 4 dots and reached end then return
            if dots > 4:
                return
            
            # loop through the string until min (i+3, len(s))
            for j in range(i, min(i + 3, len(s))):
                if int(s[i:j+1]) < 256 and (i == j or s[i] != "0"):
                    # recursive call
                    backtrack(j + 1, dots + 1, cur_ip + s[i:j+1] + ".")
        
        backtrack(0, 0, "")
        return res

s = Solution()

print(s.restore_ip_addresses("25525511135"))