package View;
import java.awt.BorderLayout;
import java.awt.Container;
import java.awt.Dimension;
import java.awt.GridLayout;
import javax.swing.*;

import Controller.Controller;
public class GUI  extends JFrame{
private JButton Save;
private JButton FeaturedMemes;
private JButton SelectImage;
private JButton Draw;
private JButton Write;
private JButton Favorite;
private JButton ShareIt;
private JPanel Text;
private JPanel Meme;
private JPanel Controls;
private JTextField TopText;
private JTextField BottomText;
private JButton FavoriteMemes;
private JButton[] Favorites;

private Controller c;
public GUI(Controller c) {
	super("Meme Maker");
	this.c = c;
	Text = new JPanel();
	Meme = new JPanel();
	Controls = new JPanel();
	Save = new JButton();
	FavoriteMemes = new JButton("FavoriteMemes");
	SelectImage = new JButton("");
	Draw = new JButton("");
	Write= new JButton("Write");
	FeaturedMemes = new JButton("Featured Memes");
	Favorite = new JButton("");
	ShareIt = new JButton("");
	TopText = new JTextField();
	BottomText = new JTextField();
	Text.setLayout(new GridLayout(2,1));
	Text.add(TopText);
	Text.add(BottomText);
	Controls.add(Draw);
	Controls.add(Favorite);
	Controls.add(ShareIt);
	Controls.add(Save);	
	Controls.add(FavoriteMemes);
	Controls.add(FeaturedMemes);
	Controls.add(SelectImage);
	Save.setIcon(new ImageIcon("/Users/mohanedmashaly/eclipse-workspace/MemeMaker/src/View/save.png"));
	Draw.setIcon(new ImageIcon("/Users/mohanedmashaly/eclipse-workspace/MemeMaker/src/View/pen.png"));
	Favorite.setIcon(new ImageIcon("/Users/mohanedmashaly/eclipse-workspace/MemeMaker/src/View/love.png"));
	ShareIt.setIcon(new ImageIcon("/Users/mohanedmashaly/eclipse-workspace/MemeMaker/src/View/share.jpg"));
	SelectImage.setIcon(new ImageIcon("/Users/mohanedmashaly/eclipse-workspace/MemeMaker/src/View/cursor.png"));
	Container container = this.getContentPane();	
	container.setLayout(new BorderLayout());
	container.add(Text,BorderLayout.LINE_END);
	container.add(Controls,BorderLayout.PAGE_START);
	this.setSize(new Dimension(1200,1200));
	this.setDefaultCloseOperation(EXIT_ON_CLOSE);
	this.setVisible(true);
}

public JTextField getTopText() {
	return TopText;
}
public void setTopText(JTextField topText) {
	TopText = topText;
}
public JTextField getBottomText() {
	return BottomText;
}
public void setBottomText(JTextField bottomText) {
	BottomText = bottomText;
}
public JButton getSave() {
	return Save;
}
public JButton getFeaturedMemes() {
	return FeaturedMemes;
}
public JButton getSelectImage() {
	return SelectImage;
}
public JButton getDraw() {
	return Draw;
}
public JButton getWrite() {
	return Write;
}
public JButton getFavorite() {
	return Favorite;
}
public JButton getShareIt() {
	return ShareIt;
}
public JButton getFavoriteMemes() {
	return FavoriteMemes;
}
public JButton[] getFavorites() {
	return Favorites;
}
}