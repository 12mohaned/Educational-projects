package Model;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;

import javax.imageio.ImageIO;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JPanel;

import java.awt.Image;
import Model.Meme;
public class Engine {
private int Featured_counter;
private ArrayList<JButton> Featured;
public Engine() {
Featured = new ArrayList<JButton>();	
}
/* 
 * this method responsible for loading the featured memes from the local drive where the loop add the images in Featured ArrayList*/
private void loadFeaturedMemes() throws IOException {
Featured_counter = new File("/Users/mohanedmashaly/eclipse-workspace/MemeMaker").list().length;
File[] Memespath = new File("/Users/mohanedmashaly/eclipse-workspace/MemeMaker").listFiles();
	for(int i =0; i < Featured_counter;i++) {
		String Image = Memespath[i].getName();
		File FileToRead = new File("/Users/mohanedmashaly/eclipse-workspace/MemeMaker/"+Image);
		Image Meme = ImageIO.read(FileToRead);
		JButton B = new JButton();
		B.setIcon(new ImageIcon(Meme));
		Featured.add(B);
}
}
public ArrayList<JButton> getFeatured(){
return Featured;	
}
}
