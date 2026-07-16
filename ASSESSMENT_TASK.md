# Assessment Task — Restaurant Ordering Chat Bot

## Task Description

It's simple. You are to create your very own chatbot!

The aim here is to have a functioning bot written in Python. You will need to include features such as **Fuzzy Logic**, **Natural Language Processing**, **Text to Speech** and **Speech Recognition**.

### Business Requirements Brief

You are to create a **Restaurant Online Take Away Ordering Service Chat Bot**, named by the type of food your restaurant serves.

- Choose a **Theme** — e.g. Vietnamese Food → call yours *VietnamBot*.

You need to:

- **Identify a Customer** — new or existing (in database)
- **Interact with the Customer** to:
  - View order history
  - View Menus
  - Order food
  - Exit

To facilitate usability and accessibility, your chat bot must have a **Voice interface** for Users and a more **Natural Conversation / Logic Flow**, and must be able to **handle fuzzy input**.

The application must be designed to **simplify maintenance and re-usability**.

### Technical Requirements

- You must follow the **Object Oriented Paradigm** — preferably in Python.
- You must persist data in a **Relational Database** (e.g. SQLite).
  - [Python SQLite — GeeksforGeeks](https://www.geeksforgeeks.org/python-sqlite/)
- You must create Classes following the **Facade Pattern**.
  - [Design Patterns in Python: Facade](https://medium.com/@amirm.lavasani/design-patterns-in-python-facade-0043afc9aa4a)
  - [Facade Method — Python Design Patterns (GeeksforGeeks)](https://www.geeksforgeeks.org/facade-method-python-design-patterns/)

### Documentation Requirements

**Project Portfolio** — use the provided Template file as a starter for your Portfolio (`Task 2 Major Project Portfolio Template.docx`).

You must document the **Requirements** of the System:

- Create a **UML Use Case Diagram** showing the interactions between the external user and the system functions.
  - [UML Use Case Diagram (Lucidchart)](https://www.lucidchart.com/pages/uml-use-case-diagram)
- Create a **Data Flow Diagram** showing the flows of data between the external user and the system functions.
  - [Data Flow Diagram (Lucidchart)](https://www.lucidchart.com/pages/data-flow-diagram)

You must document the **design** of the system using the following:

- Produce a **UML Component Diagram** that reflects the Menu Component and the Customer & Orders Component.
  - [UML Component Diagram (Lucidchart)](https://www.lucidchart.com/pages/uml-component-diagram)
- Produce a **UML Class Diagram** that reflects the Classes identified for each component and any relevant Associations between these classes.
  - [Introduction to Class Diagrams (Lucidchart)](https://www.lucidchart.com/blog/introduction-to-class-diagrams)
  - [The Class Diagram (IBM Developer)](https://developer.ibm.com/articles/the-class-diagram/)
- Include a **Database Schema diagram & Data Dictionary** to reflect the database structures that support this application.

---

## Task Details

It's simple. You are to create your very own chatbot!

The aim here is to have a functioning bot written in Python. You will need to install additional modules to handle **Fuzzy Logic**, **Natural Language Processing**, **Text to Speech** and **Speech Recognition**.

## Functional Requirements (Use Case Descriptions)

A **Use Case** describes how the system will be used by the User / Actors.

- Convert the following Functional Requirements into appropriate Use Cases.
- The requirement descriptions below need to be gathered and given appropriate Use Case names and descriptions.
- Produce a **Use Case Diagram** that graphically represents the Use Case Descriptions.

### Introduction

- You are to create a Restaurant Online Take Away Ordering Service Chat Bot named by the type of food your restaurant serves (e.g. Vietnamese Food → *VietnamBot*).
- On startup, your application must **identify itself by name** and **welcome the customer** in a polite way.

### Customer Identification and Greeting

- You must be able to identify each customer by asking their **username and password** (typed in for accuracy).
- If they are **existing Customers** (in Offline Storage), then, by name:
  - Welcome them **back**.
- **Otherwise** (new customer):
  - Ask for them to enter their password, and then their **first and last names separately** (typed in to preserve correct spelling).
  - Store the new Customer back to offline storage.
  - Welcome them to the service.
- You must be able to **store orders for a particular customer username** — using **order numbers** to differentiate between each order the customer made.

### Customer Actions

Once logged in, the main actions the customer is allowed to do are:

- Order food
- View previous orders
- See the menu
- Exit the system

### For Viewing Previous Orders

You must allow the customer to access their previous orders, including:

- Order number
- Order Date
- The Meals / Dishes ordered and their prices (at that point in time)
- Total order value

### For Viewing the Menu

- You must allow the customer to request a description of the menus for **3 different courses** — e.g. starter, main and dessert.
- They may see the dishes for **one course only** or for **all courses**.
- You must include a **price for each dish** in that course.

### For Ordering Food

- You must allow the customer to order food from each of the courses.
- Each order must have a **minimum of 3 different dishes / meals** in order to proceed to checkout.
- For the chosen Meal, the Customer is asked **how many servings** of that meal are required.
- If fewer than 3 different dishes are ordered, then the order **cannot be saved**.
- They may leave ordering at any time and **abandon the order** — please **confirm** they really want to do this.
- If **3 or more** different dishes are ordered, they may continue ordering or finish ordering.

During the order process, the customer should be able to:

- Request to access the menu again
- Abandon the order
- View the basket
- Finalise their order

On completion of ordering / checkout:

- You must **summarise the order** when they have completed ordering:
  - What dishes they ordered, the price and quantity, and the total cost for each dish
  - Total order cost
- Then ask them for **confirmation to proceed** to store the order.
- Once confirmed, the order is to be **saved to the customer account**:
  - Order number
  - Dishes and Prices
  - Total cost

### For Exit

- Thank the customer **by name** and wish them well, and ask them to come back again another time in a polite way.

## Non-Functional Requirements

- Your chat bot must have a **Natural Conversation / Logic Flow** and must be able to **handle fuzzy input**.
  - That is, do **not** use codes or numbers to identify things — e.g. *M for Menu*.
  - Allow different **synonyms** to perform the same action — e.g. to leave, the user can request to "Finish" or "Exit" or "Leave" etc.
  - Instead, it should be — *"I would like to see the Menu, please"* or *"I would like to order some food"*.
- Include **Voice Interaction** with the Application:
  - This provides a more user-friendly and accessible interface.
  - Use **Text to Speech** and **Speech Recognition** to get and display information to the user — where appropriate.
  - **Note:** You may support the spoken language with printed text at the same time.
  - Some information like **names** may need to be **typed** in, as speech recognition will struggle with spelling.
- Information must **persist over different sessions**:
  - Store Menu and Food Orders in offline storage — either a **JSON file** or **SQLite Database**.

### Maintainability and Re-usability

To allow the Application to be maintainable and re-usable:

- Write your code using **Python and Object-Oriented techniques**.
- Use a **Facade pattern** and structure your code in **Components**.
  - Facades enable us to encapsulate the Component functionality by providing a clear Facade/API Class that "hides the implementation of that functionality".
  - e.g. *View Menu* calls the *Menu* Class, which does what it needs with the *Course* and *Meal* classes to return the Menu in a user-friendly presentation.
- Use **Inheritance** to store common functionality in Parent Classes.
- For maintainability, **comment your code** to explain:
  1. Main functions of the code — i.e. use comments or docstrings.
  2. Any complex or unusual processing — i.e. use ad-hoc comments.
  3. Use meaningful variable / class / function names that relate to their purpose — i.e. intrinsic documentation.
