

# **PyMe****一站式开发工具 介绍手册**
#* * PyMe * * One Stop Development Tool Introduction Manual**
​            

​	               																			版本: v 1.1
																					Version: v 1.1

​	               																			作者: 火云红孩儿
																					Author: Honghaier

 

| 开发者   | Honghaier        |
| -------- | ---------------- |
| 版本号   | V1.4.0.3         |
| 更新日期 | 2024-03-12       |
| 官方QQ群 | 100180960        |
| 官方邮件 | 285421210@qq.com |

 

 

# **PyMe是什么？**
#What is PyMe**
## **“写在前面的一点感悟”：**
##"A little insight written at the beginning":**
 

​	朋友，你好，我是PyMe的作者火云红孩儿，一位热爱编程的程序员，在开始介绍这个项目前前，我想先讲一点我对于Python和PyMe的看法，或许不正确，或许脑洞有点大，但我觉得有必要讲出来，这样才能得到各位专家和开发者的指正。  

        Hello friend, I am Huoyun Honghaier, the author of PyMe and a programmer who loves programming. Before introducing this project, I would like to share some of my views on Python and PyMe. Perhaps it is incorrect or my imagination is a bit broad, but I think it is necessary to speak up so that I can receive guidance from experts and developers.

​	这个项目是在四年前开始的，当时我关注到Python连续占据最受欢迎的编程语言榜首，所以我计划系统的学习一下Python，在此之前我有十五年以上的C++游戏开发经验，因为我从事的是游戏引擎和工具链的开发工作，所以我对于工具软件尤为重视，在学习Python的过程中，我有一种强烈的感觉：“Python的工具链薄弱程度与Python语言的受欢迎程度不匹配”。在2023年的今天，开发工具市场的产品已经发展的越来越强大，越来越人性化。而Python作为当今耀眼的明星，居然没有一款可视化、流程化、人性化的开发工具。  

        This project started four years ago, when I noticed that Python had consistently ranked first among the most popular programming languages. Therefore, I planned to systematically study Python. Prior to this, I had more than fifteen years of experience in C++game development. As I worked in the development of game engines and toolchains, I attached great importance to tool software. In the process of learning Python, I have a strong feeling that the weakness of Python's toolchain does not match the popularity of the Python language. Today in 2023, the products in the development tool market have become increasingly powerful and user-friendly. As a dazzling star today, Python surprisingly lacks a visual, procedural, and user-friendly development tool.

​	所以，我尝试着自已做，并逐步使它成为一个独立的技术创业项目。

        So, I tried to do it myself and gradually make it an independent technology entrepreneurship project.

***\*最初\****，我只是尝试着写一个简单的界面编辑器，它基于tkinter，提供简单的控件拖拽设计和代码生成，可以直接运行，并通过pyinstaller打包成EXE。我将它命名为“TkinterDesigner”，并在github上提交了可执行程序，很快，就有人关注，并成为了第一批用户。于是，我利用工作之余，不断的完善它，加入了变量绑定、事件响应函数映射与代码编辑，并加入了一些预设的工程案例模版，使它看起来像VisualBasic一样简单而易用。  

***\*At first\****, I was just trying to write a simple interface editor based on tkiner, which provides simple control drag and drop design and code generation, can be run directly, and packaged into EXE through pyinstaller. I named it "TkinterDesigner" and submitted an executable program on GitHub. Soon, someone followed and became one of the first users. So, in my spare time, I constantly improved it by adding variable binding, event response function mapping, and code editing, as well as adding some preset engineering case templates, making it look simple and user-friendly like Visual Basic.

***\*很快，\****“TkinterDsigner”成长为一个可视化的桌面应用开发工具，在这个过程中，我熟练的掌握了Python的编程，但我并没有打算结束它，而是有了一些更大的想法。  

***\*Quickly\****, "TkinterDsigner" grew into a visual desktop application development tool. During this process, I became proficient in Python programming, but I had no intention of ending it. Instead, I had some bigger ideas.
 

​	因为我逐渐的认知到，随着Python语言在全世界的广泛学习和应用，***\*未来Python有机会成为像英语一样的通用语言！\****  

        Because I gradually realized that with the widespread learning and application of Python language around the world, there is a chance for Python to become a universal language like English in the future\****
​	我意识到：随着网络和科技的不断发展，人的价值，会越来越回归到数字化的体现，即：  

        I realize that with the continuous development of the internet and technology, human value will increasingly return to the manifestation of digitization, namely:
 

***\*人的价值 = 积累的经验素材 + 处理事情的方法 = 数据 + 算法\****
***\*Human value=accumulated experience materials+methods of handling things=data+algorithms\****
 

***\*比如：\****
***\*For example:\****
​	厨师的价值 = 能做的菜品的数量（***\*数据）\**** +  对菜品做法的追求（***\*算法）\****
        The value of a chef=the quantity of dishes that can be cooked (* * * \ * data) \ * * *+the pursuit of dish preparation (* * * \ * algorithm)\****
​	能做的菜品的数量 = 做的菜品越多，对各种菜品背后的食材，营养搭配，配料，炊具，火候，味觉感受，视觉感受的熟悉和归纳越丰富。
        The number of dishes one can cook=the more dishes one can cook, the richer the familiarity and induction of the ingredients, nutritional combinations, ingredients, cooking utensils, heat, taste perception, and visual perception behind various dishes.
​	对菜品做法的追求 = 对食材、烹饪的关系越了解，越能够在最恰当的情况下选择最恰当的烹饪方式和流程，能给与食客最满意的结果。
        The pursuit of dish preparation means that the more you understand the relationship between ingredients and cooking, the more you can choose the most appropriate cooking method and process in the most appropriate situation, and give diners the most satisfactory results.
 

***\*再比如：\****
***\*For example:\****
​	律师的价值 = 案件经手的数量（***\*数据）\**** +  处理案件的方法（***\*算法）\****
        The value of a lawyer=the number of cases handled (* * * \ * data)+the method of handling the case (* * * \ * algorithm)\****
​	案件经手的数量 = 做的案件越多，数据越多，律师对对法律在实际适用情况越熟悉，案件越有把握和信心。
        The number of cases handled=the more cases and data done, the more familiar the lawyer is with the actual application of the law, and the more confident and confident the case is.
​	处理案件的方法 = 对当事人线索调查方法越熟悉，越能够找到突破口。
        The method of handling a case=the more familiar the investigation method of the parties involved, the more able they are to find a breakthrough point.
​	虽然我不是厨师，更不是律师，但本质上，各行各业的人，都一样。我们的人生价值，都是在积累数据和改善方法。而我们的薪水，本质上反映的是我们对于“工作数据的丰富和深度 + 处理方法的熟练和恰当”。
        Although I am not a chef, let alone a lawyer, fundamentally, people from all walks of life are the same. Our life value is all about accumulating data and improving methods. And our salary essentially reflects our proficiency and appropriateness in the richness and depth of work data and processing methods.
​	人的价值，其实可以被提炼为一段包含数据和算法的代码，但需要一个通用化的编程语言。
        The value of human beings can actually be distilled into a piece of code containing data and algorithms, but it requires a universal programming language.


***\*这门编程语言，我相信就是Python。\****
***\*I believe this programming language is Python\****
***\*为什么？\****
***\*Why\****
***\*因为它具有三个特点，是其它语言无法比拟的。\****
***\*Because it has three characteristics that cannot be compared to other languages\****


**1、*****\*语法简单，最接近自然语言，学习成本最低，可以让最多的人群了解和掌握。\****
**1. ****** \ * The grammar is simple, closest to natural language, with the lowest learning cost, and can be understood and mastered by the largest audience\****
**2、*****\*功能库安装简单，别人写的功能库快速即插即用，可以让大量的价值被方便的交换。\****
**2. ****** \ * The installation of the feature library is simple, and the feature library written by others is quickly plug and play, which can facilitate the exchange of a large amount of value\****
**3、*****\*一次编写，到处运行，不受平台的限制，使得价值可以体现在更主流的应用场景。\****
**3. ***** \ * Write once, run everywhere, not limited by the platform, allowing value to be reflected in more mainstream application scenarios\****
 

​	而要想实现这个目标，还需要完成三件事：***\*更广泛的应用领域、统一的开发流程\****和***\*交换的平台\****。
        To achieve this goal, three more things need to be accomplished: a wider range of application areas, a unified development process, and a platform for exchange.
**1、*****\*更广泛的应用领域\****
**1. ****** \ * Wider application areas\****
​	目前Python语言在许多方面取得了令人瞩目的成绩，但在拥有最广泛开发者的桌面应用开发、移动应用开发、游戏开发、嵌入式等方面，还裹足不前。许多开发者告诉我，这不是Python擅长的事情，但如果Python要成为最通用的代码交换手段，必须保证Python在这些大的方向和领域占据主流开发语言的地位。
        At present, Python language has achieved remarkable results in many aspects, but it still lags behind in areas such as desktop application development, mobile application development, game development, and embedded development, which have the widest range of developers. Many developers have told me that this is not something Python is good at, but if Python is to become the most common code exchange tool, it must ensure that Python occupies the mainstream development language position in these major directions and fields.
**2、*****\*统一的开发流程\****
**2. ****** \ * Unified development process\****
​	目前Python语言缺乏标准化的开发流程，从而导致大家使用基于代码编辑器类开发工具（VSCode,PyCharm）写代码在风格太过于自由，流程和设计模式上太过于凌乱，有一定阅读和理解成本。我们需要一个流程，来将所有的Python开发者资源案例以一种科学而流程化的方式重新整理，才能够在未来方便的交换。
        At present, the Python language lacks a standardized development process, which leads to people using code editor based development tools (VSCode, PyCharm) to write code in a style that is too free, and the process and design patterns are too messy, resulting in a certain cost of reading and understanding. We need a process to reorganize all Python developer resource cases in a scientific and procedural manner in order to facilitate future exchanges.
 

**3、*****\*交换的平台\****
**3. ****** \ * Exchange platform\****
 

​	需要建立一个平台，将开发者的代码能够上传到平台中发布，这样才能实现价值的交换和竞争。
        We need to establish a platform where developers can upload their code for publication, in order to achieve value exchange and competition.
 

​	于是，《PyMe》诞生了。它不仅是一个拥有界面设计器的Python代码编辑工具，更在下面三个事情上立下目标：
        So, PyMe was born. It is not only a Python code editing tool with an interface designer, but also sets goals for the following three things:
