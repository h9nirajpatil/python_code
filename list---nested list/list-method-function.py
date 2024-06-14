
###########################LIST METHOD/FUCTION###################################################
#min()
#max()
#sort()
#count()
#reverse()
#index()


#min() #max() #sort():---- they should have same type of values.
# #
# # mylist=[10,20,30,40,50]
# # print("largest number",max(mylist))
# # print("smallest number",min(mylist))
# #
# # fruits=['apple','guava','litchi']
# # print("largest number",max(fruits))
# # print("smallest number",min(fruits))
# #
# # #sort():----- arrange the data in ascending (small to big)
# # list1=[100,90,80,70,45,32]
# # list1.sort()
# print(list1)
#
# #descending order
# list1.sort(reverse=True)
# print(list1)
#
#
# num=[10,20,30,30,30,900]
# print("Count the number of 30 in list:-",num.count(30))
# print("Index of 10 :",num.index(10))


#print the list in reverse direction
num=[10,20,30,30,30,900]
for i in range(0,len(num),1):
    if ( num[i] == 30):
        print("Index of 30 are:",i)



#print the list in reverse direction
num.reverse()
print(num)

print("sum od values:-",sum(num))








