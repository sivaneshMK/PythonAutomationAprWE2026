APIs are methods

WebDriver methods

    get
    title
    current_url
    switch_to
    window_handle
    get_window_handles
    find_element
    find_elements
    back
    forword
    refresh

WebElement methods

    send_keys --> is a webelement type method it is used to enter text on text box and password text box, multi line text box
    click --> will perform click operation on button, radio button, link, check box etc.
    clear --> will clear the existing value from the text box
    text --> get the text of elements
    get_attribute -->
    is_selected --> is a webelement type method and it is used to check the radio button or check box is selected 
                    if it is selected it will return true else it will return false
    is_displayed
    is_enabled
//span[text()='Log on']/parent::button

//label[@class='checkbox_container']/input
//div[@class='rememberMeDiv']//input

XPATH
---------
/ --> immediate child
//--> any child including immediate and grand child
    
Actions
-----------
Drag and drop
mouse over --> move_to_element
rightclick --> context click
double click

key board actions
--------------------
by using send keys 
you can perform keyboard actions

Wait Statements
----------------
Waits are used for synchronization

Synchronizations --> 
lets consider the browser and selenium should works in a same speed 

selenium will gives commands contiuesly to the browser
but browser have lot of dependencies to perform the task

browser depends on the network, browser depends on the application speed
browser depends on application behaviour

Types of waits
-----------------
Implicit wait-->
    implicit wait will apply the wait for all elements 
it can be declared in any one place of scripting 
after that it will apply wait for upcomming elemnets

Explicit wait-->
Explicit wait will have more control where we can use the wait
for particular element in particular condition we can apply the wait statement
wait is applied for particular element not for all the elements


fluent wait

sleep --> static wait, we shouldn't use this


Assignment
--------------
launch the make my trip
check one way is selected
select from and to 
select departure date (1month later from current date)
return date should be 6 month later from the departure date
Select special fares
search

I want to get all the flight name price
departure time and reaching time





