# 

# **TKinterDesigner Instruction**

| Author | Honghaier  |
| -------: | ---------- |
| Version | V1.4.8     |
| Last Update Date | 2021-06-17 |
| Twitter: | honghaier_2020@Honghaier_game |
| Email: | 285421210@qq.com |
| QQ Group | 100180960 |

WebSite:www.tkinterdesigner.com


GitHub: https://github.com/honghaier-game/TKinterDesigner.git 

## What's TKinterDesigner ？

​	Tkinterdesigner is a development tool based on python, which is used to develop Python application projects based on tkinter interface.

## What are the functions of TKinterDesigner ?

Tkinterdesigner v1.4.4 currently includes the following nine functions:



1. ###### project management: create and open the project.

2. ###### file management: create forms, create files and import resources for projects.

3. ###### interface design: design Tkinter interface.

4. ###### control settings: basic attribute editing is performed for the control.

5. ###### variable binding: bind variables for Tkinter control.

6. ###### event response: establish the mapping between events and functions for the control of Tkinter.

7. ###### logic writing: logical processing of event functions.

8. ###### compile and run: call Python command to compile and run the project.

9. ###### package exe: call Python command to package exe for the project.

10. ###### custom module import: import and call the customized module.



## TK designer function explanation:

### 1. Project management:

​		Double click to start tkinterdesigner.exe. The first step is to enter the project management interface. You can select the language according to your needs in the upper right corner. Here we choose English.

