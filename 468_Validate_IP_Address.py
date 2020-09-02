""" https://leetcode.com/problems/validate-ip-address/
Given a string IP. We need to check If IP is a valid IPv4 address, valid IPv6 address or not a valid IP address.
Return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a valid IP of any type.
A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses but "192.168.01.1", "192.168.1.00" and "192.168@1.1" are invalid IPv4 adresses.
A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:
1 <= xi.length <= 4 / Leading zeros are allowed in xi.
xi is hexadecimal string whcih may contain digits, lower-case English letter ('a' to 'f') and/or upper-case English letters ('A' to 'F').
For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses but "2001:0db8:85a3::8A2E:037j:7334" and "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.

class Solution(object):
    def validIPAddress(self, IP):
        :type IP: str
        :rtype: str


# For Real Life Validation of IP Address (ipaddress lib in Python, InetAddress class in Java)

from ipaddress import ip_address, IPV6Address
class Solution:
    def validIPAddress(self, IP: str) -> str
        try:
            return "IPv6" if type(ip_address(IP)) is IPv6Address else "IPv4"
        except:
            return "Neither"

Python - Regular Expressions : special sequence of characterss that helps you match or find  other strings or set of strings, using a specialized syntax  held in a  pattern.
Regular expression to match the pattern of IPv4 or IPv6 with given address and as matching patterns have constant length, it would take constant time complexity
import re
class Solution:
    chunk_IPv4 = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])' == 0 to 255
    patten_IPv4 = re.compile(r'^(' + chunk_IPv4 + r'\.){3}' + chunk_IPv4 + r'$')
    
    chunk_IPv6 = r'([0-9a-fA-F]{1,4})'
    patten_IPv6 = re.compile(r'^(' + chunk_IPv6 + r'\:){7}' + chunk_IPv6 + r'$')

    def validIPAddress(self, IP: str) -> str:        
        if self.patten_IPv4.match(IP):
            return "IPv4"
        return "IPv6" if self.patten_IPv6.match(IP) else "Neither"

But I am going to use Divide & Conquer. O(n)
"""
class Solution(object):
    # .count() returns the number of elements with the specified value
    def validIPAddress(self, IP):
        # counting dot and colon takes O(n) to parse the entire input string
        if(IP.count('.')==3):
            return self.validIPv4(IP)
        elif(IP.count(':')==7):
            return self.validIPv6(IP)
        else:
            return "Neither"

    # .split() splits a string in to a list with delimter
    def validIPv4(self, IP):
        dot = IP.split('.')
        for x in dot:
            if len(x) > 3 or len(x) == 0: 
                return "Neither"
            if len(x) == 1 and x[0] == '0' or not x.isdigit():
                return "Neither"
            if int(x) > 255 or int(x) < 0: # .isdigit() check should come ahead of this cause of last input
                return "Neither"
        return "IPv4"
    
    def validIPv6(self, IP):
        colon = IP.split(':')
        hexa = '0123456789abcdefABCDEF'
        for x in colon:
            if len(x) > 4 or len(x) == 0:
                return "Neither"
            # all = when all elements in iterable is true
            # if not all y in hexa are in x
            if not all(y in hexa for y in x):
                return "Neither"
        return "IPv6"
        
if __name__ == '__main__':
    print(Solution().validIPAddress("172.16.254.1"))
    print(Solution().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
    print(Solution().validIPAddress("256.256.256.256"))
    print(Solution().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334:"))
    print(Solution().validIPAddress("1e1.4.5.6"))
    

