public class hogwarts{
String name;
int age;
int house;
boolean pure;
public hogwarts(String name,int age , int house , boolean pure){
this.name = name;
this.age = age;
this.house = house;
this.pure = pure;
}
public String getname(){
return name;
}
public int age(){
return age;
}
public String Gethouse(){
String x = " ";
switch(this.house){
case 1 : x = "a";break;
case 2 : x = "b";break;
case 3: x  = "c";break;
case 4 : x = "d";break;
}
return x;
}
public String getpure()
{
if (pure == true)
return "pure"; 
else {
return "muggle";
}
}
public static void main(String[]args){
hogwarts a = new hogwarts("harry potter",18,4,true);
System.out.println(a.Gethouse());
}
}