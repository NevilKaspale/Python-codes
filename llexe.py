class Node:
	def __init__(self,data):
		self.__data=data
		self.__next=None
	def  get_data(self):
		return self.__data
	def set_data(self,data):
		self.__data=data
	def get_next(self):
		return self.__next
	def set_next(self,next_node):
		self.__next=next_node

class LinkedList:
	def __init__(self):
		self.__head=None
		self.__tail=None
	def get_head(self):
		return self.__head
	def get_tail(self):
		return self.__tail

	def add(self,data):
		new_node=Node(data)
		if(self.__head==None):
			self.__head=self.__tail=new_node
		else:
			self.__tail.set_next(new_node)
			self.__tail=new_node
	def display(self):
		temp=self.__head
		while (temp is not None):
			print(temp.get_data())
			temp=temp.get_next()

	def oddsum(self):
		sum=0
		temp=self.__head
		while (temp is not None):
			# print(temp.get_data())
			sum=sum+temp.get_data()
			temp=temp.get_next()
			temp=temp.get_next()
		print("Sum of elements at odd position:",sum)




number_list=LinkedList()
number_list.add(2)
number_list.add(5)
number_list.add(7)
number_list.add(8)
number_list.add(10)
number_list.add(69)
number_list.display()
number_list.oddsum()
