import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.safari.*;
import java.util.*;
public class Launch {
	public static void main(String[]args) 
	{
	Set<String> Problems_Solved = new HashSet<String>();
	WebDriver Safari_Driver = new SafariDriver(); 
	Safari_Driver.get("https://uhunt.onlinejudge.org/api/subs-user/1019081");
	String S = Safari_Driver.findElement(By.tagName("Problem ID")).getText();
	S = S.substring(S.indexOf('[')+1);
	StringTokenizer st = new StringTokenizer(S," ");
	
	int counter =0;
	String Problem_ID = "";
	String[]L  = null;
	while(st.hasMoreTokens()) 
	{
	String Token = st.nextToken();
	L = Token.split(",");
	}
	if(!L.equals(null)) 
	for(int i=0; i < L.length;i++) {
	if(counter == 6) {
	counter = 0;	
	}
	else {
	if(counter == 1) {
	Problem_ID = L[i];	
	}
	else 
	{
	if(counter == 2) {
	if(Integer.parseInt(L[i]) == 90){
	Problems_Solved.add(Problem_ID);	
	}
	}	
	}
	counter++;
	}
	}
	System.out.println(Problems_Solved);
	}
}

