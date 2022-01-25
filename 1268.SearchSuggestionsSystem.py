class Solution:
    # Can optimize with binary search while iterating products using bisect.bisect_left
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        previousMatchingProducts = []
        result = []
        for i in range(len(searchWord)):
            currentMatchingProducts = []
            for j, product in enumerate(previousMatchingProducts):
                if product[i] == searchWord[i]:
                    currentMatchingProducts.append(product)
            if len(currentMatchingProducts) < 3:
                for product in products:
                    if len(currentMatchingProducts) == 3:
                        break
                    if product[:i+1] == searchWord[:i+1]:
                        currentMatchingProducts.append(product)
            result.append(currentMatchingProducts)
        return result