![](http://www.tkinterdesigner.com/ReadMeImages/1.png)

In this interface, I provide 5 tabs for options:

(1) New Project:Five templates are provided, including blank interface project, dialog box project, single document project, multi document project and web crawler. You only need to select the corresponding project and click "OK" to complete the establishment of a project. If you need to change the project path, you can click "change path" to modify it.

![](http://www.tkinterdesigner.com/ReadMeImages/2.png)

Here we select the dialog interface item, and then click "OK".
After the project is successfully created, we will immediately enter the main design interface for project development. We can return to the project management console through the close button in the upper right corner.

![](http://www.tkinterdesigner.com/ReadMeImages/3.png)

(2) Open project: all the projects we created will be displayed in this panel list. We just need to select the project we need and click "OK" to enter the project. The first button displayed as a plus sign is used to open an item that is not in the list.

![](http://www.tkinterdesigner.com/ReadMeImages/4.png)

(3) Example project: I provide some small cases as a reference, developers can open to learn, so as to understand the framework and implementation of some similar small projects.

![](http://www.tkinterdesigner.com/ReadMeImages/5.png)

For example, if we select the fourth item "calculator" and click "OK", you will see a calculator interface item:

![](http://www.tkinterdesigner.com/ReadMeImages/6.png)

In this main design interface, we can see that its layout is:

(1) The top main menu: 1. view: including grid and adsorption functions used in design. You can also call it quickly through Ctrl + G and Ctrl + D. 2. help: some useless information, if you need to find me, please take a look.

(2) Shortcut button under the main menu: frame button can display or hide frame structure tree, run button can run project quickly for testing, and Publish button can be used to package and publish project as an EXE program. Besides, there are some common text, color and alignment settings shortcut buttons, I believe you can know how they use it without explaining it.

(3) The leftmost framework tree: including a list of all files in the project. Remember: you can also add a form interface, add a python file, or import a resource file through the menu that pops up by right clicking on it. If you are designing the interface, the frame structure tree will affect your viewing window space, you can click the frame button to display or hide it.

(4) Control and module list selection area on the left: for the common controls needed in interface design, I have listed them here. Although not all, with the update, I believe that it will be enriched gradually. Here, the module selection area is used to import a customized module. In the actual case project, there are some customized module classes and the cases used in the project, For example, ‘Express’ or ‘ChatServer’, you can take a look at it a little, it only needs to have certain design constraints. I will detail the functions in part seven.

(5) Central design preview area: the main visual area of interface design. You can drag in and put and stretch all the required interface controls here. The resulting interface is available.

(6) List tree of all controls in the upper right part of the current interface: list all the controls in the current interface. You can click the corresponding tree item to select the corresponding control, or delete it in the pop-up menu by right clicking the mouse.

(7) The property list item of the currently selected control in the lower right part: lists all the properties corresponding to the currently selected control. You can double-click the corresponding property item to modify it here.

(8) Information text at the bottom: displays the position and size information of the current control.

### 2. Files management

The leftmost frame structure tree lists the files in the current project. Taking the dialog box project as an example, we can see that there is a root node item named by the project name under the frame structure tree, and there are five file items under it
1. Fun. Py: This is a common function library file, which provides access to controls and control variables.
2. ICO. PNG: This is the icon file of the project, which is generated at the time of creation, provided that there is an ICO directory in the directory of your tkinder designer.
3. JSQ. Py: This is the python file of the main interface of the project, providing code support for the basic layout of the interface.
4.JSQ_ Cmd.py: This is the logic file of the main interface of the project, which provides code support for the logic of the interface. The event function of the control is mainly coded here.
5.JSQ_ Sty.py: This is the style setting file of the project. It provides the style setting of TTK. If you add a custom style here, you can set the control.

![](http://www.tkinterdesigner.com/ReadMeImages/7.png)

When we click on “Fun. Py” or “JSQ_cmd.py”, the main view area becomes the code area:
 	 Because the software is designed to use the form designer instead of modifying the code of the form interface, when you click “JSQ.py”, the main view displays the interface. For the logic code and function library code, it is hoped that developers can write, modify and debug more logic code. Therefore, a code text area and an information output window are displayed, It is convenient to modify the code at any time and view the output at compile run time.
 	 If we want to create multiple windows in the project, we can add a new interface in the frame structure tree. For example, we can open the newly created dialog box interface project and right-click on the frame structure tree on the left.

![](http://www.tkinterdesigner.com/ReadMeImages/8.png)

​	In the pop-up menu, click "New form", here we can see a new pop-up dialog box, we can enter the name of the new form, and then click "OK".

![](http://www.tkinterdesigner.com/ReadMeImages/9.png)

​		 After clicking "OK", we can see a new window, including “Mywindow.py” and “Mywindow_cmd.py” Two files,  correspond to the form layout and logic implementation of mywindow respectively.
 	 If we want to add our own logic code, we can right-click the pop-up menu item in the framework tree, click "New file", enter the name of the new file, and we can create a new Python file.

![](http://www.tkinterdesigner.com/ReadMeImages/10.png)

After clicking "OK", you can see the new file code, and then you can start to write the code. 

![](http://www.tkinterdesigner.com/ReadMeImages/11.png)

​    Sometimes, you may need some pictures, sounds, or other file resources to put into the project. You can also select and import them by right clicking the pop-up menu item in the frame structure tree and clicking "import File".

​	Finally, if you want to delete one of the files, you need to right-click the corresponding file item to pop up the menu item and click "delete File". After confirmation, you can delete the file.

### 3. UI design

​	First, we load the dialog project we created earlier.

![](http://www.tkinterdesigner.com/ReadMeImages/12.png)

   We click project1 or project1.py to enter the interface design area, and then we can start the interface design. For example, if we want to add gender options, occupation classification, and married or not to the basic account and password input interface, we need to add some new controls, including two RadioButtons and a Combobox, A Checkbutton and the required label text. These are very common controls.

​	we need to expand the main form, because its size is not enough. At this time, you can click the control tree item "Form_1" in the upper right corner, or directly click the form interface in the design area, we can see that dotted lines appear around the form, and a gray drag block appears at the midpoint of the vertex and sideline. We can click the drag block in the lower right corner of the mouse and drag it to the appropriate size.

![](http://www.tkinterdesigner.com/ReadMeImages/13.png)

​	When we're done, we can drag the OK and exit buttons directly to the right Down location.

![](http://www.tkinterdesigner.com/ReadMeImages/14.png)

​	Now we can select and drag the required controls from the list of Tool Bar on the left to the form.

![](http://www.tkinterdesigner.com/ReadMeImages/15.png)

**Here's a skill. If you need to create the same control repeatedly, you can directly select a control and drag it with the  state of pressing ALT key. You can directly copy a control for you to drag.**

If you feel that the position is not well aligned, you can select the "grid" and "suction" buttons in the shortcut button, or you can quickly call the display or cancel through key 'Ctrl + G', 'Ctrl + D'. the grid is every 10 pixel unit, which is convenient for you to drag and align after suction.

![](http://www.tkinterdesigner.com/ReadMeImages/16.png)

OK, now that we have finished creating the required control, is it very simple?
Let's set these controls below.

### 4. Control settings

Select the label before the gender radio button, then we can find the "text" attribute in the attribute box on the right, double-click it, enter "gender" in the pop-up dialog box, and click "OK" to change the text of the corresponding label.

![](http://www.tkinterdesigner.com/ReadMeImages/17.png)

**Here's a skill. If you need to set the text of label or button,you actually press key when it focused ,then you can see the Input String Dialog .**	

​    So, soon we finished all the label, the text of the two RadioButtons and the text of the Checkbutton.

​	It looks good, doesn't it? Of course, you can set a lot of properties, such as you can modify the background color and text color, you can also modify the font and so on. You can modify these operations in the property bar, or you can quickly adjust them through the shortcut button bar at the top

​	Of course, gender can't be male and female at the same time. Such bisexual is not in line with our orientation, right? We select the radio button with the word "Female". In the column of grouping and value, double-click the value item, change it to 2 in the input box, and then click the button. Then we can see the correct radio button grouping.



![](http://www.tkinterdesigner.com/ReadMeImages/18.png)



​	There can be many RadioButtons in one interface. Some of them may be for one option, such as gender, and some for another option, such as living in several areas of the city. These two parts need to be grouped into two groups, and they need to be distinguished by unique values in each group. Therefore, when the two radio buttons representing "male" and "female" use the default group number of 1, you only need to change the value of RadioButton corresponding to "female" to 2.

Next, we add career options for input. We select Combobox, find "Items" in its property box, and double-click to edit the corresponding data item of Combobox in the pop-up dialog box of data item editing area.

 For example, we input three data, namely "programmer", "planner", "designer", and click "OK", and we can see Combobox become the desired shape.

![](http://www.tkinterdesigner.com/ReadMeImages/19.png)

After clicking OK, the final result is like this：

![](http://www.tkinterdesigner.com/ReadMeImages/20.png)

​	Click "Run" or press F5, which will automatically save the design and code, and compile the run results.

![](http://www.tkinterdesigner.com/ReadMeImages/21.png)

​	This example demonstrates the property design and use of several common controls. You can try other controls by yourself, which will not be repeated here. If you have problems,please send mail to me :285421210@qq.com or visit :www.tkinterdesigner.com to submit.

### 5. Variable binding

​	In the development, we often need to store some data, maybe it's just a simple result storage, maybe it's the input value of the control. For example, in the development of instance project  JSQ(means "Calculator"), we bind a temporary variable to store the intermediate value for the label displaying the data, so as to facilitate the operation of addition, subtraction, multiplication and division. In the above example, suppose that when we click "OK" to judge that the account value is the same as the last input value, we will pop up a dialog box to prompt "account used". We can add a custom variable to bind the account. This design idea is a reference to VC + +, if you have VC + + development experience, want to letter can quickly understand.

![](http://www.tkinterdesigner.com/ReadMeImages/22.png)

​	Right click the input box corresponding to the account, and click "variable binding" in the pop-up menu. In the pop-up dialog box, we enter the name of the data item to be bound "NameArray" and select it as "List" type. If we use number type or string type, we can see an option box of "mapping to 'text'", Clicking this option means that the variable will be updated to the text of the label or entry control at the same time when the function fun. Setuidata is called for setting. Only one variable is allowed for the same control. If this item is not selected, you can create multiple variables for a control. We don't need to click here.

![](http://www.tkinterdesigner.com/ReadMeImages/23.png)



​	After creation, there will be a binding list variable in the input box. You can use `Fun.getUIData(className,‘Entry_3’,’NameArray’)`  Get it at any time.
Next, let's make relevant judgments when we click the "OK" button, which requires adding a command event mapping for the "OK" button.

### 6. Event function mapping

​     The so-called "event function mapping" is to make a function mapping for the event that can be bound to control, so that when the corresponding event is triggered, the set function will be called.
 	 We right-click the "OK" button and select "event response" in the pop-up menu.

![](http://www.tkinterdesigner.com/ReadMeImages/24.png)

​    In the pop-up event response processing editing area, we can see an event list on the left, listing common Python events. On the right, there is an input box, displaying the default function name. We can also modify it. Click "Edit function code" to directly enter the code editing area of the logic file. At this time, We can see the added event response function, where we can edit the code manually.

![](http://www.tkinterdesigner.com/ReadMeImages/25.png)

​      For the button, you can also double-click it directly like VC + + to enter the command function.

![](http://www.tkinterdesigner.com/ReadMeImages/26.png)

​	If we want to call other interfaces in the event response, we can also click the "call other interfaces" button, and an option dialog box will pop up for us to call as needed.

![](http://www.tkinterdesigner.com/ReadMeImages/27.png)


​	The most commonly used open and save file box can be directly selected here, but if you create a multi window program, you need to call another window here, just select "call custom interface" to find its py file to call. I have a "calltest" project in the example projects to demonstrate this.

### 7. Logic code writing

​	Button in the code editing area of the logic file , In the `Button_6_oncommand` Function, we can write the following code:

![](http://www.tkinterdesigner.com/ReadMeImages/28.png)

​    This code obtains the list variables bound to the input box through `Fun.GetUIData`, and directly obtains the current input value through `Fun.GetUIText`, and then compares them. If they are the same, a dialog box "name has been registered" will pop up. If they are different, the input value will be added to the list variables, and a dialog box "Registration succeeded" will pop up.

### 8. Compile and run

​	If you want to compile and run immediately, you can directly press F5 or click the "run F5" button on the top right. The program code will be saved automatically and start to compile and run. If there is an error in the code, it will be displayed in the compile error information output window in the code area. If you add print to the function, it will also be displayed in real time.

![](http://www.tkinterdesigner.com/ReadMeImages/29.png)

​	We input the name in the account of the running program, and the first time we click "OK", the "registration success" dialog box will pop up. Then we click OK again, and the "name has been registered" dialog box will pop up.
 	 We can still register successfully by changing our name. It seems that everything is the same as we expected.



![](http://www.tkinterdesigner.com/ReadMeImages/30.png)

​	

### 9. Package exe

​	After completing our own program, we hope to package the program as an EXE and publish it to users. We can directly click the "publish" button on the top right, select the output directory, and then enter the name of the EXE to be packaged.



![](http://www.tkinterdesigner.com/ReadMeImages/31.png)

Click the "OK" button, tkinterdesigner will start to call the packer to package the project.

![](http://www.tkinterdesigner.com/ReadMeImages/32.png)

If it goes well, you can finally find the corresponding exe program in the output directory:

![](http://www.tkinterdesigner.com/ReadMeImages/33.png)

### 10. Custom module import

I put the custom module at the end because you don't have to use it, but it can easily extend your project. I'm in the example project "express"," It is used in both query and server.

![](http://www.tkinterdesigner.com/ReadMeImages/34.png)

 In short, you can write a custom module class for multiple projects to use. You can easily set the properties of the module class in the designer, including throwing the interface control as a parameter to it.
 We take the project express as an example_ Query development process for a simple explanation.
 First, we need to create a blank project, right-click on the tree item of the framework file, create a python file in the pop-up menu, and then name it "Express. py" . In this file, we need to create an express class to query the express results by keywords. The complete code of this class is as follows:

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


 There is only one way to write a custom module class: if you want to pass parameters to it in the designer, you need to use set_ And get_ Variable access method for prefix. So we design the function of three variables, including the company ID of express company, express number, and we want to pass in a control ComboBox to accept the list of company names.
 If you find it inconvenient to write the current project code, you can also use vscode or your favorite code editor to write the code, or directly import or copy "Express. py" from the instance project.

Anyway, you just have this code.

Back to the main interface design area, quickly build an interface:

![](http://www.tkinterdesigner.com/ReadMeImages/35.png)

​	Now that we have finished the design of the interface, we will switch to the 'Mod' page  of the toolbar. In the "Mod" Page, we click the "import module" button, then find "Express. py" and click "open". In fact, "Express.py" does not have to be in the current directory. You can use one module for multiple projects, and you only need to import it here, and you don't need to create a module class file for every project that you use to the same module.

![](http://www.tkinterdesigner.com/ReadMeImages/36.png)

​	OK, now that the express module item appears on the module panel, let's drag it to the interface.

![](http://www.tkinterdesigner.com/ReadMeImages/37.png)

​    We can see that in the property box in the lower right part, three variables of the express module are displayed in the property box. We can set the "CompanyID" and "ExpressNumber" manually, but how to set the combobox? Here, you only need to find the corresponding combobox in the upper right control tree, and drag to the value item position of "Combobox" in the property box.

![](http://www.tkinterdesigner.com/ReadMeImages/38.png)

Then we add the command response function to the "query" button.

![](http://www.tkinterdesigner.com/ReadMeImages/39.png)

On "Button_ 8_ oncommand" function, we can write the corresponding code:

![](http://www.tkinterdesigner.com/ReadMeImages/40.png)


​    

This part of the code implements get ExpressNumber from the entry_ 5, and through the our moudle name "Express_ 9 " call `Fun.GetUIEle` to get the express module,and use the same method to get the Listbox  then called the function of the Express. `set_ExpressNumber` set the express number, and finally call the Query method to query. The parameter is the ListBox object that is displayed.

​     There are so many codes. After we finish, press F5 to run it. We can see the running program. After trying to enter the number in the express order number, click "query", and we can see the express information displayed in the list box soon.

 ![](http://www.tkinterdesigner.com/ReadMeImages/41.png)

​	This is how to use the custom module.

### About Me

Online name: honghaier
Country: China
Skills: C + +, game development
Self Description: programmer, technologist, entrepreneur

### About  TKinterDesigner 

Because I have been using VC + + for more than ten years, when I use Python to develop software, I hope to build the interface quickly, but I'm just lazy and don't want to learn more. I'll continue to improve it. I hope interested Python fans can communicate with me and give me more suggestions, because I haven't finished reading a python book and I don't know too many requirements, However, I am optimistic about Python's requirements for interface tools in rapid prototyping, and hope that Python will become better and better.
 	 Finally, I wish you all the best in your work and good health~

​                                                                                                           Honghaier

​																											2021/06/09