1、推动Python的桌面应用开发，移动应用开发和游戏开发，PyMe内置了一键打包APK，并内置了Pygame游戏引擎和工具链，同时在建设PyOpenGL的3D游戏引擎和工具链。
1. Promoting desktop application development, mobile application development, and game development in Python, PyMe has built-in one click packaging APK and Pygame game engine and toolchain, while also building a 3D game engine and toolchain for PyOpenGL.
2、推动建立从项目搭建到界面场景设计、组件编辑、代码编写、打包发布的全套开发流程，希望通过这套流程使人类的价值成果有一个流程标准，降低其它繁琐事务对问题本质的干扰，辅助开发者对代码的理解。
2. Promote the establishment of a complete development process from project construction to interface scene design, component editing, code writing, packaging and publishing, hoping to establish a process standard for human value achievements through this process, reduce the interference of other tedious tasks on the essence of problems, and assist developers in understanding the code.
3、推动建设一个开发者平台，将标准化的案例开源代码发布到其上，促进各行各业价值的交换和竞争。
3. Promote the construction of a developer platform, publish standardized case open source code on it, and promote the exchange and competition of value across various industries.

​	截止到目前，PyMe的开发完成了其中少量的工作，以下是基本的进度情况：
        As of now, PyMe's development has completed a small amount of work, and the following is the basic progress:


(1)Python桌面应用开发  -- 60% ，基本具备了一套完整的开发流程。
(1) Python desktop application development -60%, basically equipped with a complete development process.
(2) Python移动应用打包  -- 40% ，实现了有限的一键打包APK，但不稳定。
(2) Python mobile application packaging -40%, achieving limited one click packaging APK, but unstable.
(3)Python 2D游戏开发   -- 40%，实现了大量基础的常用引擎工具。
(3) Python 2D game development -40%, implementing a large number of basic commonly used engine tools.
(4) Python 3D 游戏开发   -- 20%，实现了基础的3D引擎功能。
(4) Python 3D game development -20%, achieving basic 3D engine functionality.
 

​	《PyMe》的口号就是“我用Python创世界！”，这也是我存在的意义和目标，我希望每个Python开发者，都能使用《PyMe》创造出自已心中美好的世界。
         The slogan of PyMe is "I create the world with Python!", which is also the meaning and goal of my existence. I hope that every Python developer can use PyMe to create a beautiful world from their own hearts.
## **“说人话”：**
##* * "Talking to People":**
​	你是否想学习Python，却找不到好的学习路径？
        Do you want to learn Python, but cannot find a good learning path?
​	你是否掌握了Python语言，但却连最简单的界面都难以实现？
        Have you mastered the Python language, but find it difficult to implement even the simplest interface?
​	你是否想要使用Python开发游戏，甚至是可以运行在手机上的3D游戏？
        Do you want to develop games using Python, or even 3D games that can run on your phone?
 

***\*如果答案是Yes，你需要了解这个项目： 《PyMe》\****
***\*If the answer is Yes, you need to understand this project: PyMe\****
​	长期以来，Python开发者往往会陷入到一种迷茫中，经过一段时间的Python学习，似乎学会了，掌握了一个个知识点和小案例，但	却越来越失去方向。这是为什么呢？
        For a long time, Python developers have often fallen into a state of confusion. After a period of Python learning, they seem to have learned and mastered various knowledge points and small cases, but they are increasingly losing direction. Why is this?
 

***\*因为Python缺乏体系化的编程工具！\****
***\*Because Python lacks systematic programming tools\****
​	对于绝大部分开发者来说，编程学习需要语言学习和实践练习才能深入掌握。
        For the vast majority of developers, programming learning requires language learning and practical practice to gain a deeper understanding.
​	所谓实践练习，就是应用场景，这其中IDE功不可没。
        The so-called practical exercises refer to application scenarios, in which IDE plays an indispensable role.
 

​	***\*VB，XCode，VC++，Escplise\****等知名IDE，不仅仅提供代码的编写，更是一个集成化，图形化，流程化的软件工程实践工具。他们保证了开发者可以在一个易懂的、可视化的、工程化的开发流程中逐渐沉淀经验，并得到良好的正向反馈。
        ***\*Famous IDEs such as VB, XCode, VC++, Escplise, etc\****. not only provide code writing, but also serve as integrated, graphical, and procedural software engineering practice tools. They ensure that developers can gradually accumulate experience and receive positive feedback in an easy to understand, visual, and engineering development process.

​	IDE中“项目的搭建，多文件的组织关系，可视化的界面设计，界面与逻辑的绑定关系，界面与数据的绑定关系，项目的调试与运行，打包与输出。”等功能从零散的具体功能，有机的组合成一个流畅的开发流程，这套工作流是实践练习的基础，也是承载了具体工作产业化的基础。
        The functions of "project construction, multi file organization, visual interface design, interface logic binding, interface data binding, project debugging and operation, packaging and output" in IDE are organically combined from scattered specific functions into a smooth development process. This workflow is the foundation of practical practice and also carries the foundation of industrialization of specific work.

​	不巧的是，***\*Python没有这样的开发流程，\****大多数人只能选择Pycharm，VScode两款工具软件进行开发。而这两款工具并没有完整的开发流程，严重依赖程序员自己来建立开发流程。而开发流程的建立，则需要多年的经验。这也导致了许许多多Python初学者，只会基于Python零散的大量的知识点，在控制台模式下写写爬虫，数据处理，AI训练，量化脚本等脚本，而无法完成一个完整的软件。
        Unfortunately, ***\*PythonPython does not have such a development process\****, and most people can only choose Python and VScode tools for development. However, these two tools do not have a complete development process and heavily rely on programmers to establish their own development process. The establishment of development processes requires years of experience. This has also led to many Python beginners only being able to write web crawlers, data processing, AI training, quantification scripts, and other scripts in console mode based on a large amount of scattered knowledge points in Python, and unable to complete a complete software.
​	如果你想改变这种状况，那么你需要一款提供完整工作流的开发工具。
        If you want to change this situation, then you need a development tool that provides a complete workflow.
 

***\*《PyMe》\****就是为此而生。
***\*PyMe\**** was born for this.
 

以下是《PyMe》的基本定义：
The following is the basic definition of PyMe:
 

***\*《PyMe》\*******\*是一款基于\**** ***\*Python\**** ***\*的流程化的项目开发工具软件\*******\*，主要用于流程化、可视化、组件化的设计与开发应用和游戏项目。\****
***\*PyMe\*******\* is a process oriented project development tool software \**** ***\*based on Python\**** ***\*. It is mainly used for process oriented, visual, and component-based design and development of applications and game projects\****
 

# **PyMe都有什么功能？**
# **What are the functions of PyMe**
***\*PyMe\**** 的功能分为两部分：***\*开发功能\****和***\*平台功能\****。
The functions of ***\*PyMe\****  are divided into two parts: development functions and platform functions.
#### 一、**开发功能** 
####1、 * * Development features**
​	PyMe中的开发功能分为应用开发和游戏开发两部分，其中应用开发主要包括以下十项基本功能:
        The development functions in PyMe are divided into two parts: application development and game development. Application development mainly includes the following ten basic functions:
**1.** ***\*项目管理\****:通过预设的模版工程进行项目的创建与打开。
**1.** ***\*Project Management\****: Create and open projects through preset template engineering.
**2.** ***\*文件管理\****:对于项目进行窗体，文件的创建和资源的导入。
**2.** ***\*File Management\****: Create forms, files, and import resources for projects.
**3.** ***\*界面设计\****:通过拖拽式的操作快速的制作界面。
**3.** ***\*Interface Design\****: Quickly create an interface through drag and drop operations.
**4.** ***\*控件设置\****:对控件进行常用的属性编辑。
**4.** ***\*Control Settings\****: Perform common property editing on controls.
**5.** ***\*变量绑定\****:对控件进行用户变量的创建与编辑。
**5.** ***\*Variable Binding\****: Create and edit user variables for the control.
**6.** ***\*事件响应\****:在控件事件与函数之间快速的建立映射函数。
**6.** ***\*Event Response\****: Quickly establish a mapping function between control events and functions.
**7.** ***\*逻辑编写\****:内置了代码编辑器，提供函数智能提示。
**7.** ***\*Logic Writing\****: Built in code editor, providing intelligent function prompts.
**8.** ***\*调试运行\****:可对工程进行调试和运行。
**8.** ***\*Debugging and Running\****: Can debug and run the project.
**9.** ***\*编译打包\****:提供一键实现打包功能，支持转c编译加密，打包APK。
**9.** ***\*Compilation and Packaging\****: Provides one click packaging function, supports C conversion, compilation, encryption, and packaging of APK..
**10.** ***\*界面美化\****:对界面进行样式设计编辑和快速应用。
**10.** ***\*Interface Beautification\****: Style design, editing, and quick application of the interface.
 

***\*游戏开发\****功能与***\*应用开发\****功能的区别在于，关注点从界面转向了游戏开发流程，***\*这部分的功能介绍将会有专门的文档进行解释说明\****，不在这里进行展开。
The difference between ***\*game development\**** and ***\*application development\**** is that the focus has shifted from the interface to the game development process.***\* There will be a dedicated document to explain and explain the features in this section\****, which will not be elaborated here.

#### 二、**平台功能** 
#### 2、**Platform features** 

***\*平台功能\****以***\*资源交换\****服务为主，致立于建设一个丰富、有价值的资源生态，主要包括以下项基本服务：
***\*The platform functions\**** mainly focus on ***\*resource exchange\**** services, aiming to build a rich and valuable resource ecosystem, including the following basic services:

**1.** ***\*案例下载\****：提供各类型的PyMe应用案例开源代码。
**1.** ***\*Case Download\****: Provide open-source code for various types of PyMe application cases.

**2.** ***\*组件下载\****：提供各种具有特定功能的组件，用于项目开发。
**2.** ***\*Component Download\****: Provides various components with specific functions for project development.

**3.** ***\*皮肤下载\****：提供各种风格的界面皮肤样式。
**3.** ***\*Skin Download\****: Provides various styles of interface skin styles.

**4.** ***\*项目外包\****：提供一些项目甲方发包信息，方便开发者接单。
**4.** ***\*Project Outsourcing\****: Provide some project contracting information from Party A to facilitate developers in accepting orders.

**5.** ***\*申请UP主\****：开发者可申请成为UP主，在开发者平台发布作品并获得有效下载收益分成。
**5.** ***\*Apply for UP Master\****: Developers can apply to become UP masters, publish their works on the developer platform, and receive effective download revenue sharing.

# **PyMe都有什么特点？**
# **What are the characteristics of PyMe**
​	PyMe的主要特点是：**可视化**、**低代码**、**跨平台**。
        The main features of PyMe are: **visualization**, **Low code**, and**Cross platform**.
