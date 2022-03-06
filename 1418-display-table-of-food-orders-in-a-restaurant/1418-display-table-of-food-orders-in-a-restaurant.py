class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        tablesDict = {}
        items = set()
        for order in orders:
            tableNum = int(order[1])
            item = order[2]
            tnDict = tablesDict.get(tableNum, dict())
            itemCount = tnDict.get(item, 0)
            tnDict[item] = itemCount + 1
            tablesDict[tableNum] = tnDict
            items.add(item)
        items = sorted(list(items))
        result = [["Table"] + items]
        itemsDict = {}
        for i, item in enumerate(items):
            itemsDict[item] = i+1
        for tableNum in sorted(list(tablesDict.keys())):
            row = [str(tableNum)] + ["0"]*len(items)
            for item, count in tablesDict[tableNum].items():
                row[itemsDict[item]] = str(count)
            result.append(row)
        return result
            