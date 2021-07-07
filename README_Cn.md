

#####                                                                                                                                                                                 专注于Tkinter桌面应用软件开发，让一切变的简单！

# **TKinterDesigner 使用说明**

| Author | Honghaier  |
| -------: | ---------- |
| Version | V1.5.1     |
| Last Update Date | 2021-07-01 |
| Twitter: | honghaier_2020@Honghaier_game |
| Email: | 285421210@qq.com |
| QQ Group | 100180960 |

官方网址:www.tkinterdesigner.com


GitHub: https://github.com/honghaier-game/TKinterDesigner.git 

## TKinterDesigner是什么 ？

​	Tkinterdesigner是一个基于python的开发工具，用于开发基于tkinter界面的python应用程序项目。但它与其它类型的开发工具的最大不同之处在于，它提供了一套完整的开发流程，目前python并不缺开发IDE，缺的是合理科学的开发流程，缺的是应对大量模块方向的辅助工具。Tkinterdesigner是一套Python进行应用软件开发的解决方案，包括了从项目创建到界面设计，再到事件逻辑编辑与调试运行到打包发布的整体开发流程，以及在这个基础上建立的资源平台和开发者生态。



## TKinterDesigner的开发流程是什么？

​		![](http://www.tkinterdesigner.com/ReadMeImages/0.png)



## TKinterDesigner都有什么功能 ?

Tkinterdesigner v1.5.1 版本包括以下十项主要功能:



1. ###### 项目管理：创建并打开项目。

2. ###### 文件管理：创建界面、创建文件和导入项目资源。

3. ###### 界面设计：通过拖拽方式所见即所得的设计Tkinter界面。

4. ###### 控件设置：对控件进行基本属性的设置。

5. ###### 变量绑定：为Tkinter控件绑定自定义变量。

6. ###### 事件响应：为Tkinter的控制建立事件和函数之间的映射。

7. ###### 逻辑编写：事件函数的逻辑代码编写。

8. ###### 调试运行：调用Python命令调试、运行项目。

9. ###### 打包程序：调用Python命令为项目打包exe。

10. ###### 自定义模块导入：导入并调用自定义模块。

    

## TKinterDesigner启动：

​	  双击TKinterDesigner程序，可以看到一个控制台界面，在这个页面，您可以根据需要在右上角选择语言，目前提供了五种语言：英语，简体中文，繁体中文，日语，韩语。在这里我们选择简体中文，如果我们当前版本不是最新版本，我们可以看到最新版本提示，点击即可打开最新版本的下载页。

​		![](http://www.tkinterdesigner.com/ReadMeImages/1A.png)

​		默认情况下是离线使用，如果你需要使用会员和导出功能，可以点击**GUEST**图标进行登录。

## TKinterDesigner注册与登录：

​    	点击Guest图标，会看到一个登录界面如下。

​		![](http://www.tkinterdesigner.com/ReadMeImages/1.png)

​		输入账号和密码后点击”登录“按钮即可登录，如果没有账号，可以点击”注册？“文字进入注册界面，填写“账号",”密码“,邮箱等信息后点击“注册“按钮，注册成功后会自动登录。如果不想注册，也可以直接点击”离线使用“。

​		![](http://www.tkinterdesigner.com/ReadMeImages/2.png)

​		登录成功后，会进入到项目管理页面，这里会显示登录名称，你将拥有更多的会员权益，比如在这里你可以看到出现了“组件市场''和"皮肤市场”。

![](http://www.tkinterdesigner.com/ReadMeImages/3.png)



## TKinterDesigner功能说明：

## 1. 项目管理：

  项目管理页面为选项提供了5个选项卡：

### （1） 新建项目： 

​	提供了五个模版示例， 包括空白界面项目、对话框项目、单文档项目、多文档项目和网络爬虫。您只需选择相应的项目，点击“确定”即可完成项目的建立。如果需要更改项目路径，可以单击“更改路径”进行修改。

#### <1>."空界面"项目

如果我们选择空界面，然后单击“确定”。

![](http://www.tkinterdesigner.com/ReadMeImages/57.png)

我们选择”对话框“项目，然后单击“确定”。在这个主要的设计界面中，我们可以看到它的布局是：
（1） **顶部主菜单**：包括了软件的主要菜单项，目前分为"TKinterDesigner"、"编辑"、"视图"、"帮助"四项，其中"TKinterDesigner"中最重要的是有"设置"项，在设置项里，我们可以对TKinterDesigner的一些可选项进行设置，我在这里简单介绍一下。

![](http://www.tkinterdesigner.com/ReadMeImages/128.png)

首先是“**常用设置**”，它下面有四个可选项：

- **Python目录**：对未将Python目录设置到系统Path的用户，需要在这里设置正确才可以正常的运行和发布。

- **颜色方案**：提供深色和浅色两种颜色方案供用户选择，默认深色，后续可能跟据需要扩展。

- **语言**：提供简体中文，繁体中文，英语，日语，韩语五种语言支持，后续跟据需要扩展。

- **边框透明色值**：是用于对话框在没有标题栏时做圆角形态时，对圆角外使用边框透明色镂空时设置的透明色值。

  

![](http://www.tkinterdesigner.com/ReadMeImages/129.png)

然后是**“设计操作”**项。

- **自动保存**：这里可以设置采用自动保存还是手动保存，默认自动保存，就是每项操作都保存。手动保存的话，就需要在需要保存时按Ctrl+S来进行保存。

- **操作记录数**：用于设置最多可以多少步操作内进行保存。

- **控件拖拽方式**：一般情况下是直接用鼠标进行拖拽移动，也可以选择CTRL键 + 鼠标左键进行拖拽移动，但始终支持使用鼠标中键拖拽移动。

- **控件滚轮缩放**：一般情况下是直接用一次性使用口罩进行拖拽移动，也可以选择CTRL键 + 鼠标左键进行拖拽移动，但始终支持使用鼠标中键拖拽移动。

  

![](http://www.tkinterdesigner.com/ReadMeImages/130.png)

第三项是**“代码编辑”**项。

- **字体大小**：代码区的文字大小设置。
- **字体名称**：代码区的文字字体设置。
- **鼠标滚轮缩放**：选择对应的方式可直接通过鼠标滚轮缩放字体。

（2） **主菜单下的快捷按钮**：框架按钮可以显示或隐藏框架结构树，运行按钮可以快速运行项目进行测试，发布按钮可以将项目打包发布为EXE程序。另外，还有一些常见的对齐设置，文字字体，前景背景颜色，图片背景快捷按钮。

![](http://www.tkinterdesigner.com/ReadMeImages/131.png)

（3） **最左边的项目框架文件树**：包括项目中所有文件的列表。记住：您还可以通过右键单击弹出的菜单添加窗体接口、添加python文件或导入资源文件。如果您正在设计界面，框架结构树将影响您的查看窗口空间，您可以单击"框架"按钮来显示或隐藏它。
（4） **控件和模块工具栏**：对于界面设计中需要的常用控件，我在这里列出了它们。虽然不是全部，但随着更新，相信会逐渐丰富起来。在这里，模块选择区域用于导入自定义模块。在实际的案例项目中，有一些定制的模块类和项目中使用的案例，例如'Express'或'ChatServer'，您可以稍微看一下，它只需要有一定的设计约束即可使用，在后面自定义模块部分将会讲到。
（5） **中央设计预览区**：界面设计的主要视觉区域。您可以在这里拖动、放置和拉伸所有必需的接口控件。生成的接口可用。
（6） **当前界面右上角所有控件列表树**：列出当前界面的所有控件。您可以单击相应的树项来选择相应的控件，也可以通过右键单击鼠标在弹出菜单中删除它。
（7） **右下角当前选中控件的属性列表项**：列出当前选中控件对应的所有属性。您可以双击相应的属性项在此处进行修改。
（8） **底部的信息文本**：显示当前控件的位置和大小信息。 

#### <2>."对话框"项目

“空界面”项目给了开发者最简单的方式从头设计界面和项目，但如果你想基于其它现有的模版来进行项目开发，可以通过右上角的关闭按钮返回到项目管理控制台，然后选择”对话框“项目模版。

![](http://www.tkinterdesigner.com/ReadMeImages/59.png)

​	创建成功后，我们将立即进入一个拥有简单对话框的项目中。

![](http://www.tkinterdesigner.com/ReadMeImages/4.png)

​	在”对话框“项目中，我们进行了基本的简单界面设计，并给按钮事件增加了相应的逻辑功能，你可以直接点击右上角”运行“来尝试它。

![](http://www.tkinterdesigner.com/ReadMeImages/58.png)

​	这是一个简单的例子，但大多数情况下，这可能是一个复用率比较高的例子。

#### <3>."单文档"项目

​	再次回到控制台，我们再来看一下单文档项目模版：

![](http://www.tkinterdesigner.com/ReadMeImages/60.png)

​	创建成功后，我们将看到一个单文档Python编辑器项目。

![](http://www.tkinterdesigner.com/ReadMeImages/61.png)

​    运行起来，你可以直接用它写代码的。

![](http://www.tkinterdesigner.com/ReadMeImages/62.png)

  在这个项目中，你可以看到它有一个完整的菜单，这是怎么做的呢？

![](http://www.tkinterdesigner.com/ReadMeImages/64.png)

​	我在上面的截图中详细说明了这个过程，一旦你建立了菜单，TKinterDesigner会自动为你创建出对应的响应消息函数，你只需要在对应的cmd.py中为菜单项的消息函数编写具体的逻辑代码就可以了，可以在后面的项目中多多尝试。

#### <3>."多文档"项目

​		再次回到控制台，我们再来看一下多文档项目模版：

![](http://www.tkinterdesigner.com/ReadMeImages/63.png)

​	创建成功后，我们将看到一个多文档Python编辑器项目，它使用了分割窗体。

![](http://www.tkinterdesigner.com/ReadMeImages/65.png)

​	在这个项目里，我们实现了分割窗体与页面嵌入，你可以利用这个功能来做一些独立的界面并通过嵌入的方式来把它们组合到一个界面中，TKinterDesigner目前支持Frame，NoteBook和PanedWindow三种嵌入模式。其中Frame是用来嵌入一个页面，NoteBook用来为每个页嵌入对应的页面，PanedWindow用来为分割的两个部分嵌入对应的页面，操作时只需要按照对应属性去设置就可以了。

​	在这个实例中，我们可以看到运行时，点击左边的树项文件，右边的文本框会显示对应的内容，并可以如单文档一样的运行和打印Python文件结果。

![](http://www.tkinterdesigner.com/ReadMeImages/66.png)

#### <4>."网络爬虫"项目

​		![](http://www.tkinterdesigner.com/ReadMeImages/67.png)

​	网络爬虫现在是一个热点方向，我们也把他放入到项目模版里了，在这个项目中，我们基于多文档的框架，实现了一个网络爬图片的工程。

​		![](http://www.tkinterdesigner.com/ReadMeImages/68.png)



​	为了更好的吸引人气，这里我们用一个下载美女图片的例子来演示，如果你有时候心情不太好，可以多放松一下眼睛。

​		![](http://www.tkinterdesigner.com/ReadMeImages/69.png)

​		以上就是四种新建项目的模版示例，虽然还不能满足所有的项目需求，但是我会继续努力扩增，也欢迎你提出宝贵的方向性建议，如果入选，我会将它增加到模版中提供出来。



### （2） 打开项目：

我们创建的所有项目都将显示在此面板列表中。我们只需要选择我们需要的项目，并点击“确定”进入项目。显示为加号的第一个按钮用于弹出文件"浏览"对话框打开电脑上不在列表中的项目。

![](http://www.tkinterdesigner.com/ReadMeImages/70.png)

### （3） 项目实例：

我提供一些小案例作为参考，开发者可以开放学习，从而了解一些类似小项目的框架和实现。

![](http://www.tkinterdesigner.com/ReadMeImages/6.png)

​	这些案例包括：

1. **注册调用**：演示在一个界面里通过点击按钮事件弹出另一个注册对话框。

   ![](http://www.tkinterdesigner.com/ReadMeImages/49.png)

2. **SQLite增删查改**：演示对Python自带的数据库SQLite进行增删查改。

   ![](http://www.tkinterdesigner.com/ReadMeImages/50.png)

3. **嵌入面板**：演示如何在画板Canvas和选项卡Notebook中进行其它界面嵌入。

   ![](http://www.tkinterdesigner.com/ReadMeImages/51.png)

4. **快递查询**：演示如何用自编写的模块插件完成快递查询和界面控件交互的功能。

   ![](http://www.tkinterdesigner.com/ReadMeImages/52.png)

5. **计算器**：演示了如何快速开发一款可进行加减乘除运算的计算器软件。

   ![](http://www.tkinterdesigner.com/ReadMeImages/53.png)

6. **网络聊天**：演示了如何开发一款带界面的服务器和客户端聊天程序软件。

   ![](http://www.tkinterdesigner.com/ReadMeImages/54.png)

7. **股价查询**：演示了如何调用股票查询接口进行股票查询。

   ![](http://www.tkinterdesigner.com/ReadMeImages/55.png)

8. **浏览器**：演示了如何开发一个自己的浏览器软件。

![](http://www.tkinterdesigner.com/ReadMeImages/56.png)

这些实例都是使用TKinterDesigner设计开发的，它让我们感到由衷的自豪，因为整个过程中，我们没有再为界面设计和事件处理花费多少时间，只把精力放在核心功能类上即可快速完成项目的开发。后面我们会加入更多的实例工程，以帮助大家更好的学习和掌握TKinterDesigner。

​		

### 2. 文件管理

​	我们打开《计算器》这个工程实例，可以看到最左边的框架结构树列出了当前项目中的文件。框架结构树下有一个以项目名称命名的根节点项，下面有五个文件项:
1.Fun.Py：这是一个公共函数库文件，提供对控件和控制变量的访问和一些常用函数，不建议修改，所以这里不支持直接编辑。

![](http://www.tkinterdesigner.com/ReadMeImages/8.png)

2.ico.png：这是项目的图标文件，在创建时生成，前提是在TkinterDesigner的目录中有一个ICO目录，在这里因为是实例工程，我把ico改成了实例的样子。

![](http://www.tkinterdesigner.com/ReadMeImages/71.png)

3.JSQ.Py：这是项目主界面的控件布局python文件，为界面的基本布局提供代码支持，虽然它是Py文件，但TKinterDesigner在读取它时，会发现它是界面文件，就直接进入设计模式了，因为在整个开发环节，一般是不建议你手动处理界面控件布局python文件的。

![](http://www.tkinterdesigner.com/ReadMeImages/72.png)

4.JSQ_cmd.py：项目主界面的逻辑文件，为接口的逻辑提供代码支持。这里主要对控件的事件函数进行编码，并可以进行断点调试。

![](http://www.tkinterdesigner.com/ReadMeImages/73.png)

5.JSQ_sty.py：这是项目的样式设置文件，它提供控件的样式编辑，如果在此处添加自定义样式，则可以直接设置给控件。

![](http://www.tkinterdesigner.com/ReadMeImages/74.png)


如果我们想在项目中创建多个窗口，我们可以在框架结构树中添加一个新的接口。例如，我们可以打开新建的对话框界面项目，右键单击左侧的框架结构树。

![](http://www.tkinterdesigner.com/ReadMeImages/9.png)

在弹出菜单中，点击“新建窗体”，在这里我们可以看到一个新的弹出对话框，我们可以输入新窗体的名称，然后点击“确定”。

![](http://www.tkinterdesigner.com/ReadMeImages/10.png)

单击“确定”后，我们会看到一个新窗口，包括“Mywindow.py” 和 “Mywindow_cmd.py” 两个文件，分别对应于Mywindow的表单布局和逻辑实现。
如果要添加自己的逻辑代码，可以在框架树的弹出菜单项上单击鼠标右键，单击“新建文件”，输入新文件的名称，就可以创建一个新的Python文件。

![](http://www.tkinterdesigner.com/ReadMeImages/11.png)

单击“确定”后，您可以看到新的文件代码，然后您可以开始编写代码。

![](http://www.tkinterdesigner.com/ReadMeImages/12.png)

​    有时，您可能需要一些图片、声音或其他文件资源来放入项目中。您也可以通过右键单击框架结构树中的弹出菜单项并单击“导入文件”来选择和导入它们。.

​	最后，如果要删除其中一个文件，需要右键单击相应的文件项，弹出菜单项，单击“删除文件”。确认后，可以删除该文件。

### 3. 界面设计

​	首先，我们加载前面创建的对话框项目。

![](http://www.tkinterdesigner.com/ReadMeImages/13.png)

   单击project1或project1.py进入界面设计区域，然后开始界面设计。例如，如果要在基本帐户和密码输入界面中添加性别选项、职业分类和已婚与否，则需要添加一些新控件，包括两个单选按钮和一个组合框、一个复选按钮和所需的标签文本。这些是非常常见的控件。

​	我们需要扩大主要形式，因为它的规模还不够。此时，您可以点击右上角的控件树项 "Form_1" ，也可以直接点击设计区域中的表单界面，我们可以看到表单周围出现虚线，在顶点和边线的中点处出现一个灰色的拖动块。我们可以单击鼠标右下角的拖动块并将其拖动到适当的大小。

![](http://www.tkinterdesigner.com/ReadMeImages/14.png)

​	完成后，我们可以将“确定”和“退出”按钮直接拖动到右下方的位置。

![](http://www.tkinterdesigner.com/ReadMeImages/15.png)

​	现在，我们可以从左侧工具栏列表中选择并拖动所需控件到表单。

![](http://www.tkinterdesigner.com/ReadMeImages/16.png)

**记住这个技巧。如果需要重复创建同一个控件，可以直接选择一个控件，在按住ALT键的状态下进行拖动，可以直接复制一个新的控件以供拖动，这样更快。**

如果您感觉位置没有很好对齐，可以在快捷键中选择“网格”和“抽吸”按钮，也可以通过键“Ctrl+G”、“Ctrl+D”快速调用显示或取消。网格默认为每50像素单位，便于您在吸入后拖动和对齐。

![](http://www.tkinterdesigner.com/ReadMeImages/17.png)

​	

选中“性别”单选按钮前的标签，在右侧的属性框中找到“文本”属性，双击该属性，在弹出的对话框中输入“性别”，单击“确定”即可更改相应标签的文本。

![](http://www.tkinterdesigner.com/ReadMeImages/18.png)

**这里也有一个技巧。如果您需要设置标签或按钮的文本，当它处于选中时你可以先按一下CTRL + BACKSPACE对文字进行清空，然后直接键盘输入文字就可以了。**	

​    所以，很快我们完成了所有的标签，两个单选按钮的文本和复选按钮的文本。

​	看起来不错，不是吗？当然，可以设置很多属性，比如可以修改背景色和文字颜色，也可以修改字体等等。可以在属性栏中修改这些操作，也可以通过顶部的快捷按钮栏快速调整这些操作。

​	当然，性别不能同时是男性和女性。这样的双性恋不符合我们的取向，对吧？我们选择带有“女性”字样的单选按钮。在分组和值列中，双击值项，在输入框中将其更改为2，然后单击按钮。然后我们可以看到正确的单选按钮分组。

![](http://www.tkinterdesigner.com/ReadMeImages/19.png)

​	一个界面中可以有许多单选按钮。其中一些可能是一种选择，如性别，一些是另一种选择，如生活在城市的几个地区。这两部分需要分为两组，并且需要通过每组中的唯一值来区分。因此，当代表“男性”和“女性”的两个单选按钮使用默认组号1时，您只需要将对应于“女性”的单选按钮的值更改为2。

​    接下来，我们为输入添加职业选项。选择Combobox，在其属性框中找到“Items”，在数据项编辑区弹出的对话框中双击编辑Combobox对应的数据项。

​    例如，我们输入三个数据，即“程序员”、“计划员”、“设计师”，然后单击“确定”，我们可以看到组合框变成了所需的形状。

![](http://www.tkinterdesigner.com/ReadMeImages/20.png)

单击“确定”后，最终结果如下：

![](http://www.tkinterdesigner.com/ReadMeImages/21.png)

​	好的，现在我们已经完成了所需控件的创建与摆放，所有的控件都是通过这样拖拽的方式创建到界面中的，如果你觉得这些控件在右上角树中的名字不太好记，你可以双击控件树项，在弹出的修改名称的对话框中进行修改，你也可以在属性框中通过双击"名称"属性栏来进行修改或对树项用鼠标右键，在弹出菜单里找到"修改"名称菜单项来进行修改。

![](http://www.tkinterdesigner.com/ReadMeImages/87.png)

​	这样就完成了名称的修改。

![](http://www.tkinterdesigner.com/ReadMeImages/88.png)

​	**不过要注意的是：在TKinterDesigner中，这个新修改的名称，是原始名称的别名，在后面的函数中，你即可以输入原始名称，也可以用别名来查找控件或设置变量，但为了好记，优先使用自定义的别名。Form_1作为窗体根结点，不支持修改别名。**

​	比如，你可以用`Fun.GetElement(className,‘AccountEntry’)`  获取它，也可以用`Fun.GetElement(className,‘Entry_3’)`  获取它，我们优先以别名作为搜索关键字。

​	下面我们来说一下如何为窗口增加图标和菜单，关于窗口的设置，基本都在Form_1中，我们需要先需中“Form_1", 然后双击属性框的”程序图标“项的值处，这时会弹出一个查找图标的对话框，我们选择一个图标后，会发现窗口中的图标变为了对应的图标，这样就完成了图标的设置。

![](http://www.tkinterdesigner.com/ReadMeImages/89.png)

​	要为一个界面增加菜单，然后双击属性框的”菜单“项的空值处，这时会弹出一个菜单编辑区的对话框,然后双击属性框的”菜单“项的空值处，这时会弹出一个菜单编辑区的对话框。

![](http://www.tkinterdesigner.com/ReadMeImages/90.png)

​	我们可以在这个菜单编辑区的对话框里进行菜单的编辑，首先是增加顶层菜单项，然后是选中列表框中菜单项的值，为其再次增加子菜单项或子分隔线。

![](http://www.tkinterdesigner.com/ReadMeImages/91.png)

​    在这个过程中，菜单也被实时的增加到菜单编辑区的对话框里来进行预览，调整好后，在实际运行时就可以看到效果了。

![](http://www.tkinterdesigner.com/ReadMeImages/92.png)

​	但怎么响应呢？如果你一旦确定使用菜单，则在界面对应的CMD.py文件中，会产生对应的菜单项响应函数，你在函数中进行代码编辑即可。

​    ![](http://www.tkinterdesigner.com/ReadMeImages/93.png)

单击“运行”键，将自动保存设计和代码，并运行显示结果。

![](http://www.tkinterdesigner.com/ReadMeImages/94.png)

下面我们来介绍一下控件的属性。

### 4. 控件设置

​	目前的控件工具条中，我们分为两部分:

​	第一部分是控件，主要是界面上的常用控件。第二部分是模块，主要是我们自已开发的扩展控件或者一些功能模块插件。

![](http://www.tkinterdesigner.com/ReadMeImages/95.png)

​	在控件这一页中，我们总共列罗了18种控件，这个数量不算太全，但是基本涵盖了TKinter常用的控件，后续我们会继续跟进和开发新的控件加入进来。我们点击界面上的控件，可以在右边的属性栏面板中看到一定数量的属性值可以设置，包括了以下一些方面：



**Form属性：**

- w,h:窗口大小

- 背景: 背景颜色，双击可弹出颜色选择对话框。

- 图片: 背景图，双击可弹出选择图片对话框。

- 标题:窗口的标题文字。

- 程序图标:程序的图标。

- 有标题栏:窗口是否显示标题栏。

- 可调整大小:窗口是否可以通过边缘调整大小。

- 拖拽边框宽度:如果在无标题栏的情况下，自生成的拖拽边框的宽度。

- 拖拽边框颜色：如果在无标题栏的情况下，自生成的拖拽边框的颜色。

- 主题样式：是否使用主题皮肤。

- 如终居前：窗口是否始终居前。

- 透明色值: 如果要做透明窗体，所对应的窗口镂空颜色。

- 圆角半径：边缘是否做圆角形态，如果设置了半径值，在运行时，将会在边角处以半径值形成圆角。

  ![](http://www.tkinterdesigner.com/ReadMeImages/101.png)

**Label属性：**

- 名称:控件名称
- 布局:用于设置控件布局，可以选择pack,grid,place三种布局模式。
- x,y,w,h:place模式中的位置和宽高。
- 背景:背景颜色，双击可弹出颜色选择对话框。
- 文本:控件的显示文字。
- 字体:显示文字的字体，双击可弹出字体选择对话框。
- 文字色:显示文字的颜色，双击可弹出颜色选择对话框。
- 对齐:文字的对齐方式。
- 图片:可以设置的背景图，双击可弹出选择图片对话框。
- 混排:如果即有文字，又有图片的情况下，如何进行混排。
- 样式:几种边框的显示样式。
- 状态:一般有几种情况，(1)普通(2)不可用(3)只读。
- 圆角半径：边缘是否做圆角形态，如果设置了半径值，在运行时，将会在边角处以半径值形成圆角。
- ![](http://www.tkinterdesigner.com/ReadMeImages/102.png)

**Button属性：**

- 经过时字颜色：当鼠标经过时文字的颜色
- 经过时背景色：当鼠标经过时背景的颜色
- ![](http://www.tkinterdesigner.com/ReadMeImages/103.png)

**Entry属性：**

- 替代符：对于密码型Entry，可设置的类似*的替代符。
- ![](http://www.tkinterdesigner.com/ReadMeImages/104.png)

**Text属性：**

- 滚动条：是否需要设置滚动条。

- ![](http://www.tkinterdesigner.com/ReadMeImages/105.png)

  

**ListBox属性：**

- 选择模式：几种常见的ListBox选择模式，"browse"（单选）、"multiple"（多选）和 "extended"（也是多选，但需要同时按住 Shift 键或 Ctrl 键或拖拽鼠标实现）
- 数据项：列表框中的文字项。
- ![](http://www.tkinterdesigner.com/ReadMeImages/106.png)

**Combobx属性：**

- ![](http://www.tkinterdesigner.com/ReadMeImages/107.png)

​	

**RadioButton属性：**

- 分组：所属的分组ID。
- 值：当前选中时反馈的值。
- ![](http://www.tkinterdesigner.com/ReadMeImages/108.png)

**Text属性：**

- ![](http://www.tkinterdesigner.com/ReadMeImages/109.png)

  

**LabelFrame属性：**

- ![](http://www.tkinterdesigner.com/ReadMeImages/110.png)



**Frame属性：**

- 导入界面:用于嵌入其它界面的入口，双击选择其它界面Py文件，即可嵌入到当前Frame中。
- ![](http://www.tkinterdesigner.com/ReadMeImages/111.png)

**Scale属性：**

- 方向:可选横向还是竖向。
- 显示数：是否显示当前调整的数值。
- 起始值,结束值:可调整的数值区间。
- 粒度:显示刻度的间隔。
- 刻度:调整的最小单位。
- ![](http://www.tkinterdesigner.com/ReadMeImages/112.png)



**Progress属性：**

- 最大值：进度条的区间最大数值。
- 当前值:进度条的当前进度数值。
- ![](http://www.tkinterdesigner.com/ReadMeImages/113.png)



**SpinBox属性：**

- 起始值、结束值：可调整的区间。

- 步长：每次调整的数值变化。

- 数据项：如果你想自定义SpinBox的区间值，可以直接在这里去编辑一个数据列表，作为SpinBox的数值项。

- ![](http://www.tkinterdesigner.com/ReadMeImages/115.png)

  

**TreeView属性：**

- 显示类型，默认为tree,你也可以选择“headings"，这样它将变成数据列表的形式，就类似属性面板的样子。
- 选择模式：参考ListBox选择模式
- 列数据，如果你选择了"headings"，你可以在这里为它编辑列项。
- ![](http://www.tkinterdesigner.com/ReadMeImages/116.png)
- ![](http://www.tkinterdesigner.com/ReadMeImages/117.png)
- ![](http://www.tkinterdesigner.com/ReadMeImages/118.png)
- 

**Canvas属性：**

- 在Canvas拖动到设计区时，在底部会有一栏绘图用的工具条，包括清空，画笔，直线，箭头，短形，圆形，五角形，文字，橡皮擦等，选择相应图标后，就可以在Canvas上随意做画了。
- ![](http://www.tkinterdesigner.com/ReadMeImages/119.png)



**NoteBook属性：**

- 页面：用于为当前NoteBook的创建各个页面，并导入要嵌入的窗口。
- ![](http://www.tkinterdesigner.com/ReadMeImages/120.png)



**PanedWindow属性：**

- 能被拖动:分割条是否能被拖动，决定了两部分的大小是否能改变。
- 左边界面:双击可导入左边嵌入的界面Py文件。
- 右边界面:双击可导入右边嵌入的界面Py文件。

![](http://www.tkinterdesigner.com/ReadMeImages/121.png)



**Calendar属性：**

- 栏背景与栏前景：上面的星期日到星期六一栏的背景色与文字色，对应下图中黑色背景和白色文字。
- 选中背景与选中前景：在日历控件中用鼠标选中一个日期时的改变，对应下图中的2021年7月3日位置的浅绿色背景与深绿色文字。
- ![](http://www.tkinterdesigner.com/ReadMeImages/122.png)



​	   这些是基本的控件的所有属性，如果你有问题，请给我发邮件:285421210@qq.com 或访问 :www.tkinterdesigner.com 进行反馈.

​	   除此之外，对应模块工具条有两个内置的功能模块，我们也简单说一下它们的属性，创建模块和设置属性的方式与控件拖入界面中一样。

**DataSource属性：**这是一个用于从各类数据源获取数据的模块。

- 数据类型：它有一个列表，展示了所有可以获取的数据源，你只要按上面的选择，然后就会出现相应的数据源属性。
- ![](http://www.tkinterdesigner.com/ReadMeImages/123.png)

比如这里选择TXT。

![](http://www.tkinterdesigner.com/ReadMeImages/124.png)

点击”运行“即可看到TXT文件的内容被输出显示到了TXT控件中。

![](http://www.tkinterdesigner.com/ReadMeImages/125.png)



**VideoCapture属性：**这是一个用于从摄像头获取视频并输出到Canvas上的控件。

- Canvas：输出到指定的Canvas控件，你要从右上面的控件树项中找一个合适的Canvas拖动到这里来指定。
- ![](http://www.tkinterdesigner.com/ReadMeImages/126.png)

好了，大功告成，你只需要点击”运行“，就可以看到效果了。

​	![](http://www.tkinterdesigner.com/ReadMeImages/127.png)

​	这才是我想做的，拖拖拽拽就快速化的实现界面和功能。

### 5.变量绑定

​	在开发过程中，我们经常需要存储一些数据，也许只是简单的结果存储，也许是控件的输入值。例如，在实例项目JSQ（Calculator的意思）的开发中，我们绑定了一个临时变量来存储显示数据的标签的中间值，以便进行加、减、乘、除操作。在上面的例子中，假设当我们点击“确定”来判断账户值与上次输入的值相同时，会弹出一个对话框提示“账户已使用”。我们可以添加一个自定义变量来绑定帐户。这个设计思路是对VC++的一个参考，如果你有VC++开发经验，相信可以很快理解。

![](http://www.tkinterdesigner.com/ReadMeImages/23.png)

​	右键点击账户对应的输入框，在弹出菜单中点击“变量绑定”。在弹出的对话框中，我们输入要绑定的数据项的名称“NameArray”，并选择它作为“List”类型。如果我们使用数字类型或字符串类型，我们可以看到一个选项框“映射到'文本'”，点击此选项意味着变量将更新为标签或条目控件的文本，同时函数将被激活。调用Fun.SetUserData进行设置。同一控件只允许有一个变量。如果未选择此项，则可以为控件创建多个变量。我们不需要点击这里。

![](http://www.tkinterdesigner.com/ReadMeImages/24.png)



​	创建之后，在输入框中将有一个绑定列表变量。你可以用`Fun.GetUserData(className,‘Entry_3’,’NameArray’)`  获取它。
​    接下来，让我们在单击“OK”按钮时做出相关判断，这需要为“OK”按钮添加命令事件映射。

### 6. 事件函数映射

所谓“事件函数映射”，就是对可以绑定到控制的事件进行函数映射，这样当触发相应的事件时，调用set函数。
我们右键单击“OK”按钮，然后在弹出菜单中选择“事件响应”。

![](http://www.tkinterdesigner.com/ReadMeImages/25.png)

在弹出的事件响应处理编辑区域中，我们可以看到左侧的事件列表，其中列出了常见的Python事件。右边有一个输入框，显示默认函数名。我们也可以修改它。点击“编辑功能代码”或在列表中直接双击事件项，直接进入逻辑文件的代码编辑区。此时，我们可以看到添加的事件响应函数，在这里我们可以手动编辑代码。

![](http://www.tkinterdesigner.com/ReadMeImages/26.png)

对于按钮控件，我们也可以像VC++一样直接在设计时双击控件即可进入对应的onCommand函数。

![](http://www.tkinterdesigner.com/ReadMeImages/27.png)

如果我们想在事件响应中调用其他界面，我们也可以点击“调用其他界面”按钮，然后弹出一个选项对话框，让我们根据需要调用。

![](http://www.tkinterdesigner.com/ReadMeImages/28.png)


这里可以直接选择最常用的打开和保存文件框，但是如果您创建了一个多窗口程序，您需要在这里调用另一个窗口，只需选择“调用自定义接口”就可以找到要调用的py文件。我在示例项目中有一个“calltest”项目来演示这一点。

### 7. 逻辑代码编写

按钮在逻辑文件的代码编辑区，在“Button\u 6\u oncommand”函数中，我们可以编写以下代码：

![](http://www.tkinterdesigner.com/ReadMeImages/29.png)

此代码通过“Fun.GetUserData”获取绑定到输入框的列表变量，并通过“Fun.GetText”直接获取当前输入值，然后进行比较。如果相同，将弹出“名称已注册”对话框。如果它们不同，输入值将添加到列表变量中，并弹出“注册成功”对话框。

### 8. 调试及运行

如果您想立即运行，可以直接点击右上角的“运行”按钮。程序代码将自动保存，并开始运行。如果代码中有错误，则将显示在代码区域的编译错误信息输出窗口中。如果将打印添加到该功能中，则也会实时显示打印。

![](http://www.tkinterdesigner.com/ReadMeImages/30.png)

我们在运行程序的帐户中输入名称，第一次单击“确定”时，会弹出“注册成功”对话框。然后再次点击OK，弹出“姓名已注册”对话框。
我们仍然可以通过改名成功注册。似乎一切都和我们预期的一样。

![](http://www.tkinterdesigner.com/ReadMeImages/31.png)

如果我们想要调试，可以用鼠标在代码区行号条左边点击，为程序增加断点。

![](http://www.tkinterdesigner.com/ReadMeImages/32.png)

​	增加好断点之后，即可点击下方调试区的蓝色小按钮启动调试。

​	![](http://www.tkinterdesigner.com/ReadMeImages/33.png)

​	在上面的截图中，我们可以看到，一旦启动Debug，在点击了”确定“按钮后，在Button_6_onCommand中触发了断点，并出现当前执行行的箭头，同时在下面的调试面板中，有两块区域信息显示，左边是局部变量区域，在这里可以看到当前函数已经有值的局部变量。右边是输出的DEBUG信息。

​	这时，我们可以通过点击Debug按钮栏的快捷按钮进行调试，具体使用说明如下：

​	![](http://www.tkinterdesigner.com/ReadMeImages/34.png)

​    如果你有VC++或其它编程IDE的调试经验，相信应该清楚如何使用，在这里也有一个小提示：你可在当前窗口使用如下快捷键来进行快速命令：

​	1.F5:继续执行，直至下一断点，在断点或逐行调试时你直接点蓝色箭头也是如此。

​    2.F9键：为当前行增加一个断点。

​    3.F10键：执行下一行（如果有函数，不进入函数）

​    4.F11键，执行下一行，如果有函数，进入函数。

### 9. 打包EXE

在完成我们自己的程序后，我们希望将程序打包为EXE并发布给用户。我们可以直接点击右上角的“发布”按钮，选择输出目录，然后输入要打包的EXE的名称。不过如果你未登录，是不能打包的。

​	![](http://www.tkinterdesigner.com/ReadMeImages/36.png)

单击“确定”按钮，tkinterdesigner将开始调用打包程序来打包项目。

​	![](http://www.tkinterdesigner.com/ReadMeImages/37.png)

如果进展顺利，您最终可以在输出目录中找到相应的exe程序：

​	![](http://www.tkinterdesigner.com/ReadMeImages/38.png)

### 10. 自定义模块导入

​	自定义模块是为了让开发者通过自编写的模块类与控件进行交互，完成相对独立的功能，您可以在界面设计器中将模块类导入，并轻松的设置模块类的属性，包括将接口控件作为参数传递给它。我们希望将来提供大量的可用模块给开发者使用，目前我们在”组件市场“提供了少许模块来验证这个方案，但前提是您得是注册账号才可以看到组件市场。

![](http://www.tkinterdesigner.com/ReadMeImages/39.png)

​	在”组件市场“面板里，我们可以看到Express 快递查询的组件，我们可以点击安装，安装成后后，它会被放置在当前工具目录的Market_com目录中。

它的代码如下：

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
    #设置公司的索引
    def set_CompanyID(self,companyID):
        self.CompanyID = companyID
    #取得公司的索引
    def get_CompanyID(self):
        return self.CompanyID
    #设置物流单号
    def set_ExpressNumber(self,expressNumber):
        self.ExpressNumber = expressNumber
    #取得物流单号
    def get_ExpressNumber(self):
        return self.ExpressNumber   
    #设置获取公司索引的ComboBox
    def set_ComboBox(self,comboBox):
        self.ComboBox = comboBox
        # These are some express company 's name in China.
        self.ComboBox['values'] = ['申通快递','EMS邮政','圆通快递','顺丰快递','韵达快递','中通快递','天天快递','德邦快递']
        self.ComboBox.current(4)
    #取得获取公司索引的ComboBox
    def get_ComboBox(self,comboBox):
        return self.ComboBox   
    #调用查询
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

​	我们可以看到，编写自定义模块类的方法为：创建一个类，并为需要暴露在设计器可访问的属性加入set和get函数。在Express类中我们设计了三个变量的函数，包括快递公司的公司ID、快递编号，我们希望传入一个控件组合框来接受公司名称列表。

​	现在我们创建一个空白项目，然后我们在左边Project2树项上用鼠标右键单击，在弹出菜单里选择”导入资源“，将Market_com中的Express.py导入进来。

![](http://www.tkinterdesigner.com/ReadMeImages/40.png)

在主界面设计区域，我们通过控件拖拽快速构建界面：

![](http://www.tkinterdesigner.com/ReadMeImages/41.png)

​	现在我们已经完成了界面的设计，我们将切换到工具栏的“模块”页面。在“模块”页面中，我们单击“import module”按钮，然后找到“Express”。点击“打开”。实际上，“Express.py”不必在当前目录中。您可以将一个模块用于多个项目，只需在此处导入，而不需要为用于同一模块的每个项目创建模块类文件。

![](http://www.tkinterdesigner.com/ReadMeImages/42.png)

好的，现在express模块项出现在模块面板上，让我们把它拖到界面上。

![](http://www.tkinterdesigner.com/ReadMeImages/43.png)

​	我们可以看到，在右下角的属性框中，express模块的三个变量显示在属性框中。我们可以手动设置“CompanyID”和“ExpressNumber”，但是如何设置ComboBox呢？在这里，您只需要在右上角的控件树中找到相应的ComboBox，然后拖动到属性框中“combobox”的值项位置。然后我们将命令响应函数添加到“query”按钮。

![](http://www.tkinterdesigner.com/ReadMeImages/46.png)

在“Button_7_oncommand”函数中，我们可以编写相应的代码：

![](http://www.tkinterdesigner.com/ReadMeImages/47.png)


​    

这部分代码实现了从Entry_5获取查询物流单号，并通过我们的模块名称“Express_9”调用'Fun.GetElement'来获取Express模块，并使用相同的方法来获取Listbox，然后调用Express的函数`set_ExpressNumber`设置快递号，最后调用查询方法进行查询。参数是显示的ListBox对象。
     完成后，点击右上角”Run"运行它。我们可以看到正在运行的程序。尝试在快递订单号中输入号码后，点击“查询”，很快就会看到列表框中显示的快递信息。

![](http://www.tkinterdesigner.com/ReadMeImages/48.png)

​	这就是在设计区加入自己编写的模块并调用的实例，如果你觉得代码写起来麻烦，也可以直接查看案例工程中的快递查询案例进行学习。

![](http://www.tkinterdesigner.com/ReadMeImages/45.png)



## 关于美化：应用皮肤及自定义控件样式。

​	 大多数情况下，我们使用TKinter去创建的程序并不够美观，虽然不影响功能开发，但是爱美之心，人皆有之。如果能让程序变的美观一些是最好，不过鉴于我们的开发者用户大多数是程序员，对于美化的部分，能简单化是最好，因此我希望通过提供好的配色方案作为皮肤提供给开发者使用，使程序变的美丽，因此我们也推出了皮肤市场，暂时只有官方皮肤，后面将放开给广大开发者用户上传提交以提供更好的皮肤给大家。但前提是您得是注册账号才可以看到组件市场。

![](http://www.tkinterdesigner.com/ReadMeImages/75.png)

​	我们可以在这里点击"黑金主题"图标上的”未安装"文字完成安装。

​	然后我们尝试着打开实例项目"计算器"，我们可以在Form_1的属性栏里找到"主题样式"，点击下拉列表，这时我们可以看到一个”BlackGold.py"，这就是黑金皮肤了。

![](http://www.tkinterdesigner.com/ReadMeImages/76.png)

​	我们选择它，并运行程序。你将看到一个酷酷的计算器程序，它有着深灰色的背景和暗金色的文字以及对比度明显的边缘。

![](http://www.tkinterdesigner.com/ReadMeImages/77.png)

​	当然，如果你想自已去修改自已的样式，也可以在sty.py中制作，比如我们再次打开之前创建的那个注册小程序项目。

![](http://www.tkinterdesigner.com/ReadMeImages/78.png)

​	点击左边的“Project1_sty.py"，进入到样式编辑器里。

![](http://www.tkinterdesigner.com/ReadMeImages/79.png)

​	在这个界面里，我们在样式名称里输入My，并在对应控件列表里选择”TForm“，点击”新增样式“按钮。

![](http://www.tkinterdesigner.com/ReadMeImages/84.png)

​	在这个界面里，我们在样式名称里输入My，并在对应控件列表里选择”TEntry“，点击”新增样式“按钮，并为两个关键值"background"和"foreground"设置颜色。

![](http://www.tkinterdesigner.com/ReadMeImages/85.png)

   同样的方式，我们建立其它控件的样式。

​	![](http://www.tkinterdesigner.com/ReadMeImages/86.png)

​	完成后，我们可以回到设计区，并在对话框，编辑框，单选按钮和组合框上进行鼠标右键单击，这时的弹出菜单里，会有一个”样式选择“项，我们选择对应的样式即可。

​	![](http://www.tkinterdesigner.com/ReadMeImages/82.png)

​	为所有的控件设置好样式后，它就变成了这样。

![](http://www.tkinterdesigner.com/ReadMeImages/83.png)

​	

### 关于我

网名: honghaier
国籍: China
技能: C + +, game development
自我评估: 程序员，开发者，创业者

### 感言：

​		能看到这里，相信读者也已经很辛苦了，在编写教程的过程中，我仍然在继续改BUG，可能部分截图会与实际版本略有出入，但大体相符。我希望有兴趣的Python爱好者能和我交流，给我更多的建议，希望Python能越来越好。
​		最后，祝大家工作顺利，身体健康~

​                                                                                                           Honghaier

​																											2021/07/07

