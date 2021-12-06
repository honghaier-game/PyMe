

#####                                                                                                                                                                                 Focus on Tkinter desktop application software development, make everything simple!！

# **TKinterDesigner instructions**

| Author | Honghaier  |
| -------: | ---------- |
| Version | V1.6.3     |
| Last Update Date | 2021-12-05 |
| Twitter: | honghaier_2020@Honghaier_game |
| Email: | 285421210@qq.com |
| Twitter: | honghaier_2020@Honghaier_game |

WebSite:www.tkinterdesigner.com


GitHub: https://github.com/honghaier-game/TKinterDesigner.git 

## What is TKinterDesigner ？

Tkinder designer is a development tool based on python, which is used to develop Python application project based on tkinder interface. But the biggest difference between it and other types of development tools is that it provides a complete set of development process. At present, python does not lack the development ide. What it lacks is the reasonable and scientific development process, and what it lacks is the auxiliary tools to deal with a large number of modules. Tkinder designer is a solution for Python application software development, including the overall development process from project creation to interface design, to event logic editing and debugging, to package and release, as well as the resource platform and developer ecology established on this basis.



## What is the development process of TK inter designer?

​		![](http://www.tkinterdesigner.com/ReadMeImages_Cn/0.png)



## What are the functions of TK designer?

TkinderDesigner  includes the following ten main functions:



1. ###### Project management: create and open projects.

2. ###### File management: creating interface, creating files and importing project resources.

3. ###### Interface design: design Tkinter interface by dragging and dropping what you see is what you get.

4. ###### Control setting: set the basic properties of the control.

5. ###### Variable binding: binding custom variables for Tkinter controls.

6. ###### Event response: mapping between events and functions for Tkinter's control.

7. ###### Logic writing: write the logic code of event function.

8. ###### Debug and run: call Python command to debug and run the project.

9. ###### Package program: call Python command to package exe for the project.

10. ###### Componentization and user-defined module import: directly save the current interface functions as components and call them flexibly, or import and call user-defined modules.

    

## Tkinterdesigner startup:

Double click TK inter designer program to see a console interface. On this page, you can select the language in the upper right corner as needed. Here we choose Chinese. If our current version is not the latest version, we can see the prompt of the latest version. Click to open the download page of the latest version.

​		![](http://www.tkinterdesigner.com/ReadMeImages_Cn/1A.png)

By default, it is offline. If you need to use the membership and export functions, you can click the  guest  icon to log in.

## Tkinterdesigner registration and login:

Click the guest icon and you will see a login interface as follows.

​		![](http://www.tkinterdesigner.com/ReadMeImages_Cn/1.png)

After entering the account and password, click the "login" button to login. If there is no account, you can click "register“ Enter the registration interface, fill in the "account", "password", email and other information, and then click the "registration" button. After successful registration, you will automatically log in. If you don't want to register, you can also click "offline use".

​		![](http://www.tkinterdesigner.com/ReadMeImages_Cn/2.png)

After successful login, you will enter the project management page, where the login name will be displayed, and you will have more membership rights.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/3.png)



## Tkinterdesigner Function Description:

## 1. Project management:

The project management page provides five tabs for options:

### (1) New project:

Five template examples are provided, including blank interface project, dialog box project, single document project, multi document project and web crawler. You just need to select the corresponding project and click "OK" to complete the establishment of the project. If you need to change the project path, you can click change path to modify it.

#### <1> Empty interface project

If we select an empty interface, then click OK.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/57.png)

Let's select the dialog box item, and then click OK. In this main design interface, we can see that its layout is as follows:
（1） **Top main menu**：includes the main menu items of the software.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/128.png)

The first is common settings , which has four options:
**Python directory**  *: users who do not set the python directory to the system path need to set it correctly here to run and publish normally.
-***color scheme**  *: two color schemes, dark and light, are provided for users to choose. The default color is dark, which may be expanded as needed in the future.
-* **language**  *: provide simplified Chinese, traditional Chinese, English, Japanese, Korean five language support, follow-up expansion as needed.
-*  **border transparent color value** : it is used to set the transparent color value when the dialog box uses the border transparent color to hollow out the rounded corner when there is no title bar.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/129.png)Then there is the **design operation**  item.
-* **auto save** : you can set whether to save automatically or manually. The default is auto save, that is, every operation is saved. To save manually, you need to press Ctrl + s when you need to save.
-*  **number of operation records**  *: used to set the maximum number of steps that can be saved.
-* * **control drag mode**  *: in general, you can drag directly with the mouse, or you can select Ctrl + left mouse button to drag, but you can always use the middle mouse button to drag.
-* * **control scroll wheel zoom** : in general, drag and move directly with disposable mask, or select Ctrl + left mouse button to drag and move, but always support middle mouse button drag and move.

