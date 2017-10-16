package Like;

import java.util.List;

import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JPasswordField;
import javax.swing.JTextField;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class LikeMachine {

	public static String phoneNumber= "";
	private static String password = "";
	public static String baseUrl = "https://www.facebook.com/";
	public static String abusedFriend = "";
	public static WebDriver driver;
	
	public static void main(String[] args) {
		GetUsernameOrPhoneNumber();
		GetPassword();
		GetFriend();
		Setup();
		Login();
		SearchForFriend();
		ClickOnFirstFriendResult();
		BlowUpNotificationsWithLikes();
	}
	
	public static void BlowUpNotificationsWithLikes() {
		WebElement currentStatus;
		List<WebElement> unlikedStatuses;
		
		int statuses = 0;
		int statusesAfterScroll = 0;
			while(true){
				
				unlikedStatuses = driver.findElements(By.cssSelector("a[data-testid='fb-ufi-likelink']"));
				for (int i = 0; i < unlikedStatuses.size(); i++) {
					statuses = unlikedStatuses.size();
					currentStatus = (WebElement) unlikedStatuses.toArray()[i];
					ScrollToStatus(currentStatus);
					ClickLikeButton(currentStatus);	
				}
				ScrollDown();
				unlikedStatuses = driver.findElements(By.cssSelector("a[data-testid='fb-ufi-likelink']"));
				statusesAfterScroll = unlikedStatuses.size();
				if(statuses == statusesAfterScroll)
					break;
			}
	}
	public static void ClickOnFirstFriendResult() {
		List<WebElement> friendResults = driver.findElements(By.cssSelector("a[class='_2yet']"));
		WebElement firstResult = (WebElement) friendResults.toArray()[0];
		firstResult.click();
	}
	public static void SearchForFriend() {
		WebElement searchBox = FindElementByCssSelector("input", "data-testid", "search_input");
		searchBox.sendKeys(abusedFriend);
		searchBox.sendKeys(Keys.ENTER);
	}
	public static void ScrollDown() {
		//x,y
		//x -> horizontal
		//y -> vertical
		try {
			Thread.sleep(500);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		JavascriptExecutor js=(JavascriptExecutor)driver;
		js.executeScript("window.scrollBy(0,200);");
	}
	public static void ClickLikeButton(WebElement currentStatus) {
		try {
			Thread.sleep(500);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		JavascriptExecutor js = (JavascriptExecutor)driver;
		js.executeScript("arguments[0].click()", currentStatus);
	}
	public static void ScrollToStatus(WebElement currentStatus) {
		try {
			Thread.sleep(500);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		((JavascriptExecutor) driver).executeScript("arguments[0].scrollIntoView(true);", currentStatus);
	}
	public static void Login() {
		WebElement number = FindElementByCssSelector("input", "type", "email");
		number.sendKeys(phoneNumber);
		
		WebElement pass = FindElementByCssSelector("input", "type", "password");
		pass.sendKeys(password);
		
		WebElement loginBtn = FindElementByCssSelector("input", "value", "Log In");
		loginBtn.click();
	}
	public static void Setup() {
		System.setProperty("webdriver.chrome.driver","C:/chromedriver_win32/chromedriver.exe");
		driver = new ChromeDriver(); 
		driver.get(baseUrl);
		driver.manage().window().maximize();
	}
	
	public static void GetPassword() {
		JPanel panel = new JPanel();
		JLabel label = new JLabel("Enter a password:");
		JPasswordField pass = new JPasswordField(15);
		panel.add(label);
		panel.add(pass);
		String[] options = new String[]{"OK", "Cancel"};
		int option = JOptionPane.showOptionDialog(null, panel, "Facebook password",
		                         JOptionPane.NO_OPTION, JOptionPane.PLAIN_MESSAGE,
		                         null, options, options[0]);
		if(option == 0) // pressing OK button
		{
		    password = new String(pass.getPassword());
		}
	}
	
	public static void GetFriend() {
		JPanel panel1 = new JPanel();
		JLabel label1 = new JLabel("Enter the name of the friend: ");
		JTextField input = new JTextField(30);
		
		panel1.add(label1);
		panel1.add(input);
		String[] options1 = new String[]{"OK", "Cancel"};
		int option1 = JOptionPane.showOptionDialog(null, panel1, "Facebook Friend Name",
		                         JOptionPane.NO_OPTION, JOptionPane.PLAIN_MESSAGE,
		                         null, options1, options1[0]);
		if(option1 == 0) // pressing OK button
		{
		    abusedFriend = input.getText();
		}
	}
	
	public static void GetUsernameOrPhoneNumber() {
		JPanel panel1 = new JPanel();
		JLabel label1 = new JLabel("Enter your facebook email or your phone number: ");
		JTextField input = new JTextField(30);
		
		panel1.add(label1);
		panel1.add(input);
		String[] options1 = new String[]{"OK", "Cancel"};
		int option1 = JOptionPane.showOptionDialog(null, panel1, "Username or Phone Number",
		                         JOptionPane.NO_OPTION, JOptionPane.PLAIN_MESSAGE,
		                         null, options1, options1[0]);
		if(option1 == 0) // pressing OK button
		{
		    phoneNumber = input.getText();
		}
	}
	
	public static WebElement FindElementByCssSelector(String htmlTag, String attribute, String value) {
		WebElement element = null;
		
		String cssSelector = htmlTag + "[" + attribute + "='" + value + "']";
		
		WebDriverWait wait = new WebDriverWait(driver, 100);
		element = wait.until(ExpectedConditions.elementToBeClickable(By.cssSelector(cssSelector)));
		return element;
	}
	public static WebElement FindElementById(String id) {
		WebElement element = null;
		
		WebDriverWait wait = new WebDriverWait(driver, 100);
	
		element = wait.until(ExpectedConditions.elementToBeClickable(By.id(id)));

		return element;
	}

}
