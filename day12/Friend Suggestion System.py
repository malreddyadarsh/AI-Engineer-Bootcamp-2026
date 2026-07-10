#Store two users' friend lists.
#Show common friends.
#Show unique friends for each user.
#Show all friends

friend1={"Adarsh","James","Govardhan","Balu","Manish"}
friend2={"Venkat","Raja","Pavan","Balu","James"}

common_friend=(friend1 & friend2)
print("\nCommon Friends of Friend1 and Friend2 :")
for friend in common_friend:
    print(friend)

unique_friend1=(friend1 - friend2)
print("\n Unique Friends for Friend1 :")
for friend in unique_friend1:
    print(friend)

unique_friend2=(friend2 - friend1)
print("\n Unique Friends for Friend2 :")
for friend in unique_friend2:
    print(friend)

union_friends=friend1.union(friend2) # We can also write | in place of .union
print("\n Showing All Friends :")
for friend in union_friends:
    print(friend)