（2） **Shortcut buttons under the main menu**：the frame button can show or hide the frame structure tree, the run button can quickly run the project for testing, and the Publish button can package and publish the project as an EXE program. In addition, there are some common alignment settings, text font, foreground background color, image background shortcut buttons.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/132.png)



（3） **The leftmost project framework file tree**： includes a list of all the files in the project. Remember: you can also add a form interface, add a python file, or import a resource file through the right-click menu. If you are designing an interface, the frame structure tree will affect your viewing window space. You can click the frame button to show or hide it.
（4） **Control and module toolbar**：for the common controls needed in interface design, I list them here. Although not all, but with the update, I believe it will gradually enrich. Here, the module selection area is used to import custom modules. In the actual case project, there are some customized module classes and cases used in the project, such as' express' or 'chatServer'. You can take a look at it for a moment. It only needs certain design constraints.
（5） **Central design preview area**：the main visual area of interface design. Here you can drag, place, and stretch all the necessary interface controls. The generated interface is available.
（6） **List tree of all controls in the upper right corner of the current interface**：lists all controls in the current interface. You can click the corresponding tree item to select the corresponding control, or you can right-click the mouse to delete it in the pop-up menu.
（7） **Property list item of the currently selected control in the lower right corner**：lists all properties corresponding to the currently selected control. You can double-click the corresponding property item to modify it here.
（8） **Information text at the bottom**：displays the position and size information of the current control.

#### <2>."Dialog box" project

The "empty interface" project gives developers the simplest way to design the interface and project from scratch. However, if you want to develop a project based on other existing templates, you can return to the project management console by pressing the close button in the upper right corner, and then select the "dialog box" project template.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/59.png)

After successful creation, we will immediately enter a project with a simple dialog box.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/4.png)

In the "dialog box" project, we have carried out the basic simple interface design, and added the corresponding logic function to the button event. You can directly click "run" in the upper right corner to try it.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/58.png)

This is a simple example, but in most cases, it may be an example of high reuse rate.

#### <3>."Single document" project

Back to the console again, let's take a look at the template of an order document project

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/60.png)

After creation, we will see a single document Python editor project.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/61.png)

Run up, you can directly use it to write code.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/62.png)

In this project, you can see that it has a complete menu. How is this done?

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/64.png)

I explained this process in detail in the above screenshot. Once you have established the menu, TK inter designer will automatically create the corresponding response message function for you. You only need to write the specific logic code for the message function of the menu item in the corresponding cmd.py, so you can try more in the following projects.

#### <3>."Multi document" project

​		Back to the console, let's take a look at the multi document project template:

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/63.png)

​	Once created, we'll see a multi document Python editor project that uses split forms.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/65.png)

In this project, we have implemented split form and page embedding. You can use this function to make some independent interfaces and combine them into one interface by embedding. TK inter designer currently supports three embedding modes: frame, notebook and panedwindow. The frame is used to embed a page, the notebook is used to embed the corresponding page for each page, and the panedwindow is used to embed the corresponding page for the two parts of the partition. The operation only needs to set according to the corresponding properties.

In this example, we can see that when you click the tree item file on the left, the text box on the right will display the corresponding content, and you can run and print the python file results just like a single document.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/66.png)



### （2） Open project：

All the items we created will be displayed in this panel list. We just need to select the project we need and click "OK" to enter the project. The first button displayed as a plus sign is used to pop up the file browse dialog box to open items on the computer that are not in the list.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/70.png)

#### （3）Project example：

I provide some small cases as a reference, developers can open learning, so as to understand the framework and implementation of some similar small projects.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/6.png)

These cases include:

