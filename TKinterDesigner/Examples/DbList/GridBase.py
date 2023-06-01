import Fun
# TreeView作为表格使用时的相关操作
def addItem(uiName,TreeViewName,*item):
    treeview = Fun.GetElement(uiName,TreeViewName)
    treeview.insert('', 'end', values=(item[0], item[1], item[2]))
def editSelected(uiName,TreeViewName,*item):
    treeview = Fun.GetElement(uiName,TreeViewName)
    index = treeview.selection()
    if(len(index) == 0):
        return None
    treeview.set(index, '用户账号', item[0])
    treeview.set(index, '密码', item[1])
    return treeview.item(index)['values']
def deleteSelected(uiName,TreeViewName):
    treeview = Fun.GetElement(uiName,TreeViewName)
    index = treeview.selection()
    if(len(index) == 0):
        return None
    item = treeview.item(index)
    treeview.delete(index)
    return item['values']
def getSelected(uiName,TreeViewName):
    treeview = Fun.GetElement(uiName,TreeViewName)
    index = treeview.selection()
    if(len(index) == 0):
        return None
    return treeview.item(index)['values']
def clearData(uiName,TreeViewName):
    treeview = Fun.GetElement(uiName,TreeViewName)
    obj = treeview.get_children()
    for i in obj:
        treeview.delete(i)
    return treeview
'''
def loopData(uiName,TreeViewName):
    treeview = Fun.GetElement(uiName,TreeViewName)
    obj = treeview.get_children()
    for i in obj:
        item = treeview.item(i)
        print(item['values'])
'''
'''
gender = Fun.GetTKVariable(uiName,'Group_1')
if gender  == 1:
|   gender  ='男'
else:
|   gender  ='女'   
age = Fun.GetText(uiName,'Entry_8')
combobox = Fun.GetElement(uiName,'ComboBox_10')
address=combobox.get()
Fun.SetText(uiName,'Entry_3','')
Fun.SetTKVariable(uiName,'Group_1',1)
Fun.SetText(uiName,'Entry_8',0)
combobox.current(0)
'''