package Controller;
import View.GUI;
public class Controller {
private GUI l ;
public Controller() {
l = new GUI(this);	
}
public static void main(String[]args) {
new Controller();
}
}
