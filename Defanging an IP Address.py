#Given a valid (IPv4) IP address, return a defanged version of that IP address.
#A defanged IP address replaces every period "." with "[.]".

'''
Solution 1:
---> runs in 32ms*
'''

class Solution:
    def defangIPaddr(self, address: str) -> str:  
        return "[.]".join(address.split("."))
'''
Solution 2:
---> runs in 38ms*
'''

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".","[.]")
