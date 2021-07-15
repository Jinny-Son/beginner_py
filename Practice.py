
#a="  Welcome   to the Paradise     !   "

#print(a.strip())
#print(a.replace("t","A"))#대문자 소문자 구별함 


#b= "Hello, World"
#print(b.split(","))

a="astronut"
b="in the ocean"
c= a+b #띄어쓰기 반영 안됨 
print(c)

c=a+" "+b #반드시 스페이스 눌러야만 사이에 공간이 생김 ""는 안됨
print(c)

age=28
txt = " My name is Jinny, I am {}" #숫자와 글자는 함께 연성하지 못하므로 {}를 사용해서 format을 사용해준다 

print(txt.format(age))

