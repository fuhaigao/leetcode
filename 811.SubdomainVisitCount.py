class Solution:
    # 用 counter， key:domains, value:count
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = collections.Counter()
        for cpdomain in cpdomains:
            n, domain = cpdomain.split()
            counter[domain] += int(n)
            for i in range(len(domain)):
                if domain[i] == '.':
                    counter[domain[i+1:]] += int(n)
        result = []
        for key in counter:
            result.append(str(counter[key]) + " " + key)
        return result
            