# 

# **TKinterDesigner 使用说明**

| Author | Honghaier  |
| -------: | ---------- |
| Version | V1.4.8     |
| Last Update Date | 2021-06-17 |
| Twitter: | honghaier_2020@Honghaier_game |
| Email: | 285421210@qq.com |
| QQ Group | 100180960 |

官方网址:www.tkinterdesigner.com


GitHub: https://github.com/honghaier-game/TKinterDesigner.git 

## TKinterDesigner是什么 ？

​	Tkinterdesigner是一个基于python的开发工具，用于开发基于tkinter界面的python应用程序项目。

## TKinterDesigner都有什么功能 ?

Tkinterdesigner v1.4.8 版本包括以下十项主要功能:



1. ###### 项目管理：创建并打开项目。

2. ###### 文件管理：创建界面、创建文件和导入项目资源。

3. ###### 界面设计：通过拖拽方式所见即所得的设计Tkinter界面。

4. ###### 控件设置：对控件进行基本属性的设置。

5. ###### 变量绑定：为Tkinter控件绑定自定义变量。

6. ###### 事件响应：为Tkinter的控制建立事件和函数之间的映射。

7. ###### 逻辑编写：事件函数的逻辑代码编写。

8. ###### 编译并运行：调用Python命令编译并运行项目。

9. ###### 打包程序：调用Python命令为项目打包exe。

10. ###### 自定义模块导入：导入并调用自定义模块。



## TKinterDesigner功能说明：

### 1. 项目管理：:

​		双击以启动tkinterdesigner.exe。第一步是进入项目管理界面。您可以根据需要在右上角选择语言。在这里我们选择汉语。

