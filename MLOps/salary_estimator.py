from sklearn.externals import joblib
simple_linear=joblib.load("salary model.pk1")
multi_linear=joblib.load("multi_linear.pk1")


print("\t\t\t welcome to my tools:")
print("\t\t\t --------------------")
print()
while True:
	print("""\t Press 1: salary predict 
	 Press 2: House selling price prediction
	 Press 3 : Exit
""")

	print("Enter your choice",end=" ")
	ch=int(input())

	if ch==1:
		print("Enter your Exp:",end=" ")
		experience=float(input())
		print("Predicted salary:",simple_linear.predict(experience)[0])
	if ch==2:
		print("Enter your Avg. Area Income",end=" ")
		income=float(input())
		
		print("Avg. Area House Age",end=" ")
		age=float(input())
		
		print("Avg. Area Number Of Rooms",end=" ")
		rooms=float(input())
		
		print("Avg. Area Number Of Bedrooms",end=" ")
		bedrooms=float(input())
		
		print("Area Population",end=" ")
		population=float(input())
		print("Expected House Salary:",multi_linear.predict([[income,age,rooms,bedrooms,population]]))

	if ch==3:
		exit()
	input("Enter to continue.....")