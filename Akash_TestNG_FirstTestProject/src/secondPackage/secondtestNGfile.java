
package secondPackage;
import java.io.FileInputStream;
import java.util.Properties;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.io.FileNotFoundException;
import java.io.IOException;

public class secondtestNGfile {
	
	public static String baseUrl = "https://driveqa.davizta.com:6913/davizta/login.html";
    static String driverPath = "D:\\ChromeDriver\\chromedriver_win32\\chromedriver.exe";
    public static WebDriver driver ; 
	  //WebDriverWait wait = new WebDriverWait(driver,30);
	
	public static void main(String[] args) throws IOException {

		launchUrl_verifyLoginPage_verifyHomePage();	
	}
	  
  public static void launchUrl_verifyLoginPage_verifyHomePage() throws IOException {
	  FileInputStream fis = new FileInputStream("D:\\Eclipse Workplace\\FirstTestProject\\datalocators.properties");
		// create Properties class object to access properties file
		Properties prop = new Properties();
		// load the properties file
		prop.load(fis);
    System.setProperty("webdriver.chrome.driver",driverPath);
	  driver = new ChromeDriver();
	  driver.get(baseUrl);
	  driver.manage().window().maximize();
	  
	  //wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//input[@name='username']")));
	  driver.manage().timeouts().implicitlyWait(10,TimeUnit.SECONDS);
	 String Title =  driver.getTitle();
	 System.out.println(Title);
	 Assert.assertEquals(Title, "ICyte");
	 System.out.println("On Login Page");

	  driver.manage().timeouts().implicitlyWait(10,TimeUnit.SECONDS);
	  driver.findElement(By.name(prop.getProperty("Username"))).sendKeys("agupta_a2@davizta.com");
	  driver.findElement(By.name(prop.getProperty("Password"))).sendKeys(("Admin@1234"));
	  driver.findElement(By.xpath(prop.getProperty("Login"))).click();
	  driver.manage().timeouts().implicitlyWait(20,TimeUnit.SECONDS);
	  driver.findElement(By.xpath(prop.getProperty("img"))).isDisplayed();
	  System.out.println("User is on Home Page");
	  driver.manage().deleteAllCookies();
	  driver.close();
  }
  
}
