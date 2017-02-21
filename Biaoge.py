#encoding=UTF-8
import pandas
import collections
class SingleTable:
    def __init__(self, tableName):
        self.tableData = pandas.DataFrame()
        self.desc = ""
        self.name = tableName

    def getColNames(self):
        return self.tableData.columns.tolist()

    def getRowNames(self):
        return self.tableData.index.tolist()

    def setValue(self, rowName, colName, value):
        if colName not in self.tableData.columns.tolist():
            self.tableData[colName] = "-"
        if rowName not in self.tableData.index.tolist():
            self.tableData.loc[rowName] = ["-"] * len(self.tableData.columns.tolist())
        self.tableData[colName][rowName] = value

    def getValue(self, rowName, colName):
        if colName not in self.tableData.columns.tolist() or rowName not in self.tableData.index.tolist():
            return "-"
        else:
            return self.tableData[colName][rowName]

class Biaoge:
    def __init__(self):
        self.tables = collections.OrderedDict()

    def _getTableByName(self, tableName):
        if tableName not in self.tables:
            self.tables[tableName] = SingleTable(tableName)
        return self.tables[tableName]

    def set(self, tableName, rowName, colName, value):
        table = self._getTableByName(tableName)
        table.setValue(rowName, colName, value)

    def setDesc(self, tableName, desc):
        table = self._getTableByName(tableName)
        table.desc = desc

    def getMarkdown(self):
        markdown = ""
        for name in self.tables:
            table = self.tables[name]
            markdown += "## " + name + '\n'
            markdown += table.desc + '\n'
            dt = []
            dt.append(['  '] + table.getColNames())
            dt.append(['---'] * (len(table.getColNames()) + 1))
            dt += map(lambda r: [str(r)] + map(lambda c: str(table.getValue(r, c)), table.getColNames()), table.getRowNames())
            colmaxlens = map(lambda q: max(q), zip(*map(lambda x: map(lambda y: len(y), x), dt)))
            markdown += '\n'.join(map(lambda r: '|' + '|'.join(['{:^{width}}'.format(r[i], width = colmaxlens[i]) for i in range(len(r))]) + '|', dt))
            markdown += '\n'
        return markdown

