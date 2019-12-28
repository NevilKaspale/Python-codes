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
	def find_node(self,data):
		count=0
		temp=self.__head
		while (temp !=None):
			if(temp.get_data()==data):	
				return temp
			count += 1
			# print(count,"node/s traversed")
			temp=temp.get_next()
		return None
	def insert(self,data,data_before):
		new_node=Node(data)
		if(data_before==None):
			new_node.set_next(self.__head)
			self.__head=new_node
			if(new_node.get_next()==None):
				self.__tail=new_node
		else:
			m=node_before=self.find_node(data_before)
			if(node_before is not None):
				new_node.set_next(node_before.get_next())
				node_before.set_next(new_node)
				if(new_node.get_next()is None):
					self.__tail=new_node
			else:
				print(data_before,"is not present in the Linked List")

	def delete(self,data):
		node=self.find_node(data)
		if(node is not None):
			if(node==self.__head):
				if(self.__head==self.__tail):
					self.__tail=None
				self.__head=node.get_next()
			else:
				temp=self.__head
				while(temp is not None):
					if(temp.get_next()==node):
						temp.set_next(node.get_next())
						if(node==self.__tail):
							self.__tail=temp
						node.set_next(None)
						break
					temp=temp.get_next()
		else:
			print(data,"is not present in Linked List")
					
number_list=LinkedList()
while(True):
	d=int(input("1.add 2.insert 3.delete 4.display 5.exit\n"))
	if(d==1):
		ele=input("Element to be added")
		number_list.add(ele)
		number_list.display()
	elif(d==2):
		ele=input("Element to be inserted")
		prev=input("Element to be inserted after")
		number_list.insert(ele,prev)
		number_list.display()
	elif(d==3):
		ele=input("Element to be deleted")
		number_list.delete(ele)
		number_list.display()
	elif(d==4):
		number_list.display()
	elif(d==5):
		break
	else:
		print("Enter proper number")

# number_list.add(2)
# number_list.add(5)
# number_list.add(7)
# number_list.add(8)

# number_list.display()
# found=number_list.find_node(8)
# if(found is None):
# 	print('not found')
# else:
# 	print('found')

# number_list.insert(6,5)
# number_list.display()
# print(".....................................")
# number_list.delete(6)
# number_list.display()