1. **Registration call**：demonstrates that another registration dialog box will pop up by clicking the button event in an interface.

   ![](http://www.tkinterdesigner.com/ReadMeImages_Cn/49.png)

2. **SQLite add, delete, query and change**：demonstrates how to add, delete, query and change SQLite, the database of Python.

   ![](http://www.tkinterdesigner.com/ReadMeImages_Cn/50.png)

3. **Embedded panel **：demonstrates how to embed other interfaces in Sketchpad canvas and tab notebook.

   ![](http://www.tkinterdesigner.com/ReadMeImages_Cn/51.png)

4. **Express query**：demonstrates how to use the self-designed module plug-in to complete the function of Express query and interface control interaction.

   ![](http://www.tkinterdesigner.com/ReadMeImages_Cn/52.png)

5. **Calculator**：demonstrates how to quickly develop a calculator software for addition, subtraction, multiplication and division.

   ![](http://www.tkinterdesigner.com/ReadMeImages_Cn/53.png)

6. **Network chat**：demonstrates how to develop a server and client chat program software with interface.

   ![](http://www.tkinterdesigner.com/ReadMeImages_Cn/54.png)

7. **Stock price query**：demonstrates how to call the stock query interface for stock query.

   ![](http://www.tkinterdesigner.com/ReadMeImages_Cn/55.png)

8. **Browser**：demonstrates how to develop your own browser software.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/56.png)

9. **web crawler **: demonstrates how to develop your own beauty crawler software.
![](http://www.tkinterdesigner.com/ReadMeImages_Cn/69.png)

10. **Pdf file merge**: demonstrates how to merge and split PDF files.
![](http://www.tkinterdesigner.com/ReadMeImages_Cn/300.png)

These examples are designed and developed with TK inter designer, which makes us feel proud. In the whole process, we don't spend much time on interface design and event processing, but only focus on the core function class to quickly complete the development of the project. Later, we will add more example projects to help you better learn and master TK inter designer.

​		

### 2. Document management

When we open the project example "calculator", we can see that the left most frame structure tree lists the files in the current project. There is a root node item named after the name of the project under the framework structure tree. There are five file items below:
1. Fun. Py: This is a public function library file, which provides access to controls and control variables and some common functions. It is not recommended to modify, so direct editing is not supported here.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/8.png)

2. ICO. PNG: This is the icon file of the project. It is generated when it is created. The premise is that there is an ICO directory in the directory of Tkinter designer. Here, because it is an example project, I changed ICO to an example.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/71.png)

3. JSQ. Py: This is the control layout Python file of the main interface of the project, which provides code support for the basic layout of the interface. Although it is a py file, when tkinterdesigner reads it, it will find that it is an interface file, and it will directly enter the design mode, because in the whole development section, it is generally not recommended that you handle the interface control layout Python file manually.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/72.png)

4.JSQ_ Cmd.py: the logic file of the main interface of the project, which provides code support for the logic of the interface. Here, we code the event function of the control and debug the breakpoint.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/73.png)

5.JSQ_ Sty.py: This is the style setting file of the project. It provides the style editing of the control. If you add a custom style here, you can directly set it to the control.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/74.png)


If we want to create multiple windows in the project, we can add a new interface to the framework tree. For example, we can open the new dialog interface project and right-click the frame tree on the left.

![](C:\Users\28542\Desktop\TKinterDesigner\9.png)

In the pop-up menu, click "new form". Here we can see a new pop-up dialog box. We can enter the name of the new form, and then click "OK".

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/10.png)

After clicking "OK", we will see a new window, including "Mywindow. Py" and "Mywindow_cmd. Py", corresponding to the form layout and logic implementation of Mywindow.
If you want to add your own logic code, you can right-click the pop-up menu item in the frame tree, click new file, and enter the name of the new file to create a new Python file.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/11.png)

After you click OK, you can see the new file code, and then you can start writing the code.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/12.png)

Sometimes, you may need some pictures, sounds, or other file resources to put into the project. You can also select and import them by right clicking the pop-up menu item in the frame tree and clicking import file
 	 Finally, if you want to delete one of the files, you need to right-click the corresponding file item, pop up the menu item, and click delete file. After confirmation, you can delete the file.

### 3. Interface design

First, we load the dialog project we created earlier.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/13.png)

Click project2 or project2. Py to enter the interface design area, and then start the interface design. For example, if you want to add gender option, occupation classification and married or not to the basic account and password input interface, you need to add some new controls, including two radio buttons and a combo box, a check button and the required label text. These are very common controls.
 	 We need to expand the main form because it's not big enough. At this point, you can click the control tree item "form" in the upper right corner_ You can also directly click the form interface in the design area. We can see a dotted line around the form and a gray drag block at the midpoint of the vertex and sideline. We can click the drag block in the lower right corner of the mouse and drag it to the appropriate size.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/14.png)

When finished, we can drag the "OK" and "exit" buttons directly to the lower right.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/15.png)

Now we can select and drag the desired control to the form from the toolbar list on the left.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/16.png)

**Remember this technique. If you need to create the same control repeatedly, you can directly select a control and drag it while holding down the ALT key. You can directly copy a new control for dragging, which is faster.**

If you feel that the position is not well aligned, you can select the "grid" and "suction" buttons in the shortcut keys, or you can quickly call "Ctrl + G" and "Ctrl + D" to display or cancel. The grid is 50 pixel units, which makes it easy for you to drag and align after inhaling.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/17.png)

