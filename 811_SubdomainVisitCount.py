class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """

        # Hashmap O(N) / O(N)
        # Quetion specified that maximum of two periods per string, thus, inner for loop only three times
        # => O(n * d) = O(3n) 
        """ 
        1) Will need to split given inputs by first " ": then counter + domains
        2) domains split('.') and divide into subdomains with counter - store into hashmap
        3) return the value:key in hashmap in format using string.formatter
        """

        domain_dict = {}
        for subdomain in cpdomains:
            counter, domain = subdomain.split(' ')
            counter = int(counter)

            sub = domain.split('.') # google, mail, com
            for i in range(len(sub)):
                # google.mail.com - mail.com  - com
                domain_dict['.'.join(sub[i:])] = domain_dict.get('.'.join(sub[i:]), 0) + counter

        # Formatters with replacement fileds or placeholders - {}
        # pass into the method the value you want to concatenate with STRING
        return ["{} {}".format(count, do) for do, count in domain_dict.items()]

if __name__ == '__main__':
    cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    print(Solution().subdomainVisits(cpdomains))