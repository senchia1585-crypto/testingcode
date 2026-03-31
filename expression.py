# programmer intro to expression
# interger Is the number ever that is 1000 /-1000 that is call interger
print(2+100) # interger can + by print commad
A=print(2+100) # print again the assigment of equaltion will become 
#none because print is function that will print the result but not return the result to A
print(100.900 + 100.00)
B=print(100.900 + 100.00)
print(f"Total number of : {A} + {B}  ")
 # this call float that means that is number with decimal point
print("Hello"+ " " + "World")
A=105+1
B=100.999+100.999
C=A+B
# cannot use print to express the equaltion 
#because print is function that will print the result but not return the result to A and B
print(f"Total number of : {C}")



# "" for string that means use this "" mark anything can be string 
# string cannot add with number  will become logic error
# True and False can be dentify in boolean  that is an unit or special thing in code

# print(False) 

pop=True
pop_2=False
print(f"{pop} or {pop_2} ")
# print(True)
import time
print("Please make a choice....")
time.sleep(3)
print("Do you believe in GOD? You only got two option please make your choice within 3 seconds.....")
time.sleep(3)
input=input("PLEASE CHOOSE TRUE OR FALSE: ")
if input=="True":
    print("Thank your believe in GOD.")
elif input=="False":
    print("Oh! Bro you don't believe in GOD, I am sorry about that")
    print("You should choose True, because God is the best thing in the world, if you don't believe in God, you will be lost in the world")
else:
    time.sleep(3)
    print("............")
    time.sleep(5)
    print("I am sorry about that, you only got two option, please choose again")


#False=not True
   # pop_sound=not True
   # print(f"{pop_sound}")


# this is while loop that mean when x is less than 10 will keep run the code inside while loop
# assignment statement
view_of_jason = 2
jason_view="Youtube" # view of jason channel on youtube
print(jason_view +"is the good social media platform")
print("jason today had view"+" "+str(view_of_jason))  
# str() is function that can convert interger or float to string1
view=view_of_jason
no_view=view_of_jason
# view_of_jason is interger that cannot use not function
print(view)
print(no_view)
jack_view=6
total_view=jack_view + view_of_jason
print("Both people's total view today is"+" "+ str(total_view))
# str function can convert interger to string and then can add togerther with string
good_quality_of_jason_channel=True
bad_quality_of_jason_channel=False
print(not good_quality_of_jason_channel)
print(str(not bad_quality_of_jason_channel)+","+ "Jason channel is bad quality")
# let str covert the boolean function to string and then add with string to make a sentence
x=100
x="99"
print(99==x)
if 99==x:
    print("x is True")
elif x=="99": # this is elif statement that mean if the first condition is not true then will check the second condition
     print("x is the string 99 not a number")
else: # else if all above condition not suitable will run this code
    print("x is False")



    


