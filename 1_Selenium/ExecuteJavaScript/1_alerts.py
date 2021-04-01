from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="../../chromedriver.exe")
driver.get('http://google.com')
driver.implicitly_wait(3)

# js = 'alert( "Hello World" );'
# it's another way to print alert
#
# js = '''
# var name = "Mark";
# window.alert(name);
# '''

js = '''
var name = "Mark";
newWindow = window.open("", "myWindow", "width=200,height=100");  
newWindow.document.write("<p>name</p>");
newWindow.close();

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}  
await sleep(2000);

name = "Ace";
newWindow = window.open("", "myWindow", "width=200,height=100");  
newWindow.document.write("<p>name</p>");
newWindow.close();  
'''


# You can declare a variable in one statement, leaving it undefined. Then you can assign a
# value to it in a later statement, without declaring it again.
var nationality;
nationality = "U.S.";
