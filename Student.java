public class Student {
 String name;
 int age;
public Student(String name){
    this(name,18);
}
public Student(String name,int age){
    this.name = name;
    this.age = age;
}
void display(){
    System.out.println("NAME: "+name+"\nAGE: "+age);
}
}