#### **一、可视化：**
####1. Visualization:**

​	PyMe提供全套的可视化开发方式，从项目搭建、界面设计、控件属性、变量绑定到逻辑编写、调试运行、打包输出，可视化的编辑始终贯穿流程。这种体验类似Visual Basic，Visual C++，如果你有类似的经验，可以很快上手。
        PyMe provides a complete set of visual development methods, from project construction, interface design, control properties, variable binding to logic writing, debugging and running, packaging and output, visual editing always runs through the process. This experience is similar to Visual Basic, Visual C++, and if you have similar experience, you can get started quickly.
![img](http://www.py-me.com/mkdoc_images/wps1.jpg) 

#### **二、低代码：**
#### **2. Low code: **
​	PyMe通过可视化的方式，可以生成出项目的代码框架，并在此基础上建立简单、灵活的函数脚本编程机制，使得整个开发过程由复杂而繁琐的事情变得简单而有条理，大大降低了工作量。
        PyMe can generate the code framework of a project through visualization and establish a simple and flexible function script programming mechanism on this basis, making the entire development process simple and organized from complex and tedious tasks, greatly reducing workload.
![img](http://www.py-me.com/mkdoc_images/wps2.jpg) 

#### 三、**跨平台：**
#### 3、**Cross platform:**

​	PyMe提供多平台的编辑、运行与打包能力，可以帮助开发者在Window,Mac,Linux上建立符合自身需要的跨平台应用，更可以打包出APK和IOS移动应用和游戏。
        PyMe provides multi platform editing, running, and packaging capabilities, which can help developers build cross platform applications that meet their needs on Windows, Mac, and Linux. It can also package APK and IOS mobile applications and games.
# **PyMe面向什么用户人群？**
# **What user group does PyMe target **

PyMe的主要用户包括以下一些群体：
The main users of PyMe include the following groups:

1. Python初学者：帮助他们建立良好的开发流程和工程化的开发思想。
1. Python beginners: Help them establish good development processes and engineering development ideas.
2. 应用开发者：帮助他们可以使用PyMe快速化的进行应用软件开发。
2. Application developers: Help them develop application software quickly using PyMe.
3. 游戏爱好者：帮助非专业游戏开发者和独立制作者能够使用Python开发游戏。
3. Game enthusiasts: Help non professional game developers and independent creators to develop games using Python.
 

# **PyMe的下载、使用与教程、反馈**
# **PyMe downloads, usage, tutorials, and feedback**
​	目前我提供了三种下载方式，你可以在其中找到PyMe的文件包并下载使用。
        At present, I have provided three download methods, where you can find the PyMe file package and download it for use.
 

PyMe的官方网址：[www.py-me.com](http://www.py-me.com)
PyMe's official website: [www.py-me.com](http://www.py-me.com)
PyMe的官方Github: https://github.com/honghaier-game/PyMe
PyMe的官方QQ群共享：100180960 

## **版本说明：**
## **Version Description:**
​	目前版本只支持***\*win64\**** ，其它平台如Mac,Linux请静待我的推进，也希望您能告诉我您的需要，因为目前的主要用户群是windows开发者，所有在精力有限的情况下，以windows版本为主。
        The current version only supports***\*win64\****. For other platforms such as Mac and Linux, please wait for my progress and let me know your needs. The main user group at present is Windows developers, so with limited energy, the Windows version is the main version.
 

​	要注意的是：***\*PyMe不开源，它是一款工具产品，但PyMe中你生成的所有工程代码，包括内置的Fun函数库和游戏引擎底层源码，都是公开的。~\****
        It should be noted that ***\*PyMe is not open-source and is a tool product. However, all the engineering code generated in PyMe, including the built-in Fun library and the underlying source code of the game engine, is publicly available~\****
 

## **官方教程：**
## **Official Tutorial:**
​	目前PyMe的教程包括三方面的内容：
        At present, PyMe's tutorials include three aspects of content:
#### 1、**作者的书**
#### 1、**Author's book**
​	《Python跨平台应用软件开发实战》，机械工业出版社出版：
        《Practical Development of Python Cross Platform Application Software》, published by China Machinery Industry Press:
![img](http://www.py-me.com/mkdoc_images/wps3.jpg) 

#### 2、**B站的视频教程**
#### 2. Video tutorials for Bilibili**
​	目前的视频教程分为两部分：
        The current video tutorial is divided into two parts:
​	《PyMe基础使用入门课》 https://www.bilibili.com/video/BV1tF411d7kN
        《Introduction to PyMe Basic Usage Course》 https://www.bilibili.com/video/BV1tF411d7kN
![img](http://www.py-me.com/mkdoc_images/wps4.jpg) 

《PyMe游戏开发入门课》 https://www.bilibili.com/video/BV1N94y1r77W
《PyMe Game Development Beginner Course 》https://www.bilibili.com/video/BV1N94y1r77W
![img](http://www.py-me.com/mkdoc_images/wps5.jpg) 

​	在PyMe中，也集成了这些教程，开发者可以通过“视频教程”页面来观看。
        In PyMe, these tutorials are also integrated, and developers can watch them through the "Video Tutorial" page.
![img](http://www.py-me.com/mkdoc_images/wps6.jpg) 

#### 3、**PyMe的向导教程**
#### 3、**PyMe Wizard Tutorial**
​	PyMe中加入了一步一步渐进式的操作向导，开发者可以跟着向导教程在具体的实例练习中快速的学会整个开发过程。
        PyMe has added a step-by-step step-by-step operation guide, allowing developers to quickly learn the entire development process through specific instance exercises.
而向导教程也贯穿于两个方面：
And the guide tutorial also runs through two aspects:
***\*1.“新手入门”：\****开发者新建项目后点击顶部菜单“新手入门”菜单项，就可以选择对应的向导教程进行学习。
***\*1. "Beginner's Guide"\****: After creating a new project, developers can click on the "Beginner's Guide" menu item at the top to select the corresponding guide tutorial for learning.
![img](http://www.py-me.com/mkdoc_images/wps7.jpg) 

​	点击相应的教程向导，即可开始运行步进式的教程，只需要一步一步跟着做即可学会相应的案例开发。
        Click on the corresponding tutorial guide to start running the step-by-step tutorial. Simply follow step by step to learn the corresponding case development.
![img](http://www.py-me.com/mkdoc_images/wps8.jpg) 

​	2、***\*“模板项目”：\****新建的模版案例，会自带向导教程，双击文件与资源栏中的“向导教程”图标，即可进入向导教学。
        2. ***\"Template Project":\****新 The newly created template case will come with a wizard tutorial. Double click the "Wizard Tutorial" icon in the file and resource bar to enter the wizard tutorial.
![img](http://www.py-me.com/mkdoc_images/wps9.jpg) 

## **建议反馈：**
## **Suggested feedback:**
​	作为软件内置的一种沟通机制，在最后一页“建议反馈”里，开发者可以反馈发现的问题，建议，我在收到反馈后会进行解答和回复。
        As a communication mechanism built into the software, on the last page of "Suggestion Feedback", developers can provide feedback on discovered issues and suggestions. After receiving feedback, I will provide answers and replies.
![img](http://www.py-me.com/mkdoc_images/wps10.jpg) 

# **PyMe的角色类型**
# **PyMe's Role Types**
​	PyMe并不强制要求登录使用，但只有注册账号才能够打包软件和访问开发者平台。注册账号分为免费账号和专业开发者账号。免费账号可以进行软件打包和访问开发者平台，但目前有几个功能是提供给专业开发者账号才能使用和享有。
        PyMe does not require mandatory login for use, but only by registering an account can software be packaged and access the developer platform be accessed. Registered accounts are divided into free accounts and professional developer accounts. Free accounts can package software and access developer platforms, but currently there are several features that are only available for professional developer accounts to use and enjoy.


​	专业开发者账号所享有的这些功能包括以下几个方面：
        The features enjoyed by professional developer accounts include the following aspects:


**1、*****\*加密功能\****：帮助开发者可以将Python工程先转成C再编译成pyd文件后再进行打包，最大程度的保护源代码。
**1、*****\*Encryption Function \****: Helps developers convert Python projects into C, compile them into pyd files, and then package them, maximizing source code protection.
**2、*****\*解除水印\****：普通账号在打包时，会在界面右上角显示PyMe字样的文字，专业开发者账号可以去除。
**2、*****\*Remove Watermark \*****: When packaging a regular account, the text "PyMe" will be displayed in the upper right corner of the interface, which can be removed by professional developer accounts.
**3、*****\*窗口数量\****：普通账号在同一个项目内可以创建五个窗口数量以内（包含五个窗口），专业开发者账号不受窗口数量限制。
**3、*****\*Window Quantity\****：: A regular account can create up to five windows (including five windows) within the same project, while a professional developer account is not limited by the number of windows.
**4、*****\*原生调用\****：专业开发者将可以在移动设备上进行原生接口调用，比如相册、摄像头、蓝牙等功能。（暂时尚不完善，无法正常使用）

 

​	这些方面对于大多数开发者来说是不影响使用的，所以如果您只是做项目的开发、设计、代码编写、调试运行、非加密的打包输出，是没有问题的。

 

# **新手入门：应用软件开发快速上手**

​	千里之行，始于足下，下面我们来了解一下PyMe的简易使用，它将基于PyMe提倡的开发流程来进行讲解，我将结合一个简单的《计算器》软件来展示这个流程：

![img](http://www.py-me.com/mkdoc_images/liuchengtu.png) 

## 1. **项目管理**

​	双击启动PyMe.exe，首先进入的是项目管理界面，首先开发者可以根据在右上角需要选择所用语言，这里我们点击“简”选择简体中文。

![img](http://www.py-me.com/mkdoc_images/wps30.jpg) 

图示：登录界面

#### 一、**基本设置:** 

在开始进入到项目之前，我们先来了解一下软件的设置，在语言选择部分的上部“基于Python 3.8.8开发”文字右边有一个“齿轮”，点击它，可以进入到设置页。

![img](http://www.py-me.com/mkdoc_images/wps130.jpg) 

在这个“设置”对话框中有三个页面，分别为“常用设置”、“设计操作”、“代码编辑”，这里主要说明一下，在第一次使用PyMe时需要注意“常用设置”里的相关设置。

 

1、“环境”分为“真实环境”和“虚拟环境”，需要注意区分并正确设置。

“真实环境”就是我们从Python官方网址下载Python安装程序进行安装，作为PyMe的执行环境，选中后设置Python目录为Python.exe所在目录。

“虚拟环境”是使用Conda等容器环境，使用容器中创建的Python环境作为PyMe的执行环境，选中后，会列出我们创建的Python环境名称，选择即可。

 

2、“分辨率”：这个“分辨率”指定当前软件是否受DPI的影响。

“高分辨率”会更加精细，但打包时会增大包体文件。

“低分辨率”会更加粗颗粒，但打包时会减小包体文件，因为会去掉相关库的使用。

 

3、“打开项目时备份”可指定每次打开工程前，会先对工程的源码进行备份，备份文件会自动保存到项目所在目录的BackUp子目录中，需要时在PyMe中双击“BackUp”图标，进入“BackUp”目录，然后双击对应的备份文件即可恢复到对应备份时的项目文件。

也可以在项目开发中，随时通过CTRL+B快捷键来进行项目备份，也可以通过CTRL+R快捷键来恢复最近的备份。

“备份数量”限制，指定了自动备份的最大数量。

 

1、“版本下载目录”指定了自动下载增量更新时的下载文件本地目录，如果版本不一致，在启动PyMe后会在顶部显示最新版本的文字，点击即可进入更新。

![img](http://www.py-me.com/mkdoc_images/wps131.jpg) 

图示：有新版本时的更新提示

 

2、“Android字体”指定了打包APK时，安卓系统字体不支持中文时，需要设置为使用TTF或OTF文件。“TTF应用范围”指定这种字体文件是应用于所有文字还是只应用于中文显示。

3、“多状态图片生成规则”代表在设置多状态按钮（普通状态、鼠标移入状态，点击状态）时，使用状态图片的命名规则。

 

“设计操作”和“代码编辑”主要帮助开发者在开发中进行一些辅助设置，大家可以自行体验尝试。

#### 二、**登录账号:** 

​	默认情况下，开发者可以使用游客模式进行开发，如果想要使用平台功能，则需要点击图示中红框位置，进入到登录界面，在登录界面里，将可以注册新账号：

![img](http://www.py-me.com/mkdoc_images/wps31.jpg) 

 

​	在这里，我们仍然使用“离线使用”进入到启动界面，在这个界面中，我提供了五个选项的选项卡：

#### 三、**新建项目:** 

​	提供了***\*空界面项目\****，***\*对话框项目\****，***\*单文档项目、多文档项目、数据库应用（DBMS）、2D游戏项目和3D游戏项目以及Git-SVN拉取项目 八\****种模版供选择，开发者可以跟据需要在此基础上创建项目。

 

**1、*****\*空界面项目\****：空白的界面项目框架，你可以随意的设计界面。

![img](http://www.py-me.com/mkdoc_images/wps32.jpg) 

图示：空界面项目设计视图

***\*2、对话框项目\****：最简单的登录框，方便开发者了解界面控件的使用。

![img](http://www.py-me.com/mkdoc_images/wps33.jpg) 

图示：对话框编辑运行演示

***\*3、单文档项目\****：单文档的Python代码编辑器项目，具备基本的代码文件的创建、打开、编写与运行。

![img](http://www.py-me.com/mkdoc_images/wps34.jpg) 

图示：单文档运行演示

***\*4、多文档项目\****：简单的多文档的Python项目IDE，包括对一个简单Python项目进行多文件编辑、运行、打包的功能。

![img](http://www.py-me.com/mkdoc_images/wps35.jpg) 

图示：多文档运行演示

***\*5、DBMS项目\****：简单的小型数据库管理软件，展示了基本的数据库管理软件框架和数据库组件的使用。

![img](http://www.py-me.com/mkdoc_images/wps36.jpg) 

图示：数据库框架设计演示

***\*6、2D游戏项目\****：2D的游戏开发框架，提供了动画、粒子、角色、界面、场景等编辑器的功能。

![img](http://www.py-me.com/mkdoc_images/wps37.jpg) 

图示：2D游戏中场景编辑演示

***\*7、3D游戏项目\****：3D的引擎开发框架，目前只有部分底层库，工具尚不完善。

![img](http://www.py-me.com/mkdoc_images/wps38.jpg) 

图示：3D游戏中场景编辑演示

 

​	项目创建成功后，我们将立刻进入到主设计界面进行项目开发，我们可以通过右上角的关闭按钮来返回到项目管理控制台。

#### 四．**打开项目:** 

​	“打开项目”的面板主要用于显示已经创建的近期项目，在列表中以图标方式显示，我们只需要选择需要的项目并点击“确定”即可进入项目，第一个显示为加号的按钮，用于加载一个不在图标列表中的项目。

 

![img](http://www.py-me.com/mkdoc_images/wps39.jpg) 

图示：“打开项目”选项页中的最近项目

 

#### 五、实例项目:**

​	“实例项目”页主要展示我们从开发者商店下载的项目案例，开发者商店属于平台功能，必须要注册账号并登录后，才可以看到。这些案例从开发者商店下载后将保存在“Examples”文件夹中。

 

![img](http://www.py-me.com/mkdoc_images/wps40.jpg) 

图示：“实例项目”页面中展示了从开发者商店下载的案例

![img](http://www.py-me.com/mkdoc_images/wps41.jpg) 

图示：开发者商店中展示的可下载案例。

 

![img](http://www.py-me.com/mkdoc_images/wps42.jpg) 

图示：案例的详细介绍。

 

 

***\*实例工程\****包括了不同分类下的数十个案例，比如：

**UIData**:界面嵌入演示，演示了如何在一个对话框中嵌入另一个界面，并访问它们的数据。

![img](http://www.py-me.com/mkdoc_images/wps43.jpg) 

**PDFTool**:演示了PDF文件拆分与合并工具的开发。

![img](http://www.py-me.com/mkdoc_images/wps44.jpg) 

**批量发票识别导出*****\*：\****对发票图片进行识别并整理成表格，方便财务快速统计。

![img](http://www.py-me.com/mkdoc_images/wps45.jpg) 

**计算器**：一个简单的计算器案例，演示了控件变量的绑定和使用。

![img](http://www.py-me.com/mkdoc_images/wps46.jpg) 

**五子棋**:一个基于画布的绘图功能制作的五子棋游戏。

![img](http://www.py-me.com/mkdoc_images/wps47.jpg) 

 

人脸识别：通过人脸识别库来对摄像头采集的图像进行人脸识别。

![img](http://www.py-me.com/mkdoc_images/wps48.jpg) 

 

工程案例比较多，感兴趣的开发者可以从开发者商店进行下载体验。

## 2. **界面设计**

在“新建项目”页面选择“空界面”，然后设定项目路径后，点击“确定”按钮。这时会进入到空界面的设计视图。

![img](http://www.py-me.com/mkdoc_images/wps49.jpg) 

图示：空界面项目设计视图说明

#### **一、视区讲解：**

界面设计视图分为以下七个部分，具体说明如下：

**1、*****\*顶部菜单\****：PyMe工具的基本设置、新手入门向导教程和独立的实用工具。

**2、*****\*控件与界面的快捷功能按钮\****：每个控件的常用设置项。

**3、*****\*控件与组件创建工具条\****：提供可以拖拽到界面上使用的控件与各种组件。

**4、*****\*主设计区\****：对界面及控件进行摆放和调整的设计区域。

**5、*****\*控件树与属性编辑面板\****：罗列当前界面已创建的所有控件和组件。 

**6、*****\*绘图工具条\****：用于在画布中进行图形绘制的工具条。

**7、*****\*项目文件与文件夹列表栏\****：用于访问项目的文件与文件夹。

 

​	下面以计算器软件项目来介绍如何进行界面设计，我们在主视计区用鼠标选中窗体，它的边框的八个方向会显示一个可以拖拽的橙色小方块，我们用鼠标点击它后拖拽到合适的大小即可。

![img](http://www.py-me.com/mkdoc_images/wps50.jpg) 

在设置好窗体的大小后，我们可以在右边的属性编辑面板对窗体进行相应的设置。“设置属性”一栏里罗列了当前窗体的基本属性设置：

宽：窗体窗度

高：窗体高度

布局方式：窗体采用“打包排布”、“表格排布”还是“数值定位”。

背景：当前窗体背景色

图片：当前窗体的背景图片

标题：当前窗体的标题栏文字

窗口菜单：当前窗体菜单管理器，用于编辑菜单。

程序图标：当前项目的程序图标

有标题栏：设置是否使用标题栏

可调整大小：设置窗体是否可以通过边缘拖动进行大小调整

系统托盘：当前项目的托盘管理器，用于编辑运行项目时显示在WINDOWS系统任务栏的托盘菜单，比如下图就属于系统托盘。

![img](http://www.py-me.com/mkdoc_images/wps51.jpg) 

 WINDOWS上的系统托盘图标

拖拽边框宽度：拖拽窗口边缘时的区域宽度。

拖拽边缘颜色：拖拽窗口边缘时的区域显示颜色。

主题样式：当前窗体使用的皮肤样式。

始终居前：设置当前窗体是否始终运行在当前桌面的最前面。

透明色值：设置是否对窗体进行关键色镂空的设置，用于制作一些类似以下效果的窗体。

圆角半径：设置窗体是否进行圆角设置。

透明度：设置窗体是否使用透明效果，用于制作半透明窗体。

#### **二、控件创建：**

​	一般来说，计算器软件包括一个数值展示标签和一些按钮，比如这样：

![img](http://www.py-me.com/mkdoc_images/wps52.jpg) 

​	在PyMe中有两种方法来创建控件，第一种方式是通过从控件和组件工具条进行拖拽来创建。

![img](http://www.py-me.com/mkdoc_images/wps53.jpg) 

​	第二种方式是通过在窗体上用鼠标右键单击，然后在“创建控件”菜单项下选择对应的控件类型来创建。

![img](http://www.py-me.com/mkdoc_images/wps54.jpg) 

​	下面来选中这个Label，这时我们可以直接通过拖拽控件以及橙色小方块来调整它的位置和大小。在默认情况下，控件采用“数值定位”，数值可以使用像素位置或百分比，在选中控件的情况下，在设计区下部的绘图工具条之上，会有一条布局设置工具条，在这里我们可以设置相应的布局方式，以及控件的X、Y、宽度和高度等数值。

![img](http://www.py-me.com/mkdoc_images/wps55.jpg) 

  					图示：布局设置工具条。 

​	在这里，我们将Label设置X位置0像素，Y位置0像素，宽度为100%，高度为30像素，并在右边的属性栏中选择“背景”属性为深灰色，字体为32大小的System字体，文字色为白色，并设置右对齐，也可以通过顶部的快捷按钮来进行设置。

![img](http://www.py-me.com/mkdoc_images/wps56.jpg) 

​	设置好Label之后，我们来创建按钮。

​	从工具条中拖动创建一个Button或者通过右键菜单来创建一个Button，放置到Label下方靠左位置，调整大小，作为数字“1”按钮。

![img](http://www.py-me.com/mkdoc_images/wps57.jpg) 

​	下面我们来修改一下按钮的文字内容，对于控件的文字，PyMe同样提供了多样化的修改方式：

1、通过双击右边属性栏的“文本”属性，在弹出对话框中进行修改。

2、在控件上用鼠标右键点击，在弹出菜单中选择“设置文字内容”菜单项。

3、选中控件后按CTRL+退格键来消除“文本”属性，然后直接输入文字。

![img](http://www.py-me.com/mkdoc_images/wps58.jpg) 

​	然后我们通过属性栏和顶部栏对控件字体进行设置，也可以通过属性栏和顶部快捷栏来设置字体与大小。

![img](http://www.py-me.com/mkdoc_images/wps59.jpg) 

 

#### **三、控件复制：**

​	在完成按钮“1”之后，我们还需要创建出其它按钮，这时可以通过控件的复制功能来快速的创建。控件的复制有两种方法：

1、选中控件按CTRL键+C键进行复制，然后按CTRL键+V键进行粘贴。

2、按着ALT键拖动控件。

 

![img](http://www.py-me.com/mkdoc_images/wps60.jpg) 

​	图示：通过ALT键拖动控件方式复制控件。

​	通过控制复制和快速设置文字，我们可以快速的制作出界面的所有控件。

![img](http://www.py-me.com/mkdoc_images/wps61.jpg) 

​            图示：所有的界面控件

## 3. **控件设置**

​	控件的设置分为属性设置和样式设置两方面：

#### **一、属性设置：**

​	属性设置主要通过右边的属性栏来进行，在上面的界面设计中，我们已经完成了基本的界面可视化创建和控件的基本属性设置，在这里我们可以再细致的调节一下相关属性。

![img](http://www.py-me.com/mkdoc_images/wps62.jpg) 

​	Label的属性包括：

名称：控件自定义名称，方便开发者定义控件。

背景：背景颜色设置。

文本：文字内容。

自动换行：是否文字到达边界后自动换行。

字体：字体设置。

文字色：文字的颜色：

对齐：文字在控件中的对齐位置。

图片：控件的背景图片。

图片位置：设置图片在控件中的位置。

样式：边框的样式。

圆角半径：控件圆角的半径。

显示：是否设置显示或隐藏。

 

![img](http://www.py-me.com/mkdoc_images/wps63.jpg) 

​	Button的属性包括：

名称：控件自定义名称，方便开发者定义控件。

背景：背景颜色设置。

文本：文字内容。

字体：字体设置。

文字色：文字的颜色：

对齐：文字在控件中的对齐位置。

按下时字颜色：鼠标按下时的文字颜色。

按下时背景色：鼠标按下时的背景颜色。

图片：控件的背景图片。

图片位置：设置图片在控件中的位置。

样式：边框的样式。

状态：正常还是失败。

圆角半径：控件圆角的半径。

显示：是否设置显示或隐藏。

​	本实例演示了两个常见控件的属性，其它的控件开发者可以再跟着官方教程学习或自行尝试，在这里不再赘述。

#### 二、**样式设置：**

​	在文件与资源栏点击“STY”标记的图标，可以进入到样式编辑器。在样式编辑器里可以为一些控件编辑外观属性。

在这里，我们创建一个MyStyle的TButton样式，并设定一些样式属性。

![img](http://www.py-me.com/mkdoc_images/wps64.jpg) 

​	编辑好之后点击“保存样式”，就可以在界面设计视图应用了，只需要在对应的控件上用鼠标右键单击，然后在弹出的菜单里找到“选择样式”菜单项，然后在其子菜单项中选择样式，或者选择为同类控件应用此样式，就可以快速化的设定控件使用编辑好的样式了。

![img](http://www.py-me.com/mkdoc_images/wps65.jpg) 

​	点击“同类型应用MyStyle.TButton”后即可完成对所有按钮的样式设置。

![img](http://www.py-me.com/mkdoc_images/wps66.jpg) 

 

​	如果你不能很好的设置样式，也可以选择使用官方的皮肤样式，可以实现一键对整个界面的美化。

## 4. **变量绑定**

​	“变量绑定”的作用是为界面或控件设置一些变量，以方便开发者随时存取和设置。比如在当前的计算器界面上，我们还需要设定三个变量值，包括被操作数、操作符号与操作数。我们在当前界面上用鼠标右键在Label上单击，在弹出的菜单中选择“变量绑定”。

![img](http://www.py-me.com/mkdoc_images/wps67.jpg) 

​	这时弹出“Label_1”的绑定数据编辑区对话框，这个对话框左边是一个数据项列表，右边是输入和操作按钮。我们输入以下三个数据项：

***\*参数1\****：“当前值” ，数据类型设为“浮点型”，数据默认值为0.0，并勾选“映射到显示文字”，使这个变量值设置为控件的文本内容。

***\*参数2\****：“操作类型”，数据类型设为“整型”，数据默认值为0。

***\*参数3\****：“被操作数”，数据类型设为“浮点型”，数据默认值为0.0。



![img](http://www.py-me.com/mkdoc_images/wps68.jpg) 

​	创建完成后，点击“确定”按钮，Label_1控件上就绑定了我们设定的用户变量。我们可以在代码中访问和设置。

## 5. **事件响应**

​	下面我们来为按钮点击事件绑定一个函数，这样我们就可以在函数中编写代码来完成对应的逻辑处理。在按钮“1”上用鼠标右键单击，选择菜单项“事件响应”，进入到事件响应处理编辑区对话框。

![img](http://www.py-me.com/mkdoc_images/wps69.jpg) 

​	弹出的“Button_1”的事件响应处理编辑区对话框，我们可以看到左边有一个事件列表，罗列了常用的控件事件，在右边有一个输入框，显示了默认的函数名称，我们也可以修改它。

​	在右下方罗列了触发事件后一些常用的处理逻辑，包括了：

1、编辑函数代码：进入到代码编辑器的事件函数中，编写逻辑代码。

2、删除事件函数：删除控件已经绑定的指定事件函数。

3、设置弹出菜单：弹出一个菜单。

4、设置光标：设置鼠标的形态。

5、调用其它界面：包括一些常用的通用对话框，如（打开文件对话框、保存文件对话框、打开目录查找对话框，调用选择颜色对话框，调用自定义界面）。

6、跳转到其它界面：跳转到另一个界面。

7、控件中加载界面：在容器控件（Frame,LabelFrame,Notebook,PanedWindow)中加载一个界面。

8、调用数据库操作：调用数据库组件进行查询、增、删、查、改等功能。

 

![img](http://www.py-me.com/mkdoc_images/wps70.jpg) 

​	在这里，我们选择“Command”事件后点击“编辑函数代码”按钮，进入按钮控件Button_1的Command事件的函数代码编辑区。

![img](http://www.py-me.com/mkdoc_images/wps71.jpg) 

​	这样我们就可以开始准备为Button_1在触发点击事件后的响应函数编写函数。

​	实际上，为一个控件的事件绑定响应函数也有另外三种方法：

​	1、在右边“事件响应”页下双击对应的事件栏，可快速的为事件绑定响应函数。

​	2、双击控件，可迅速绑定首个事件的响应函数并进入代码编辑。

![img](http://www.py-me.com/mkdoc_images/wps72.jpg) 

​	3、在代码编辑器右侧的助手栏中，选中控件，并在下部的控件事件类型列表中选择相应的事件后，点击“绑定函数”进行绑定，在这里也可以点击“解绑函数”来删除响应函数。

![img](http://www.py-me.com/mkdoc_images/wps73.jpg) 

## 6. **逻辑编写**

#### 一、**Fun函数库：**

​	Fun函数库文件是PyMe软件的界面底层支持库，它提供了大量的函数来访问界面，设置控件及数据，可以极大的方便开发者快速化的进行界面交互的调用。

​	使用Fun函数的方法有两种：

​	1、直接输入“***\*Fun. ”\****，通过智能提示来选择函数。

![img](http://www.py-me.com/mkdoc_images/wps74.jpg) 

​	2、通过鼠标右键菜单，在“界面函数”菜单项下找到对应控件的功能函数菜单项，来快速生成函数，这种方式非常适合初学者快速掌握控件的功能调用。

![img](http://www.py-me.com/mkdoc_images/wps75.jpg) 

​	如果想要了解函数的实现，可以按着CTRL键，然后将鼠标移动到控件上，这时会浮现出函数的解释和代码实现。

![img](http://www.py-me.com/mkdoc_images/wps76.jpg) 

 

​	Fun函数的列表和解释放于附录中。

#### **二、逻辑实现：**

​	在Button_1_onCommand函数内，我们编写代码：

```
	当前值 = Fun.GetUserData(uiName,'Label_1','当前值')

	当前值 = 当前值 * 10 + 1

	Fun.SetUserData(uiName,'Label_1','当前值',当前值)

```

这段代码实现了将当前值由0变为1，再按一次变为11的实现。

![img](http://www.py-me.com/mkdoc_images/wps77.jpg) 

在完成按钮“1”的代码实现后，我们在右侧助手栏选择按钮“2”，在下面的控件事件类型列表中选择“点击事件”，点击“绑定函数”，为Button_2生成点击事件的响应函数。

![img](http://www.py-me.com/mkdoc_images/wps78.jpg) 

 

​	然后我们将上面Button_1_onCommand中的代码复制到Button_2_onCommand中，将语句“当前值 = 当前值 * 10 + 1” 改为“当前值 = 当前值 * 10 + 2”，并依次为其它的按钮逐一完成相应的函数绑定，并为数字按钮做相同代码操作。

​	然后，我们来为“+”按钮加入以下代码，将当前值存入被操作数，并设置操作类型为1，对当前值进行置0操作：

 

```
def Button_4_onCommand(uiName,widgetName):

  当前值 = Fun.GetUserData(uiName,'Label_1','当前值')

  Fun.SetUserData(uiName,'Label_1','被操作数',当前值)

  Fun.SetUserData(uiName,'Label_1','操作类型',1)

  Fun.SetUserData(uiName,'Label_1','当前值',0.0)
```

![img](http://www.py-me.com/mkdoc_images/wps79.jpg) 

​	采用同样的方式，我们继续完成“减法”、“乘法”、“除法”按钮的逻辑实现。只是对操作类型变为2，3，4。然后是“C”按钮的处理，“C”是“CLS”的缩写，代表了重置操作。我们在其中加入代码：

```
  Fun.SetUserData(uiName,'Label_1','被操作数',0.0)

  Fun.SetUserData(uiName,'Label_1','操作类型',0)

  Fun.SetUserData(uiName,'Label_1','当前值',0.0)
```

 

​	最后是“=”按钮，用于计算运行结果。

​	在四则运算中，结果 = 被操作数 按照运算符操作 操作数

​	而操作数就是“当前值”，所以代码如下：

```
def Button_15_onCommand(uiName,widgetName):

  被操作数 = Fun.GetUserData(uiName,'Label_1','被操作数')

  操作类型 = Fun.GetUserData(uiName,'Label_1','操作类型')

  操作数 = Fun.GetUserData(uiName,'Label_1','当前值') 

  结果 = 0.0

  if 操作类型 == 1:

     结果 = 被操作数 + 操作数

  elif 操作类型 == 2:

     结果 = 被操作数 - 操作数

  elif 操作类型 == 3:

     结果 = 被操作数 * 操作数

  elif 操作类型 == 4:

     if 操作数 == 0.0:

       Fun.MessageBox(text='除数不能为零',title='提示',type='info',parent=None)

     else:

       结果 = 被操作数 / 操作数

  Fun.SetUserData(uiName,'Label_1','当前值',结果)
```

![img](http://www.py-me.com/mkdoc_images/wps80.jpg) 

## 7. **调试运行**

​	在完成了界面设计与逻辑编写后，我们可以点击右上角“运行”按钮，来运行当前项目。

​	如果没有错误，我们将可以看到当前运行的结果。

![img](http://www.py-me.com/mkdoc_images/wps81.jpg) 



 

我们可以对运行的计算器进行测试：

 

| ***\*第一步：点击“5”，作为被操作数\****                      | ***\*第二步：点击“X”，设置运算符号\****                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![img](http://www.py-me.com/mkdoc_images/wps82.jpg) | ![img](http://www.py-me.com/mkdoc_images/wps83.jpg) |
| ***\*第三步：点击“2”和“0”，作为操作数\****                   | ***\*第四步：点击“=”，得出结果\****                          |
| ![img](http://www.py-me.com/mkdoc_images/wps84.jpg) | ![img](http://www.py-me.com/mkdoc_images/wps85.jpg) |

 

​	如果运行中出现一些错误，这时我们需要进行调试，在PyMe中提供了基础的断点调试功能，我们可以用鼠标点击行号位置，在相应行号设置断点，然后通过下部的调试按钮工具条来控制调试。

 

![img](http://www.py-me.com/mkdoc_images/wps86.jpg) 

 

​	在调试工具条中，共包括了一个启动窗口和六个按钮。

![img](http://www.py-me.com/mkdoc_images/wps87.jpg) 

启动窗口代表启动调试从哪个窗口开始运行。后面的六个按钮分别为：

![img](http://www.py-me.com/mkdoc_images/wps88.jpg) 启动调试，快捷键为F5。

![img](http://www.py-me.com/mkdoc_images/wps89.jpg) 逐行执行，如果有函数，不进入函数，快捷键为F10。

![img](http://www.py-me.com/mkdoc_images/wps90.jpg) 逐行执行，如果有函数，进入函数，快捷键为F11。

![img](http://www.py-me.com/mkdoc_images/wps91.jpg) 跳出函数，转到下一行。

![img](http://www.py-me.com/mkdoc_images/wps92.jpg) 重启调试。

![img](http://www.py-me.com/mkdoc_images/wps93.jpg) 停止调试。

 

​	在这里我们点击“![img](http://www.py-me.com/mkdoc_images/wps94.jpg)”启动调试，当我们再次进行计算，并点击“=”按钮后，我们将看到中断。

 

![img](http://www.py-me.com/mkdoc_images/wps95.jpg) 

 

​	中断响应后，我们可以点击“![img](http://www.py-me.com/mkdoc_images/wps96.jpg)”逐行执行，在需要进入函数的时候点击“![img](http://www.py-me.com/mkdoc_images/wps97.jpg)”。并查看下部的变量值，这样就可以对代码进行调试了。结束调试后点击“![img](http://www.py-me.com/mkdoc_images/wps98.jpg)”即可。

## 8. **皮肤美化**

​	在完成项目的开发后，我们可以对皮肤进行美化，在PyMe的开发者商店中，提供了一些ttk的美化方案，下载后可以一键使用。

首先，注册并登录账户，然后选择“皮肤商店”页面，在这个页里里，罗列了一些官方提供的皮肤样式，可以付费购买。

![img](http://www.py-me.com/mkdoc_images/wps99.jpg) 

​	购买后，将会安装到PyMe中，然后我们进入到“打开项目”页，再次进入到我们的计算器项目。

![img](http://www.py-me.com/mkdoc_images/wps100.jpg) 

​	在主题样式选择所安装的样式文件，计算器瞬间变了样：

![img](http://www.py-me.com/mkdoc_images/wps101.jpg) 

 

![img](http://www.py-me.com/mkdoc_images/wps102.jpg) 

![img](http://www.py-me.com/mkdoc_images/wps103.jpg) 

## 9. **打包发布**

​	现在，我们已经完成了所有的开发工作，工们可以进入到最后的打包发布。

在PyMe中，支持一键打包为多样化的可执行程序，我们只需要点击右上角的“发布”按钮，但我们必须登录账号才能打包。

#### **一、打包EXE：**

​	PyMe目前集成了pyinstaller和nuitka两种打包工具，默认使用“pyinstaller”工具，在对话框里主要包括以下一些设置：

1、打包类型：选择打包成目录，或者打包成一个单一的文件。

2、打包类型：在某些应用软件，需要通过控制台输出信息，在这里可以选择是否附带控制台输出窗口。

3、加密文件：默认情况下，pyinstaller打包应用软件，并不能保护好代码被破解，在这里可以选择“使用加密”，这是一项VIP功能，可以对Python代码进行C转码后编译成pyd再进行打包，大大保护了项目源码。

![img](http://www.py-me.com/mkdoc_images/wps104.jpg) 

​	点击“启动打包”后，将会在文本框输出相应的打包信息，等待一小段时间，即可看到打包完成的提示。

![img](http://www.py-me.com/mkdoc_images/wps105.jpg) 

​	进入打包输出的目录，可以看到打包好的可执行文件。

 

![img](http://www.py-me.com/mkdoc_images/wps106.jpg) 

​	Nuitka也是一种加密式的打包工具，它会将Python代码先转为C再进行编译，但目前Nuitka打包方式仍存在一些BUG，暂不推荐，有能力的开发者可以尝试。

#### 二、**打包APK：**

​	PyMe致力于推动Python在移动设备的打包能力，在这里我们可以选择平台为“android”，然后点击“运行”按钮，这时会弹出分辨率对话框。

![img](http://www.py-me.com/mkdoc_images/wps107.jpg) 

​	这时，会弹出一个窗口，模拟了移动设备的显示效果。

![img](http://www.py-me.com/mkdoc_images/wps108.jpg) 

​	如果没有问题，再点击“发布”按钮，这时会进入到Android平台的打包对话框：

![img](http://www.py-me.com/mkdoc_images/wps109.jpg) 

 

​	在Android打包设置对话框中，我们需要设置好相关的SDK和系统变量，在下部的文本框中罗列了具体的步骤，需要逐一进行设置和确认。

​    ![img](http://www.py-me.com/mkdoc_images/wps110.jpg)

 

​	完成相应的设置后，点击“启动编译”，PyMe将开始进行Android打包。

![img](http://www.py-me.com/mkdoc_images/wps111.jpg) 

​	完成打包后会显示“Android打包成功”的提示，这时我们可以在输出目录里看到生成的APK文件。

 

![img](http://www.py-me.com/mkdoc_images/wps112.jpg) 

我们将可以将APK安装到手机上进行测试。

# **平台功能介绍：资源下载与UP主**

​	PyMe开发者平台致力于建设一个UGC的Python作品平台，从而实现代码价值的交换和变现。

所以，开发者平台并不仅仅为官方发布作品，更重要的是让开发者用户提交作品。

 

***\*当前的开发者平台包括以下三个方面的内容：\****

#### 一、**实例项目：提供各种基于PyMe的小型案例项目。**

![img](http://www.py-me.com/mkdoc_images/wps113.jpg) 

***\*实例项目商店\****目前包括界面基础、文件操作、表格处理、网络数据、图形图像、机器学习、游戏开发、数字孪生、智能硬件、其它工具等分类。通过点击右边的“获取”或“价格”按钮即可购买并下载安装。

下载安装后，将会出现以“我的实例”页面，以方便打开。

![img](http://www.py-me.com/mkdoc_images/wps114.jpg) 

打开“WIFI密码破解”项目后的视图。

![img](http://www.py-me.com/mkdoc_images/wps115.jpg) 

通过这样的方式，开发者将可以学习到作者是如何创作相关的软件。

 

#### 二、**组件商店：提供具有单一功能的组件类。**

![img](http://www.py-me.com/mkdoc_images/wps116.jpg) 

​	组件商店同样也包括一些分类，开发者下载后可以在项目中使用，只需要点击“其它”页下面的“导入模块”后，会打开“Market_com”目录，选择相应的组件即可。

![img](http://www.py-me.com/mkdoc_images/wps117.jpg) 

​	这里我们以组件“MultiPage”为例，点击“确定”后，组件会出现在工具条上。

![img](http://www.py-me.com/mkdoc_images/wps118.jpg) 

​	设置好后，我们准备几张图片，放置到Resources目录下。

![img](http://www.py-me.com/mkdoc_images/wps119.jpg) 

​	然后为Form_1绑定Load事件函数，我们编写代码：

 

```
def Form_1_onLoad(uiName):

  MultiPage_1 = Fun.GetElement(uiName,'MultiPage_1')

  MultiPage_1.AddPage('第一页','1.png','A.py')

  MultiPage_1.AddPage('第二页','2.png','B.py')

  MultiPage_1.AddPage('第三页','3.png','B.py')
```

​	完成后，点击“运行”，可以看到组件MultiPage的运行效果，它实现了多页的切换卡效果。

![img](http://www.py-me.com/mkdoc_images/wps120.jpg) 

#### 三、**皮肤商店：**

​	皮肤商店主要用于提供皮肤样式，用于整体更换案例的皮肤样式，在前面的“皮肤美化”部分介绍过，在此不在赘述。

#### 四、**UP主申请：**

​	UP主这个角色定义为发布作品的开发者，将享有作品发布后的下载付费收益的分成。（有效下载的30%为平台运营收入，余下70%为UP主（税前）收入，将在（1）满足100元人民币或（2）每年12月底进行兑付）。

在“我是UP主”页面，开发者可以提交申请，成为UP主。

![img](http://www.py-me.com/mkdoc_images/wps121.jpg) 

​	点击“申请成为UP主”按钮，将弹出“申主成功UP主”的信息提交对话框，在这里需要提交个人信息，以确保享有所发布的产品收益，并担任相应的法律责任（包括版权和病毒、木马风险传播责任）。

![img](http://www.py-me.com/mkdoc_images/wps122.jpg) 

​	提交后，审核通过将会收到邮件，便可以在“我是UP主”页面提交工程案例、组件和皮肤，作品通过审核后，将会发布在开发者商店。

![img](http://www.py-me.com/mkdoc_images/wps123.jpg) 

**写在最后：**

​	作为一个简单的工具说明书，写到这里暂告结束，大量的控件属性、细节功能和使用方法，并未在文档中一一列出，更详细的使用说明和案例讲解请陆续关注B站视频以及官方教材，PyMe从零起步发展到今天，实属不易，在这个过程中，粉丝们给予了我莫大的信任和支持，使我能够坚持下来，我对此衷心的表示感谢！

最后，送给大家一首PyMe学习歌，祝各位在使用PyMe的过程中一切顺心，记得备份哟（CTRL+B)~ 

​																						火云红孩儿 

​																						2023/11/15

 

![img](http://www.py-me.com/mkdoc_images/wps124.png) 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

# **附录：Fun函数速查手册**

Fun函数包括了大量的封装函数，分为系统函数、界面函数和功能类，系统函数主要用于辅助系统调用和功能，界面函数主要用于辅助对界面控制的访问和设置。

#### **一、系统函数：**

***\*字符串判断类：\****

IsInt(text)：判断字符串内容是否是整数

IsFlot(text)：判断字符串内容是否是浮点数

IsNumeric(text：判断字符串内容是否是数字

CheckSpecialChar(text)：判断字符串是否包含特殊字符

IsMobilePhone(text)：判断字符串是否为手机号

IsEmail(text)：判断字符串是否为邮件地址

 

***\*随机数与日期时间：\****

RandNumber(begin=0,end=100)：在begin~end间生成一个随机整数

GetCurrTime(splitChar=':')：取得当前时间的字符串，参数为间隔符

GetCurrDate(splitChar=':')：取得当前日期的字符串，参数为间隔符

 

***\*辅助功能：\****

OutputProcessToText(cmdText,uiName,elementName)：运行命令并输出到对应的ListBox或Text中。

LoadImageFromFile(imagefile)：从文件中加载一个图片。

MessageBox(text="",title="info",type="info",parent=None)：弹出一个信息对话框。参数1 :对话框显示文字 ,参数1:显示文字,参数2:标题文字,参数3:对话框类型,可选:info、warning、error

InputBox(title,text)：弹出一个输入对话框。参数1 :对话框标题文字 ,参数2:对话框默认框输入文字 。

AskBox(title,text)：弹出一个选择对话框,你需要选择YES或NO。参数1 :对话框标题文字 ,参数2 :对话框显示文字 。

SelectDirectory(title="选择路径",initDir = os.path.abspath('.'))：打开查找目录对话框

SelectColor(title="请选择颜色")：打开选取颜色对话框

EnumFontName()：罗列当前系统的所有文字

WalkAllResFiles(parentPath,alldirs=True,extName=None)：返回对应目录的所有指定类型文件。参数1 :目录名称 ,参数2 :是否进入子目录,参数3:是否有扩展名筛选 。

ImportResources(srcFile,coverMode=True)：将文件复制到资源目录

CopyFile(srcFile,dstFile,coverMode=True)：复制文件

MoveFile(srcFile,dstFile,coverMode=True)：移动文件

DeleteFile(dstFile)：删除文件

GetFileMD5(srcFile)：取得文件MD5码

CompareFileMD5(srcFile,dstFile)：比较两个文件是否一致

CreateDir(dstDir,coverMode=True)：创建目录

CopyDir(srcDir,dstDir,coverMode=True)：复制目录

MoveDir(srcDir,dstDir,coverMode=True)：移动目录

DeleteDir(srcDir)：删除目录

CheckIsDir(srcDir)：判断是否是目录

CheckExist(srcDir)：判断文件或目录是否存在

checkPtInRect(x,y,left,right,top,bottom)：判断点是否在矩形中

ReadFromFile(filePath,encoding='utf-8',autoEval=False):从一个文件中读取内容。

WriteToFile(filePath,content,encoding='utf-8'):将内容写入到一个文件中。

OpenFile(title="Open Python File",filetypes=[('Python File','*.py'),('All files','*')],initDir = ''):调用打开文件框

SaveFile(title="Save Python File",filetypes=[('Python File','*.py'),('All files','*')],initDir = '',defaultextension='py'):调用保存文件框

GetResourcePath(FileName):查询一个资源文件的路径

 

#### **二、界面函数：**

界面函数一般以uiName为第一参数，代表了界面类名，在第一次调用界面时，这个uiName的值就是当前工程名，在被重复调用时，会以“_索引”作为后缀。

在多数控件相关的函数中，会有第二参数elementName代表了控件名称。

 

Register(uiName,elementName,element,alias=None,groupName=None,styleName=None)：注册一个控件以便访问，由PyMe生成的界面文件中调用。

DestroyUI(uiName,result=0,animation='')：关闭窗口，参数result代表返回值，animation为关闭窗口的动画类型，包括缩放动画zoomout和渐隐动画fadeout。

GetElement(uiName,elementName)：取得控件。

GetElementName(element)：取得控件的名称。

GetElementType(uiName,elementName)：取得控件的类型

GetElementXYWH(uiName,elementName)：取得控件的绝对位置

AddTKVariable(uiName,elementName,defaultValue = None)：为控件增加一个Tkinter的内置控件变量，参数defaultValue为默认值。

SetTKVariable(uiName,elementName,value)：设置控件的tkinter变量，如Entry，由PyMe生成的界面文件中调用。

GetTKVariable(uiName,elementName)：取得控件的tkinter变量，由PyMe生成的界面文件中调用。

SetTKAttrib(uiName,elementName,AttribName,attribValue)：设置控件的tkinter属性，比如bg、fg、relief等。

GetTKAttrib(uiName,elementName,AttribName)：取得控件的tkinter属性。

AddUserData(uiName,elementName,dataName,datatype,datavalue,isMapToText = 0)：为控件增加一个用户变量。参数dataName为变量名称，datatype为变量类型，包括int,float,string,list,dict等固定类型，如果开发者需要动态的将一个类或自定义类型设为变量，可以输入自定义类型名称即可，datavalue为默认值，isMapToText为int,float,string变量是否作为控件的显示文本。

DelUserData(uiName,elementName,dataName)：删除用户变量。

SetUserData(uiName,elementName,dataName,datavalue)：设置用户变量。

GetUserData(uiName,elementName,dataName)：取得用户变量。

SetVisible(uiName,elementName,Visible)：设置控件显示或隐藏

IsVisible(uiName,elementName)：取得控件显示或隐藏

SetEnable(uiName,elementName,Visible)：设置控件正常或失效

IsEnable(uiName,elementName)：取得控件正常或失效

SetText(uiName,elementName,textValue,aliasName=True):设置控件的文本内容，支持控件(Label、Button、RadioButton、CheckButton、Entry、Text、ComboBox, SpinBox)

InsertText(uiName,elementName,position=tkinter.END,textValue='')：在文本框插入文本

GetText(uiName,elementName)：取得控件的文本内容，支持控件(Label、Button、RadioButton、CheckButton、Entry、Text、ComboBox, SpinBox)

SetFont(uiName,elementName,fontName,fontSize,fontWeight='normal',fontSlant='roman',fontUnderline=0,fontOverstrike=0)：设置控件的字体

GetFont(uiName,elementName,fontName,fontSize,fontWeight='normal',fontSlant='roman',fontUnderline=0,fontOverstrike=0,createifnofind=False)：取得控件的字体

SetBGColor(uiName,elementName,RGBColor)：设置控件的背景颜色

GetBGColor(uiName,elementName)：取得控件的背景颜色

SetTextColor(uiName,elementName,RGBColor)：设置文字的颜色

GetTextColor(uiName,elementName)：取得文字的颜色

SetImage(uiName,elementName,imagePath,autoSize = True)：设置控件的背景图片

GetImage(uiName,elementName)：取得控件的背景图片文件名称。

SetCanvasBGImage(uiName,elementName,imagePath,wrapType='Zoom')：设置画布Canvas上的背景图片，可以设置图片的绘图方式:Original为原始大小,Zoom为缩放匹配画布大小,Tiling为平铺满画布"""

SetImageFromURL(uiName,elementName,url,autoSize = True)：从网络上下载图片设置为控件的背景图片。

LoadGIF(uiName,elementName,imagefile,w=0,h=0)：加载一个GIF动态图片显示到控件上。

StopGIF(uiName,elementName)：停止GIF动画播放

LoadImageToIconList(uiName,elementName,ItemName,imageFile)：为控件加载一个图标列表。

SetItemBGColor(uiName,elementName,lineIndex,color)：设置ComboBox选项的背景色。

SetItemFGColor(uiName,elementName,lineIndex,color)：设置ComboBox选项的文字色。

AddItemText(uiName,elementName,text,lineIndex="end")：增加当前ListBox和ComboBox的文字项内容

AddLineText(uiName,elementName,text,lineIndex="end",textTag=''):为Text控件或ListBox控件增加一行文字

AddPage(uiName,elementName,text,iconFile="",targetUIName='')：为NoteBook增加一个选项页。

SelectPage(uiName,elementName,index=0)：选中NoteBook的指定页

HidePage(uiName,elementName,index=0)：隐藏NoteBook的指定页

DelPage(uiName,elementName,index=0：删除NoteBook的指定页

AddTreeItem(uiName,elementName,parentItem="",insertItemPosition="end",itemName="",itemText="",itemValues=(),iconName="",tag="")：为TreeView增加一个树项。

SetTreeItemText(uiName,elementName,itemName,text)：设置树项的文字

GetTreeItemText(uiName,elementName,itemName)：取得树项的文字

SetTreeItemValues(uiName,elementName,itemName,itemValues)：设置树项的值

GetTreeItemValues(uiName,elementName,itemName)：取得树项的值

SetTreeItemIcon(uiName,elementName,itemName,iconName="")：设置树项的图标

ExpandTreeItem(uiName,elementName,itemName,expand=True)：展开或收缩树项

AddRowText(uiName,elementName,rowIndex ='end',values=(),tag='')：为ListView增加一行，参数rowIndex为行索引,values为各列的文字内容列表。

GetRowTextList(uiName,elementName,rowIndex)：取得ListView的指定行文字内容列表。

GetCellText(uiName,elementName,rowIndex,columnIndex)：取得ListView的指定单元格文字。

SetCellText(uiName,elementName,rowIndex,columnIndex,text)：设置ListView的指定单元格的文字。

DeleteRow(uiName,elementName,rowIndex)：删除指定行

DeleteAllRows(uiName,elementName)：删除所有行

CheckPickedRow(uiName,elementName,x,y)：取得对应鼠标点位置的选中行索引

CheckPickedCell(uiName,elementName,x,y)：取得对应鼠标点位置的选中单元格行列索引

GetSelectedRowIndex(uiName,elementName)：取得ListView的选中行

CheckPickedTreeItem(uiName,elementName,x,y)：取得对应鼠标点位置选中的树项

SelectTreeItem(uiName,elementName,item):选中对应树项

MoveTreeItem(uiName,elementName,itemName,parentItem="",insertItemPosition="end")：将一个树项移动到parentItem下的insertItemPosition位置。

DelItemText(uiName,elementName,lineIndexOrText)：删除当前ListBox和ComboBox的文字项内容。

DelLineText(uiName,elementName,lineIndex="end")：删除Text控件或ListBox控件的指定行文字

DelTreeItem(uiName,elementName,item)：删除树项

DelAllTreeItem(uiName,elementName)：清空所有树项

DelAllLines(uiName,elementName)：清空Text控件或ListBox控件的文字内容。

DelAllItemText(uiName,elementName)：删除ComboBox控件的所有行文字

GetSelectText(uiName,elementName)：取得ListBox、ComboBox、Navigation的选中索引值。

DelSelectText(uiName,elementName)：删除Text控件的选中文字。

GetValueList(uiName,elementName)：取得控件的值列表

SetValueList(uiName,elementName,valueList)：设置控件的值列表

SetCurrentValue(uiName,elementName,value)：设置控件的选中值(RadioButton、CheckButton、Scale、Progress、ListBox、ComboBox、SpinBox、SwitchButton)

GetCurrentValue(uiName,elementName)：取得控件的选中值(RadioButton、CheckButton、Scale、Progress、ListBox、ComboBox、SpinBox、SwitchButton)

GetCurrentIndex(uiName,elementName)：取得控件的选中值(RadioButton、CheckButton、Scale、Progress、ListBox、ComboBox、SpinBox、SwitchButton)

SetCurrentIndex(uiName,elementName,index)：设置ListBox、ComboBox、Navigation的选中索引值。

SetScale(uiName,elementName,minimum,maximum,tickinterval)：设置Scale控件

SetSlider(uiName,elementName,minimum,maximum,value=0)：设置Slider控件

MovingChildPageXViewOffset(uiName,elementName,step=1)：面板内视野横向移动指定步长

MovingChildPageYViewOffset(uiName,elementName,step=1):面板内视野纵向移动指定步长

MovingChildPageXViewTo(uiName,elementName,x=1.0)：面板内视野横向移动到目标位置

MovingChildPageYViewTo(uiName,elementName,y=1.0)：面板内视野纵向移动到目标位置

GetDate(uiName,elementName)：取得日历和日期选择控件的日期

SetDate(uiName,elementName,year,month,day)：设直日历和日期选择控件的日期

InitElementData(uiName)：初始化界面各控件初始数。

InitElementStyle(uiName,Style)：初始化界面各控件初始样式。

GetUIDataDictionary(uiName)：取得界面的所有控件数据。

GoToUIDialog(uiName,targetUIName)：从当前界面跳转到另一个界面

CallUIDialog(uiName,topmost = 1,toolwindow = 1,grab_set = 1,animation='')：调用显示一个界面对话框并返回所有控件的输入值。动画类型fadein - 渐显动画,zoomin - 缩放动画。

LoadUIDialog(uiName,elementName,targetUIName)：在指定控件上加载一个界面

ShowWindow(uiName,WindowState)：设置窗口显示状态

CenterDlg(uiName,popupDlg,dw=0,dh=0)：将弹出界面对话框居中。

MaximizeUI(uiName)：最大化窗口

MinimizeUI(uiName)：最小化窗口

RestoreUI(uiName)：恢复窗口

HideUI(uiName)：隐藏窗口

SetRoundedRectangle(uiName,elementName,WidthEllipse=20,HeightEllipse=20)：

ShowRoundedRectangle(Control,WidthEllipse,HeightEllipse)：设置控件的圆角属性。注意 :此功能不跨平台。

SetTransparencyFunction(root,alpha)：设置窗体透明值。

SetCursor(uiName,elementName,cursor)：设置光标

ExpandAllTreeItem(targetTree,isOpen,parentItem = None)：展开或关闭树项

SetControlPack(uiName,elementName,fill,side,padx,pady,expand)：设置控件的打包布局。

SetControlGrid(uiName,elementName,row,column,rowspan,columnspan)：设置控件的表格布局。

SetControlPlace(uiName,elementName,x,y,w,h,anchorpoint='nw')：设置控件的绝对或相对位置。

PlayAction_MoveBy(uiName,elementName,moveX=0,moveY=0,duration = 1.0,fps = 50)：控件移动一定距离

PlayAction_ScaleTo(uiName,elementName,anchor = "center",scaleW=1.0,scaleH=1.0,duration = 1.0,fps = 50):控件缩放到指定大小

 SetRootRoundRectangle(canvas,hastitlebar,x1, y1, x2, y2, radius=25,**kwargs):使用TKinter方式设置窗口圆角

LoadDynamicColumn(uiName,listViewName):从数据库表字段查询结果更新列表字段

 

 

***\*Canvas控件上绘图的相关函数：\****

LoadCanvasRecord(uiName)：加载画布.cav文件

DoCanvasRecord(drawCanvas,shapeType,x,y,x2,y2,fillcolor,outlinecolor,fillwidth,dash1=0,dash2=0,newImage=None,text='',textFont = None,textColor='',shapeTag='')：执行.cav文件

DrawLine(uiName,drawCanvasName,x1,y1,x2,y2,color,width=1,dash=(0,0),shapeTag='')：在画布上画线

DrawArrow(uiName,drawCanvasName,x1,y1,x2,y2,color,width=1,dash=(0,0),shapeTag='')：在画布上画箭头

DrawTriangle(uiName,drawCanvasName,direction,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag='')：在画布上画三角形

DrawRectangle(uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag='')：在画布上显示矩形

DrawRoundedRectangle(uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),roundRadius=10,shapeTag='')：在画布上显示圆角矩形

DrawCircle(uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag='')：在画布上画圆

DrawDiamond(uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag='')：在画布上画菱形

DrawCylinder(uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag='')：在画布上画圆柱

DrawStar(uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag='')：在画布上画星星

DrawText(uiName,drawCanvasName,x,y,text,textFont=None,color='#FFFFFF',anchor='nw',shapeTag='')：在画布上写文字

DrawImage(uiName,drawCanvasName,x1,y1,x2,y2,imagefile,shapeTag='')：在画布上显示图片

DrawButton(uiName,drawCanvasName,x1,y1,x2,y2,text='',textcolor='#000000',textFont = None,fillcolor='#FFFFFF',outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag='')：在画布上绘制一个按钮。

EraserCanvas(uiName,drawCanvasName,x1,y1,x2,y2)：用背景色擦除画布上指定区域。

GetShapePoint(uiName,drawCanvasName,shapeTag,pointTag,absoluteMode=True)：获取图形上的绑定点位置

SetShapeRect(uiName,canvasName,shapeTag,x1,y1,x2,y2)：设置图形所在的区域位置

GetShapeRect(uiName,canvasName,shapeTag)：取得图形所在的区域位置

SetShapeFillColor(uiName,canvasName,shapeTag,color)：设置图形的填充色

GetShapeFillColor(uiName,canvasName,shapeTag)：取得图形的填充色

SetShapeOutlineColor(uiName,canvasName,shapeTag,color)：设置图形的边框色

GetShapeOutlineColor(uiName,canvasName,shapeTag)：取得图形的边框色

SetShapeLineWidth(uiName,canvasName,shapeTag,width)：设置图形的边框宽度

SetShapeImage(uiName,canvasName,shapeTag,imageFile)：设置图形的图片背景

GetShapeImage(uiName,canvasName,shapeTag)：取得图形的图片背景

SetShapeText(uiName,drawCanvasName,shapeTag,text,color = None)：修改图形文字内容

GetShapeText(uiName,drawCanvasName,shapeTag)：取得图形文字内容

BindShapeEvent_SetShapeRect(uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag,x,y,w,h)：绑定事件-设置图形位置与大小

BindShapeEvent_SetFillColor(uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag,color)：绑定事件-设置图形颜色

BindShapeEvent_SetOutlineColor(uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag,color)：绑定事件-设置图形边框颜色

BindShapeEvent_ChangeImage(uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag,ImageFile)：绑定事件-更换图形图片

BindShapeEvent_ChangeText(uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag,Text,TextColor)：绑定事件-设置图形文字

BindShapeEvent_JumpToUI(uiName,drawCanvasName,shapeTag,bindEvent,targetUIName)：绑定事件-跳转其它界面

BindShapeEvent_LoadUI(uiName,drawCanvasName,shapeTag,bindEvent,widgetName,targetUIName)：绑定事件-嵌入界面

BindShapeEvent_DeleteShape(uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag)：绑定事件-删除图形

BindShapeEvent_CallFunction(uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag,callBackFuncton,param = None)：绑定事件-调用函数

BindShapeMouseEvent(uiName,drawCanvasName,shapeTag,bindEvent,actionInfo)：对绑定事件进行处理

DeleteShape(uiName,drawCanvasName,shapeTag)：删除图形

ReDrawCanvasShape(uiName,canvasName)：重绘界面指定画布

ReDrawCanvasRecord(uiName,ForceReDraw=False)：重绘界面所有画布。

 

#### 三、**功能类：**

WindowDraggable：定义一个可拖拽移动和拖拽边框大小的窗口类。

DownLoadFileProgressDialog类：用于提供从网络下载的支持，可显示下载进度。

 

 