​	

Select the label in front of the "gender" radio button, find the "text" attribute in the attribute box on the right, double-click the attribute, enter "gender" in the pop-up dialog box, and click "OK" to change the text of the corresponding label.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/18.png)

**Here's a trick, too. If you need to set the text of the label or button, when it is selected, you can first press Ctrl + backspace to clear the text, and then enter the text directly from the keyboard. **

So soon we finished all the tags, the text of the two radio buttons and the text of the check button.

It looks good, doesn't it? Of course, many properties can be set, such as background color, text color, font, etc. You can modify these operations in the property bar, or you can quickly adjust these operations through the shortcut button bar at the top.

Of course, gender cannot be both male and female. This bisexuality doesn't fit our orientation, does it? We choose the radio button with the word "female". In the group and value columns, double-click the value item, change it to 2 in the input box, and then click the button. Then we can see the correct radio button grouping.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/19.png)

There can be many radio buttons in an interface. Some of them may be a choice, such as gender, and some may be another choice, such as living in several areas of the city. These two parts need to be divided into two groups, and need to be distinguished by the unique value in each group. Therefore, when the two radio buttons representing "male" and "female" use the default group number of 1, you only need to change the value of the radio button corresponding to "Female" to 2.

Next, we add career options to the input. Select Combobox, find "items" in its property box, and double-click to edit the data item corresponding to Combobox in the pop-up dialog box in the data item editing area.

For example, if we enter three data, namely "programmer", "planner", "designer", and then click "OK", we can see that the combo box becomes the desired shape.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/20.png)

After clicking OK, the final result is as follows:

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/21.png)

OK, now we have finished the creation and placement of the required controls. All the controls are created into the interface by dragging. If you think the names of these controls in the upper right corner of the tree are not easy to remember, you can double-click the control tree item and modify it in the pop-up dialog box, You can also double-click the "name" attribute bar in the attribute box to modify it, or right-click the tree item to find the "modify" name menu item in the pop-up menu to modify it.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/87.png)

This completes the name modification.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/88.png)

​	**However, it should be noted that in TkinterDesigner, the newly modified name is an alias of the original name. In the following functions, you can either enter the original name or use the alias to find controls or set variables. However, for the sake of remembering, the user-defined name is preferred. Form_ As the root node of the form, 1 does not support modifying the alias.**

For example, you can use`Fun.GetElement(className,‘AccountEntry’)`  to get it, or`Fun.GetElement(className,‘Entry_3’)`  To get it, we give priority to the alias as the search keyword.

​	Now let's talk about how to add icons and menus to the window. The settings of the window are basically in the Form_ 1, we need to "Form_ 1 ", and then double-click the value of the" program icon "item in the property box. A dialog box for finding the icon will pop up. After selecting an icon, we will find that the icon in the window changes to the corresponding icon. This completes the icon setting.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/89.png)

To add a menu to an interface, double-click the blank value of the menu item in the property box to pop up a dialog box in the menu editing area. Then double-click the blank value of the menu item in the property box to pop up a dialog box in the menu editing area.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/90.png)

We can edit the menu in the dialog box of the menu editing area. First, add the top-level menu item, and then select the value of the menu item in the list box to add a submenu item or a sub separator line.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/91.png)

In this process, the menu is also added to the dialog box in the menu editing area in real time for preview. After adjustment, you can see the effect in the actual operation.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/92.png)

But how to respond? Once you decide to use the menu, the corresponding menu item response function will be generated in the corresponding cmd.py file of the interface. You can edit the code in the function.

​    ![](http://www.tkinterdesigner.com/ReadMeImages_Cn/93.png)

Click the "run" key, the design and code will be saved automatically, and the results will be displayed.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/94.png)

Let's introduce the properties of the control.

### 4. Control settings

The current control toolbar is divided into two parts

The first part is the controls, mainly the common controls on the interface. The second part is the module, mainly our own development of extension controls or some function module plug-ins.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/95.png)

In the controls page, we have listed a total of 18 kinds of controls. This number is not too complete, but it basically covers the controls commonly used by Tkinter. In the future, we will continue to follow up and develop new controls. We can click the control on the interface to see that a certain number of property values can be set in the property bar panel on the right, including the following aspects:



**Form property：**

- w,h:window size

- background: background color. Double click to open the color selection dialog box.

- image: background picture. Double click to open the select Picture dialog box.

- Title:the title text of the window.

- ICON:the icon of a program.

- ToolWindow:whether the window displays a title bar.

- Resizable:whether the window can be resized by edges.

- Drag border width:if there is no title bar, the width of the self generated drag border.