![](http://www.tkinterdesigner.com/ReadMeImages/1.png)

在这个界面中，我为选项提供了5个选项卡：
（1） 新Project: 提供了五个模版示例， 包括空白界面项目、对话框项目、单文档项目、多文档项目和网络爬虫。您只需选择相应的项目，点击“确定”即可完成项目的建立。如果需要更改项目路径，可以单击“更改路径”进行修改。

![](http://www.tkinterdesigner.com/ReadMeImages/2.png)

在这里，我们选择对话框界面项，然后单击“确定”。
项目创建成功后，我们将立即进入项目开发的主设计界面。我们可以通过右上角的关闭按钮返回到项目管理控制台。

![](http://www.tkinterdesigner.com/ReadMeImages/3.png)

（2） 打开项目：我们创建的所有项目都将显示在此面板列表中。我们只需要选择我们需要的项目，并点击“确定”进入项目。显示为加号的第一个按钮用于打开不在列表中的项目。

![](http://www.tkinterdesigner.com/ReadMeImages/4.png)

（3） 项目实例：我提供一些小案例作为参考，开发者可以开放学习，从而了解一些类似小项目的框架和实现。

![](http://www.tkinterdesigner.com/ReadMeImages/5.png)

例如，如果我们选择第四项“计算器”并单击“确定”，您将看到计算器界面项：

![](http://www.tkinterdesigner.com/ReadMeImages/6.png)

在这个主要的设计界面中，我们可以看到它的布局是：
（1） 顶部主菜单：1.视图：包括设计中使用的网格和吸附功能。您还可以通过Ctrl+G和Ctrl+D快速调用它。2.帮助：一些无用的信息，如果你需要找我，请看一下。
（2） 主菜单下的快捷按钮：框架按钮可以显示或隐藏框架结构树，运行按钮可以快速运行项目进行测试，发布按钮可以将项目打包发布为EXE程序。另外，还有一些常见的文字、颜色和对齐设置快捷按钮，相信大家不用解释就能知道它们是如何使用的。
（3） 最左边的框架树：包括项目中所有文件的列表。记住：您还可以通过右键单击弹出的菜单添加窗体接口、添加python文件或导入资源文件。如果您正在设计界面，框架结构树将影响您的查看窗口空间，您可以单击框架按钮来显示或隐藏它。
（4） 左边的控件和模块列表选择区：对于界面设计中需要的常用控件，我在这里列出了它们。虽然不是全部，但随着更新，相信会逐渐丰富起来。在这里，模块选择区域用于导入自定义模块。在实际的案例项目中，有一些定制的模块类和项目中使用的案例，例如'Express'或'ChatServer'，您可以稍微看一下，它只需要有一定的设计约束。我将在第七部分详细介绍函数。
（5） 中央设计预览区：界面设计的主要视觉区域。您可以在这里拖动、放置和拉伸所有必需的接口控件。生成的接口可用。
（6） 当前界面右上角所有控件列表树：列出当前界面的所有控件。您可以单击相应的树项来选择相应的控件，也可以通过右键单击鼠标在弹出菜单中删除它。
（7） 右下角当前选中控件的属性列表项：列出当前选中控件对应的所有属性。您可以双击相应的属性项在此处进行修改。
（8） 底部的信息文本：显示当前控件的位置和大小信息。

### 2. 文件管理

1. 最左边的框架结构树列出了当前项目中的文件。以对话框项目为例，可以看到框架结构树下有一个以项目名称命名的根节点项，下面有五个文件项
  1.有趣。Py：这是一个公共函数库文件，提供对控件和控制变量的访问。
  2.图标。PNG：这是项目的图标文件，在创建时生成，前提是在tkinder设计器的目录中有一个ICO目录。
  3.JSQ.Py：这是项目主界面的python文件，为界面的基本布局提供代码支持。
  4.JSQ_cmd.py：项目主界面的逻辑文件，为接口的逻辑提供代码支持。这里主要对控件的事件函数进行编码。
  5.JSQ_sty.py：这是项目的样式设置文件。它提供TTK的样式设置。如果在此处添加自定义样式，则可以设置控件。

![](http://www.tkinterdesigner.com/ReadMeImages/7.png)

当我们点击“Fun. Py” 或 “JSQ_cmd.py”，主视图区域成为代码区域：
由于软件的设计是使用表单设计器而不是修改表单界面的代码，所以当您单击“JSQ.py”时，主视图将显示界面。对于逻辑代码和函数库代码，希望开发人员能够编写、修改和调试更多的逻辑代码。因此，显示代码文本区域和信息输出窗口，方便随时修改代码，并在编译运行时查看输出。
如果我们想在项目中创建多个窗口，我们可以在框架结构树中添加一个新的接口。例如，我们可以打开新建的对话框界面项目，右键单击左侧的框架结构树。

![](http://www.tkinterdesigner.com/ReadMeImages/8.png)

在弹出菜单中，点击“新建窗体”，在这里我们可以看到一个新的弹出对话框，我们可以输入新窗体的名称，然后点击“确定”。

![](http://www.tkinterdesigner.com/ReadMeImages/9.png)

单击“确定”后，我们会看到一个新窗口，包括“Mywindow.py” 和 “Mywindow_cmd.py” 两个文件，分别对应于Mywindow的表单布局和逻辑实现。
如果要添加自己的逻辑代码，可以在框架树的弹出菜单项上单击鼠标右键，单击“新建文件”，输入新文件的名称，就可以创建一个新的Python文件。

![](http://www.tkinterdesigner.com/ReadMeImages/10.png)

单击“确定”后，您可以看到新的文件代码，然后您可以开始编写代码。

![](http://www.tkinterdesigner.com/ReadMeImages/11.png)

​    有时，您可能需要一些图片、声音或其他文件资源来放入项目中。您也可以通过右键单击框架结构树中的弹出菜单项并单击“导入文件”来选择和导入它们。.

​	最后，如果要删除其中一个文件，需要右键单击相应的文件项，弹出菜单项，单击“删除文件”。确认后，可以删除该文件。

### 3. 界面设计

​	首先，我们加载前面创建的对话框项目。

![](http://www.tkinterdesigner.com/ReadMeImages/12.png)

   单击project1或project1.py进入界面设计区域，然后开始界面设计。例如，如果要在基本帐户和密码输入界面中添加性别选项、职业分类和已婚与否，则需要添加一些新控件，包括两个单选按钮和一个组合框、一个复选按钮和所需的标签文本。这些是非常常见的控件。

​	我们需要扩大主要形式，因为它的规模还不够。此时，您可以点击右上角的控件树项 "Form_1" ，也可以直接点击设计区域中的表单界面，我们可以看到表单周围出现虚线，在顶点和边线的中点处出现一个灰色的拖动块。我们可以单击鼠标右下角的拖动块并将其拖动到适当的大小。

![](http://www.tkinterdesigner.com/ReadMeImages/13.png)

​	完成后，我们可以将“确定”和“退出”按钮直接拖动到右下方的位置。

![](http://www.tkinterdesigner.com/ReadMeImages/14.png)

​	现在，我们可以从左侧工具栏列表中选择并拖动所需控件到表单。

![](http://www.tkinterdesigner.com/ReadMeImages/15.png)

**这里有一个技巧。如果需要重复创建同一个控件，可以直接选择一个控件，在按住ALT键的状态下进行拖动。可以直接复制控件以供拖动。**

如果您感觉位置没有很好对齐，可以在快捷键中选择“网格”和“抽吸”按钮，也可以通过键“Ctrl+G”、“Ctrl+D”快速调用显示或取消。网格为每10像素单位，便于您在吸入后拖动和对齐。

![](http://www.tkinterdesigner.com/ReadMeImages/16.png)

好的，现在我们已经完成了所需控件的创建，它非常简单吗？
让我们在下面设置这些控件。

### 4. 控件设置

选中“性别”单选按钮前的标签，在右侧的属性框中找到“文本”属性，双击该属性，在弹出的对话框中输入“性别”，单击“确定”即可更改相应标签的文本。

![](http://www.tkinterdesigner.com/ReadMeImages/17.png)

**这里有一个技巧。如果您需要设置标签或按钮的文本，当它聚焦时按一下键，就可以看到输入字符串对话框。**	

​    所以，很快我们完成了所有的标签，两个单选按钮的文本和复选按钮的文本。

​	看起来不错，不是吗？当然，可以设置很多属性，比如可以修改背景色和文字颜色，也可以修改字体等等。可以在属性栏中修改这些操作，也可以通过顶部的快捷按钮栏快速调整这些操作。

​	当然，性别不能同时是男性和女性。这样的双性恋不符合我们的取向，对吧？我们选择带有“女性”字样的单选按钮。在分组和值列中，双击值项，在输入框中将其更改为2，然后单击按钮。然后我们可以看到正确的单选按钮分组。



![](http://www.tkinterdesigner.com/ReadMeImages/18.png)



​	一个界面中可以有许多单选按钮。其中一些可能是一种选择，如性别，一些是另一种选择，如生活在城市的几个地区。这两部分需要分为两组，并且需要通过每组中的唯一值来区分。因此，当代表“男性”和“女性”的两个单选按钮使用默认组号1时，您只需要将对应于“女性”的单选按钮的值更改为2。

​    接下来，我们为输入添加职业选项。选择Combobox，在其属性框中找到“Items”，在数据项编辑区弹出的对话框中双击编辑Combobox对应的数据项。

​    例如，我们输入三个数据，即“程序员”、“计划员”、“设计师”，然后单击“确定”，我们可以看到组合框变成了所需的形状。

![](http://www.tkinterdesigner.com/ReadMeImages/19.png)

单击“确定”后，最终结果如下：

![](http://www.tkinterdesigner.com/ReadMeImages/20.png)

单击“运行”或按F5键，将自动保存设计和代码，并编译运行结果。

![](http://www.tkinterdesigner.com/ReadMeImages/21.png)

​	此示例演示了几个常用控件的属性设计和使用。您可以自己尝试其他控件，这里不再重复。如果你有问题，请给我发邮件:285421210@qq.com 或访问 :www.tkinterdesigner.com 进行反馈.

### 5.变量绑定

​	在开发过程中，我们经常需要存储一些数据，也许只是简单的结果存储，也许是控件的输入值。例如，在实例项目JSQ（Calculator的意思）的开发中，我们绑定了一个临时变量来存储显示数据的标签的中间值，以便进行加、减、乘、除操作。在上面的例子中，假设当我们点击“确定”来判断账户值与上次输入的值相同时，会弹出一个对话框提示“账户已使用”。我们可以添加一个自定义变量来绑定帐户。这个设计思路是对VC++的一个参考，如果你有VC++开发经验，想信可以很快理解。

![](http://www.tkinterdesigner.com/ReadMeImages/22.png)

​	右键点击账户对应的输入框，在弹出菜单中点击“变量绑定”。在弹出的对话框中，我们输入要绑定的数据项的名称“NameArray”，并选择它作为“List”类型。如果我们使用数字类型或字符串类型，我们可以看到一个选项框“映射到'文本'”，点击此选项意味着变量将更新为标签或条目控件的文本，同时函数将被激活。调用Fun.SetUserData进行设置。同一控件只允许有一个变量。如果未选择此项，则可以为控件创建多个变量。我们不需要点击这里。

![](http://www.tkinterdesigner.com/ReadMeImages/23.png)



​	创建之后，在输入框中将有一个绑定列表变量。你可以用`Fun.GetUserData(className,‘Entry_3’,’NameArray’)`  获取它。
​    接下来，让我们在单击“OK”按钮时做出相关判断，这需要为“OK”按钮添加命令事件映射。

### 6. 事件函数映射

所谓“事件函数映射”，就是对可以绑定到控制的事件进行函数映射，这样当触发相应的事件时，调用set函数。
我们右键单击“OK”按钮，然后在弹出菜单中选择“事件响应”。

![](http://www.tkinterdesigner.com/ReadMeImages/24.png)

在弹出的事件响应处理编辑区域中，我们可以看到左侧的事件列表，其中列出了常见的Python事件。右边有一个输入框，显示默认函数名。我们也可以修改它。点击“编辑功能代码”，直接进入逻辑文件的代码编辑区。此时，我们可以看到添加的事件响应函数，在这里我们可以手动编辑代码。

![](http://www.tkinterdesigner.com/ReadMeImages/25.png)

对于按钮，也可以像VC++一样直接双击进入命令功能。

![](http://www.tkinterdesigner.com/ReadMeImages/26.png)

如果我们想在事件响应中调用其他接口，我们也可以点击“调用其他接口”按钮，然后弹出一个选项对话框，让我们根据需要调用。

![](http://www.tkinterdesigner.com/ReadMeImages/27.png)


这里可以直接选择最常用的打开和保存文件框，但是如果您创建了一个多窗口程序，您需要在这里调用另一个窗口，只需选择“调用自定义接口”就可以找到要调用的py文件。我在示例项目中有一个“calltest”项目来演示这一点。

### 7. Logic code writing

按钮在逻辑文件的代码编辑区，在“Button\u 6\u oncommand”函数中，我们可以编写以下代码：

![](http://www.tkinterdesigner.com/ReadMeImages/28.png)

此代码通过“Fun.GetUserData”获取绑定到输入框的列表变量，并通过“Fun.GetText”直接获取当前输入值，然后进行比较。如果相同，将弹出“名称已注册”对话框。如果它们不同，输入值将添加到列表变量中，并弹出“注册成功”对话框。

### 8. 编译并运行

如果您想立即编译和运行，可以直接按F5或单击右上角的“RunF5”按钮。程序代码将自动保存，并开始编译和运行。如果代码中有错误，则将显示在代码区域的编译错误信息输出窗口中。如果将打印添加到该功能中，则也会实时显示打印。

![](http://www.tkinterdesigner.com/ReadMeImages/29.png)

我们在运行程序的帐户中输入名称，第一次单击“确定”时，会弹出“注册成功”对话框。然后再次点击OK，弹出“姓名已注册”对话框。
我们仍然可以通过改名成功注册。似乎一切都和我们预期的一样。

![](http://www.tkinterdesigner.com/ReadMeImages/30.png)

​	

### 9. 打包EXE

在完成我们自己的程序后，我们希望将程序打包为EXE并发布给用户。我们可以直接点击右上角的“发布”按钮，选择输出目录，然后输入要打包的EXE的名称。



![](http://www.tkinterdesigner.com/ReadMeImages/31.png)

单击“确定”按钮，tkinterdesigner将开始调用打包程序来打包项目。

![](http://www.tkinterdesigner.com/ReadMeImages/32.png)

如果进展顺利，您最终可以在输出目录中找到相应的exe程序：

![](http://www.tkinterdesigner.com/ReadMeImages/33.png)

### 10. 自定义模块导入

我把自定义模块放在最后，因为您不必使用它，但它可以很容易地扩展您的项目。在示例项目“express”中，它同时用于查询和服务器。

![](http://www.tkinterdesigner.com/ReadMeImages/34.png)

简而言之，您可以为多个要使用的项目编写自定义模块类。您可以在设计器中轻松设置模块类的属性，包括将接口控件作为参数传递给它。
我们以项目express为例，对查询开发过程进行简单的说明。
首先，我们需要创建一个空白项目，右键单击框架文件的树项，在弹出菜单中创建一个python文件，然后将其命名为“Express.py“的。在这个文件中，我们需要创建一个express类来按关键字查询express结果。该类的完整代码如下：

```
iimport urllib.request
import json
import msvcrt
import tkinter

class   Express:
    def __init__(self):
        self.Company_Dict = {1:'shentong',2:'youzhengguonei',3:'yuantong',4:'shunfeng',5:'yunda',6:'zhongtong',7:"tiantian",8:"debang"}
        self.CompanyID = 4
        self.ExpressNumber = '0000001'
        self.ComboBox = None
    #set CompanyID
    def set_CompanyID(self,companyID):
        self.CompanyID = companyID
    #get CompanyID
    def get_CompanyID(self):
        return self.CompanyID
    #set ExpressNumber
    def set_ExpressNumber(self,expressNumber):
        self.ExpressNumber = expressNumber
    #get ExpressNumber
    def get_ExpressNumber(self):
        return self.ExpressNumber   
    #set ComboBox
    def set_ComboBox(self,comboBox):
        self.ComboBox = comboBox
        # These are some express company 's name in China.
        self.ComboBox['values'] = ['申通快递','EMS邮政','圆通快递','顺丰快递','韵达快递','中通快递','天天快递','德邦快递']
        self.ComboBox.current(4)
    #get ComboBox
    def get_ComboBox(self,comboBox):
        return self.ComboBox   
    #Query
    def Query(self,ListBox):
        self.CompanyID = self.ComboBox.current() + 1
        ListBox.delete(0,tkinter.END)
        url = "http://www.kuaidi100.com/query?type=%s&postid=%s" % (self.Company_Dict[self.CompanyID], self.ExpressNumber)
        response = urllib.request.urlopen(url)
        html = response.read().decode('utf-8')
        target = json.loads(html)
        #print(target)
        status = target['status']
        if status == '200':
            data = target['data']
            #print(data)
            data_len = len(data)
            
            for i in range(data_len):
                time_text = "Time: " + data[i]['time']
                ListBox.insert(tkinter.END,time_text)
                state_text = "State: " + data[i]['context']
                ListBox.insert(tkinter.END,state_text)
        else:
            ListBox.insert(tkinter.END,"Error")
```

编写自定义模块类的方法只有一种：如果要在设计器中向其传递参数，则需要对模块加入set和get函数。所以我们设计了三个变量的函数，包括快递公司的公司ID、快递编号，我们希望传入一个控件组合框来接受公司名称列表。
如果您觉得编写当前项目代码不方便，也可以使用vscode或您喜爱的代码编辑器来编写代码，或者直接导入或复制“Express”。从实例项目中选择“py”。

不管怎样，你只有这个代码。

回到主界面设计区域，快速构建界面：

![](http://www.tkinterdesigner.com/ReadMeImages/35.png)

现在我们已经完成了界面的设计，我们将切换到工具栏的“模块”页面。在“模块”页面中，我们单击“import module”按钮，然后找到“Express”。点击“打开”。实际上，“Express.py”不必在当前目录中。您可以将一个模块用于多个项目，只需在此处导入，而不需要为用于同一模块的每个项目创建模块类文件。

![](http://www.tkinterdesigner.com/ReadMeImages/36.png)

好的，现在express模块项出现在模块面板上，让我们把它拖到界面上。

![](http://www.tkinterdesigner.com/ReadMeImages/37.png)

我们可以看到，在右下角的属性框中，express模块的三个变量显示在属性框中。我们可以手动设置“CompanyID”和“ExpressNumber”，但是如何设置组合框呢？在这里，您只需要在右上角的控件树中找到相应的组合框，然后拖动到属性框中“combobox”的值项位置。

![](http://www.tkinterdesigner.com/ReadMeImages/38.png)

然后我们将命令响应函数添加到“query”按钮。

![](http://www.tkinterdesigner.com/ReadMeImages/39.png)

在“Button_8_oncommand”函数中，我们可以编写相应的代码：

![](http://www.tkinterdesigner.com/ReadMeImages/40.png)


​    

这部分代码实现了从Entry_5获取ExpressNumber，并通过我们的moudle name“Express_9”调用'Fun.GetElement'来获取Express模块，并使用相同的方法来获取Listbox，然后调用Express的函数`set_ExpressNumber`设置快递号，最后调用查询方法进行查询。参数是显示的ListBox对象。
     代码太多了。完成后，按F5运行它。我们可以看到正在运行的程序。尝试在快递订单号中输入号码后，点击“查询”，很快就会看到列表框中显示的快递信息。

 ![](http://www.tkinterdesigner.com/ReadMeImages/41.png)

​	这是如何使用自定义模块。

### 关于我

网名: honghaier
国籍: China
技能: C + +, game development
自我评估: 程序员，开发者，创业者

### 关于 TKinterDesigner 

因为我用VC++已经有十多年了，用Python开发软件的时候，我希望能很快建立界面，但是我就是懒，不想多学。我会继续改进的。我希望有兴趣的Python爱好者能和我交流，给我更多的建议，因为我还没有读完Python的书，我也不知道太多的需求，但是我对Python在快速原型中对接口工具的要求很乐观，希望Python能越来越好。
最后，祝大家工作顺利，身体健康~

​                                                                                                           Honghaier

​																											2021/06/17

