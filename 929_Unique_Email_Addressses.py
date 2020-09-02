""" https://leetcode.com/problems/unique-email-addresses/
Every email consists of a local name and a domain name, separated by the @ sign.
For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.
Besides lowercase letters, these emails may contain '.'s or '+'s.
If you add periods ('.') between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name.  For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.  (Note that this rule does not apply for domain names.)
If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.  (Again, this rule does not apply for domain names.)
It is possible to use both of these rules at the same time.
Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails? 
"""

"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
"""
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        # set - unindexed unordered iterable, .add .remove .update
        checked = set()
        for x in emails:
            local, domain = x.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            # if (local + domain) not in checked: Set does not allow duplicate numbers anyways
            # just add with updated one, '.'
                checked.add(local.replace('.','') + '@'+ domain) # don't necessarily need replaceAll // replace(old, new, count)
        return len(checked) # set() match automatically  = O(n) -> USE FUCKUING DAVID DICTIONARY  O(1) = adjacent matrix 

if __name__ == '__main__':
    print(Solution().numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