- Drag border color： if there is no title bar, the color of the self generated drag border.

- Theme style：whether to use theme skin.

- TopMost：whether the window is always in front.

- Transparent color value:  if you want to make a transparent window, the corresponding window hollowing color.

- Fillet radius：whether the edge has a fillet shape. If the radius value is set, the fillet will be formed at the corner with the radius value during operation.

  ![](http://www.tkinterdesigner.com/ReadMeImages_Cn/101.png)

**Label properties：**

- Layout: used to set the control layout. You can choose three layout modes: pack, grid and place.
- x,y,w,h:position, width and height in place mode.
- Background: background color. Double click to open the color selection dialog box.
- Text: the display text of the control.
- Font: displays the font of the text. Double click to open the font selection dialog box.
- Text color: displays the color of the text. Double click to open the color selection dialog box.
- Alignment: the alignment of text.
- Picture: can set the background image, double-click to pop up the select Picture dialog box.
- compand: if there are both text and pictures, how to shuffle.
- Styles: display styles of several borders.
- Status: there are several situations: (1) common, (2) not available, 
- Fillet radius: whether the edge has a fillet shape. If the radius value is set, the fillet will be formed at the corner with the radius value during operation.
- ![](http://www.tkinterdesigner.com/ReadMeImages_Cn/102.png)

**Button property：**

- ActiveTColor：the color of the text when the mouse passes by
- ActiveBGColor：the color of the background when the mouse passes by
- ![](http://www.tkinterdesigner.com/ReadMeImages_Cn/103.png)

**Entry属性：**

- showChar：for cryptographic entry, it can be set as a substitution character similar to *.
- ![](http://www.tkinterdesigner.com/ReadMeImages_Cn/104.png)

**Text属性：**

- VScroll bar: whether the scroll bar needs to be set.

- ![](http://www.tkinterdesigner.com/ReadMeImages_Cn/105.png)

  

**Listbox properties：**

- Selection mode: several common listbox selection modes, such as "Browse", "multiple" and "extended" (which are also multiple choices, but need to hold down shift key or Ctrl key or drag mouse at the same time)
- Data item: text item in list box.
- ![](http://www.tkinterdesigner.com/ReadMeImages_Cn/106.png)

**Combobx properties：**

- ![](http://www.tkinterdesigner.com/ReadMeImages_Cn/107.png)

​	

**RadioButton property：**

- Group: the group ID to which it belongs.
- Value: the feedback value when currently selected.
- ![](http://www.tkinterdesigner.com/ReadMeImages_Cn/108.png)

**Text property：**

- ![](http://www.tkinterdesigner.com/ReadMeImages_Cn/109.png)

  

**LabelFrame property：**

- ![](http://www.tkinterdesigner.com/ReadMeImages_Cn/110.png)



**Frame property：**

- Import interface: it is used to embed other interfaces. Double click to select py file of other interfaces to embed it into the current frame.
- ![](http://www.tkinterdesigner.com/ReadMeImages_Cn/111.png)

**Scale property：**

- Orient: horizontal or vertical.
- ShowVal：whether the current adjusted value is displayed.
- From,to:adjustable value range.
- Tickinterval:displays the interval of the scale.
- Resolution:the smallest unit of adjustment.
- ![](http://www.tkinterdesigner.com/ReadMeImages_Cn/112.png)



**Progress property：**

- Maximum value: the maximum value of the progress bar.
- Current value: the current progress value of the progress bar.
- ![](http://www.tkinterdesigner.com/ReadMeImages_Cn/113.png)



**Spinbox property：**

- From,to：adjustable range.

- Step：the numerical change of each adjustment.

- Data item: if you want to customize the interval value of spinbox, you can directly edit a data list here as the value item of spinbox.

- ![](http://www.tkinterdesigner.com/ReadMeImages_Cn/114.png)

  

**Treeview properties：**

- -The display type is tree by default. You can also choose "headings" so that it will be in the form of a data list, similar to the property panel.
  -Select mode: refer to Listbox  select mode
  -Column data. If you select "headings", you can edit column items for it here.
- ![](http://www.tkinterdesigner.com/ReadMeImages_Cn/116.png)
- ![](http://www.tkinterdesigner.com/ReadMeImages_Cn/117.png)
- ![](http://www.tkinterdesigner.com/ReadMeImages_Cn/118.png)
- 

**Canvas properties：**

- When you drag canvas to the design area, there will be a bar for drawing at the bottom, including empty, brush, line, arrow, short shape, circle, Pentagon, text, eraser, etc. after selecting the corresponding icon, you can draw freely on canvas.
- ![](http://www.tkinterdesigner.com/ReadMeImages_Cn/119.png)



**Notebook properties**

- Page: used to create each page for the current notebook and import the window to be embedded.
- ![](http://www.tkinterdesigner.com/ReadMeImages_Cn/120.png)



**Panedwindow property:**

- Drag:whether the splitter bar can be dragged determines whether the size of the two parts can be changed.
- Left interface: double click to import the interface py file embedded on the left.
- Right interface: double click to import the interface py file embedded on the right.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/121.png)



**Calendar properties：**

- Bar background and foreground: the background color and text color of the above column from Sunday to Saturday correspond to the black background and white text in the figure below.
- Select background and foreground: the change when you select a date with the mouse in the calendar control corresponds to the light green background and dark green text of July 3, 2021 in the following figure.
- ![](http://www.tkinterdesigner.com/ReadMeImages_Cn/122.png)



​	   These are all the properties of the basic control. If you have any questions, please email me 285421210@qq.com Or visit:www.tkinterdesigner.com 进行反馈.

​	   In addition, there are two built-in function modules in the corresponding module toolbar. Let's briefly talk about their properties. The way to create modules and set properties is the same as the way to drag controls into the interface.

**Datasource property:**this is a module used to obtain data from various data sources.

- Data type: it has a list showing all the available data sources. Just press the above selection, and then the corresponding data source properties will appear.
- ![](http://www.tkinterdesigner.com/ReadMeImages_Cn/123.png)

For example, select TXT here.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/124.png)

Click "run" to see that the contents of the txt file are output and displayed in the txt control.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/125.png)



***Videocapture property：**this is a control used to get video from the camera and output it to canvas.

- Canvas：output to the specified canvas control. You need to find a suitable canvas from the top right control tree item and drag it here to specify.
- ![](http://www.tkinterdesigner.com/ReadMeImages_Cn/126.png)

OK, it's done. You just need to click "run" to see the effect.

​	![](http://www.tkinterdesigner.com/ReadMeImages_Cn/127.png)

​	This is the power of TK inter designer. Drag and drop can quickly realize the interface and function.

### 5.Variable binding

​	In the development process, we often need to store some data, maybe just a simple result storage, maybe the input value of the control. For example, in the development of the instance project JSQ (calculator), we bound a temporary variable to store the intermediate value of the tag displaying the data, so as to add, subtract, multiply and divide. In the above example, suppose that when we click "OK" to judge that the account value is the same as the last input value, a dialog box will pop up to prompt "account used". We can add a custom variable to bind the account. This design idea is a reference to VC + +, if you have VC + + development experience, I believe you can quickly understand.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/23.png)

Right click the input box corresponding to the account and click "Data binding" in the pop-up menu. In the pop-up dialog box, we enter the name of the data item to be bound "NameArray", and select it as the "list" type. If we use numeric type or string type, we can see an option box "map to 'text'", clicking this option means that the variable will be updated to the text of the label or entry control, and the function will be activated. Call fun. 

```
SetUserData
```

 to set. Only one variable is allowed for the same control. If not selected, you can create multiple variables for the control. We don't need to click here.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/24.png)



​	After creation, there will be a binding list variable in the input box. You can use 

```
Fun.GetUserData(className,‘Entry_3’,’NameArray’)
```

get it。
    Next, let's make a judgment when we click the OK button, which requires adding a command event map to the OK button.

### 6. Event function mapping

The so-called "event function mapping" refers to the function mapping of events that can be bound to control, so that when the corresponding event is triggered, the set function is called.
Let's right-click the "OK" button and select "event response" from the pop-up menu.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/25.png)

In the pop-up event response processing edit area, you can see the event list on the left, which lists the common Python events. There is an input box on the right to display the default function name. We can also modify it. Click "Edit function" button or double-click the event item in the list to directly enter the code editing area of the logic file. At this point, we can see the added event response function, where we can edit the code manually.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/26.png)

For button control, we can also double-click the control to enter the corresponding "onCommand" function just like VC + +。

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/27.png)

If we want to call other interfaces in the event response, we can click on the "call the other interface" button, and then pop up an option dialog box to let us call it as needed.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/28.png)


Here you can directly select the most commonly used open and save file box, but if you create a multi window program, you need to call another window here. Just select "call other UI File" to find the PY file to call. I have a "calltest" project in the sample project to demonstrate this.

### 7. logic code writing

The button is in the code editing area of the logic file. In the "button_6_onCommand" function, we can write the following code:

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/29.png)

This code gets the list variables bound to the input box through 

```
Fun.GetUserData(uiName,elementName,dataName)
```

, and directly gets the current input value through 

```
Fun.GetText(uiName,elementName)
```

, and then compares them. If it is the same, the "name registered" dialog box will pop up. If they are different, the input value will be added to the list variable, and the registration success dialog box will pop up.

### 8. Commissioning and operation

If you want to run it immediately, you can directly click the "run" button in the upper right corner. The program code will be automatically saved and run. If there are errors in the code, they are displayed in the compile error message output window in the code area. If printing is added to this function, printing is also displayed in real time.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/30.png)

We enter the name in the account where the program is running. When we click "OK" for the first time, the dialog box of "successful registration" will pop up. Then click OK again to pop up the "name registered" dialog box.
We can still register successfully by changing our name. It seems that everything is as we expected.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/31.png)

如果我们想要调试，可以用鼠标在代码区行号条左边点击，为程序增加断点。

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/32.png)

​	After adding the breakpoint, you can click the small blue button in the debugging area below to start debugging.

​	![](http://www.tkinterdesigner.com/ReadMeImages_Cn/33.png)

In the screenshot above, we can see that once debug is started, after clicking the "OK" button,  The breakpoint is triggered in "Button_6_onCommand" and the arrow of the current execution line appears. At the same time, in the debugging panel below, there are two area information display, and the left is the local variable area. Here, you can see the local variable with the value of the current function. On the right is the output debug information

​	At this time, we can debug by clicking the shortcut button in the debug button bar. The specific instructions are as follows:

​	![](http://www.tkinterdesigner.com/ReadMeImages_Cn/34.png)

​    If you have debugging experience in VC + + or other programming ides, I believe you should know how to use them. Here is a tip: you can use the following shortcut keys to make quick commands in the current window:

​	1.F5: continue to execute until the next breakpoint, as well as the blue arrow when you directly click the breakpoint or debug line by line.

​    2.F9 : add a breakpoint for the current line.

​    3.F10 : execute the next line (if there is a function, do not enter the function)

​    4.F11 , execute the next line, if there is a function, enter the function.

### 9. Package exe

After completing our own program, we want to package the program as exe and publish it to users. We can directly click the "publish" button in the upper right corner, select the output directory, and then enter the name of the EXE to be packaged. But if you don't log in, you can't pack it.

​	![](http://www.tkinterdesigner.com/ReadMeImages_Cn/36.png)

Click the OK button and tkinder designer will start calling the packer to package the project.

​	![](http://www.tkinterdesigner.com/ReadMeImages_Cn/37.png)

如果进展顺利，您最终可以在输出目录中找到相应的exe程序：

​	![](http://www.tkinterdesigner.com/ReadMeImages_Cn/38.png)

### 10. Componentization and custom module import

Componentization is an indispensable means in the rapid development process. We can package all or part of the controls in the interface to generate a component at any time during the development process, and import and use it in the "interface" bar of the toolbar.

The method is to right-click the control tree item on the right, click componentization in the pop-up menu, then enter the component name in the pop-up dialog box, and click OK to generate the component.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/302.png)

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/303.png)

After generating the component, we can import and use it in other projects.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/304.png)

Drag the componentized interface to the current interface. It will exist as an independent control with the original logic.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/305.png)

When running, you will find that this method can greatly improve your development in the form of component, and make your engineering code very efficient and reusable.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/306.png)

Custom module is designed to enable developers to interact with controls through self-designed module classes and complete relatively independent functions. You can import module classes in the interface designer and easily set the properties of module classes, including passing interface controls to it as parameters. We hope to provide a large number of available modules for developers in the future. At present, we provide a few modules in the "ModuleMarket" to verify this scheme, but only if you register your account number can you see the component market.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/309.png)

we can see the components queried by express express. We can click Install. After installation, it will be placed in the market of the current tool Market_com directory

Its code is as follows：

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
    #Set Company ID
    def set_CompanyID(self,companyID):
        self.CompanyID = companyID
    #Get Company ID
    def get_CompanyID(self):
        return self.CompanyID
    #Set Express Number
    def set_ExpressNumber(self,expressNumber):
        self.ExpressNumber = expressNumber
    #Get Express Number
    def get_ExpressNumber(self):
        return self.ExpressNumber   
    #Set the ComboBox to get company name
    def set_ComboBox(self,comboBox):
        self.ComboBox = comboBox
        # These are some express company 's name.
        self.ComboBox['values'] = ['sentong','EMS','yuantong','shunfeng','yunda','zhongtong','tiantian','debang']
        self.ComboBox.current(4)
    #get the value of ComboBox
    def get_ComboBox(self,comboBox):
        return self.ComboBox   
    #Query result 
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

​	As we can see, the way to write custom module classes is to create a class and add set and get functions to properties that need to be exposed to the designer. In express class, we designed three variable functions, including the company ID and the express number of express company. We want to pass in a control combo box to accept the list of company names.

Now we create a blank project, and then we right-click the left project2 tree item, and select import resource in the pop-up menu, and then we will market_ Express.py in com is imported.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/40.png)

In the main interface design area, we quickly build the interface by dragging and dropping controls

![](C:\Users\28542\Desktop\TKinterDesigner\41.png)

Now that we have finished designing the interface, we will switch to the "module" page of the toolbar. On the module page, click the import module button, and then find express. Click "open". In fact, "express. Py" does not have to be in the current directory. The first mock exam is that you can use a module for multiple projects, and you need to import it here without creating module classes for each item used for the same module.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/42.png)

好的，现在express模块项出现在模块面板上，让我们把它拖到界面上。

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/43.png)

We can see that in the property box in the lower right corner, three variables of the express module are displayed in the property box. We can set "company Id" and "express number" manually, but how to set combobox? Here, you just need to find the corresponding combobox in the control tree in the upper right corner, and then drag it to the value item position of "combobox" in the property box. Then we add the command response function to the "query" button.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/46.png)

In the "Button_7_oncommand" function, we can write the corresponding code:

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/47.png)


​    

This part of the code implements the_ 5 to obtain the logistics order number, and through our module name "Express"_ 9 " call 

```
Fun.GetElement
```

to get the Express module, and use the same method to get Listbox, then call Express's function 

`set_ExpressNumber` 

sets the express number, and finally calls the query method to query. The parameter is the listbox object that is displayed.
When finished, click "run" in the upper right corner to run it. We can see the program running. Try to enter the number in the express order number, click "query", and you will soon see the express information displayed in the list box.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/48.png)

​	这就是在设计区加入自己编写的模块并调用的实例，如果你觉得代码写起来麻烦，也可以直接查看案例工程中的快递查询案例进行学习。

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/45.png)



## About beautification: apply skin and custom control style.

In most cases, the program we use Tkinter to create is not beautiful enough. Although it does not affect the function development, everyone has a love for beauty. It's best if we can make the program more beautiful. However, since most of our developers and users are programmers, it's best to simplify the beautification part. Therefore, I hope to provide a good color scheme as a skin for developers to make the program more beautiful. Therefore, we also launched the skin market, with only official skin for the time being, In the future, we will open up to the majority of developers and users to upload and submit, so as to provide better skin for everyone. But the premise is that you have to register an account to see the component market.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/310.png)

​	We can click the "not installed" text on the "black gold theme" icon here to complete the installation.

​	Then we try to open the instance project "calculator", which we can use in the Form_1, click the drop-down list, then we can see a "BLACKGOLD. Py", which is the black gold skin.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/76.png)

We select it and run the program. You'll see a cool calculator program with a dark gray background, dark gold text and sharp contrast edges.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/77.png)

Of course, if you want to modify your style yourself, you can also make it in sty.py, such as the registration applet project we created before we open again.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/78.png)

Click "Project1_sty.py "to enter the style editor.

![](C:\Users\28542\Desktop\TKinterDesigner\79.png)

​	In this interface, we enter "My" in the style name, select "TForm" in the corresponding control list, and click the "Add New Style" button.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/84.png)

enter "My" in the style name, select  "TLabel" in the control Type  list, click the "Add New Style" button, and set colors for the two key values "background" and "foreground".

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/85.png)

In the same way, we create the style of other controls.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/86.png)

 	 After that, we can go back to the design area and right-click the dialog box, edit box, radio button and combo box. In the pop-up menu, there will be a "style selection" item. We can select the corresponding style.![](http://www.tkinterdesigner.com/ReadMeImages_Cn/82.png)

​	After you style all the controls, it looks like this.

![](http://www.tkinterdesigner.com/ReadMeImages_Cn/83.png)

​	About the skin style, it shows that there are some bugs, which need to be improved. This part only explains how to use.

### About me

Online name: honghaier

Nationality: China

Skills: C +, game development

Self assessment: programmer, developer, entrepreneur

### Speech:

As you can see here, I believe the readers have worked very hard. In the process of compiling the tutorial, I am still changing the bug. Maybe some screenshots will be slightly different from the actual version, but they are generally consistent. I hope interested Python fans can communicate with me and give me more suggestions. I hope Python can get better and better.
 		 Finally, I wish you all the best in your work and good health~

​                                                                                                           Honghaier

​																											2021/12/05

