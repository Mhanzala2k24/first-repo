 class bb {

 String name;
 String FatherName;
 long grno;
 
 public bb(){
this.name = "MUHAMMAD HANZALA";
this.FatherName = "SHAHBAZ ASLAM";
this.grno = 29;
 }

public bb(String name,String FatherName,long grno){
this.name = name;
this.FatherName = FatherName;
this.grno = grno;
}
public void display(){
    System.out.println("NAME: "+name+"\nFATHER NAME: "+FatherName+"\nGR NO: "+grno);
}

}
