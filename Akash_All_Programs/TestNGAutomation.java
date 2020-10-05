package firstpackage;
import org.apache.log4j.Logger;
import org.apache.log4j.PropertyConfigurator;
import org.apache.commons.exec.util.*;
import org.apache.commons.io.FileUtils;
import org.apache.commons.exec.*;
import org.apache.commons.exec.launcher.*;
import java.io.File;
import java.io.FileInputStream;
import java.util.Properties;
import java.util.concurrent.TimeUnit;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
import org.testng.annotations.AfterSuite;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.BeforeSuite;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Listeners;
import org.testng.annotations.Parameters;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;


@Listeners(firstpackage.TestNGListeners.class)

public class TestNGAutomation   {
	
	public String baseUrl = "https://driveqa.davizta.com:6913/davizta/login.html";
	String driverPath = "D:\\ChromeDriver\\chromedriver_win32\\chromedriver.exe";
	public WebDriver driver;
	Logger logger;
	//***********************************************************************************************
	public void explicitwaitIsElementDisplayed(String locator) {
		WebDriverWait wait = new WebDriverWait(driver,30);
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath(locator)));
	}
	//****************************************************************************************

	
	public void loginit (String message) {
		logger=  Logger.getLogger("firstTestNGfile");
		PropertyConfigurator.configure("log4j.properties");
		logger.info(message);
		}

	public void screenshot(String filename) {
		try {
		TakesScreenshot ts=(TakesScreenshot)driver;
		File source= 	ts.getScreenshotAs(OutputType.FILE);
		File DestFile = new File("./Screenshots/"+filename+".png");
		FileUtils.copyFile(source, DestFile);
		} catch (IOException e) {
			e.printStackTrace();
	}
	}
	
	public String datafetch(String key) throws IOException {
		FileInputStream fis = new FileInputStream("D:\\Eclipse Workplace\\FirstTestProject\\datalocators.properties");
		// create Properties class object to access properties file
		Properties prop = new Properties();
		// load the properties file
		prop.load(fis);
		return prop.getProperty(key);
	}
	
	
	@BeforeTest(groups = { "Akash" })
	public void launchUrl() throws IOException {
		System.setProperty("webdriver.chrome.driver", driverPath);
		driver = new ChromeDriver();
		driver.get(baseUrl);
	
		driver.manage().window().maximize();
		//driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
		system.out.println("Hello Akash 4");
			}
	

	@Test(priority = 1, groups = { "Akash" })
	public void verifyLoginPage() throws Exception{
		
		// wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//input[@name='username']")));
		loginit("Getting Page Title");
		String Title = driver.getTitle();
		System.out.println(Title);
		loginit("Verifying Page Title");
		Assert.assertEquals(Title, "ICyte");
		System.out.println("On Login Page");
		screenshot("LoginPage");
		System.out.println("Screenshot Taken");
		loginit("User is present on Login Page");

		
	}

	@Test(dataProvider = "userpass", priority = 2, groups = { "Akash" }, dependsOnMethods = { "verifyLoginPage" })
	//@Parameters({"user","password"})
	public void verifyHomePage(String user, String password) throws IOException {
		loginit("Page is Loading");
		explicitwaitIsElementDisplayed("//div[contains(text(),'Login')]");
		loginit("Page is loaded");
		
		loginit("Entering user name");
		WebElement email = driver.findElement(By.name(datafetch("Username")));
		email.sendKeys(user);
		
		//driver.findElement(By.name("username")).sendKeys(user);
		loginit("Entering Password");
		WebElement pass = driver.findElement(By.name(datafetch("Password")));
		pass.sendKeys(password);
		
		loginit("Clicking on login");
		WebElement Login = driver.findElement(By.xpath(datafetch("Login")));
		Login.click();
		explicitwaitIsElementDisplayed("//div[contains(text(),'Compare Snapshot')]");
		
		driver.findElement(By.xpath("//img[contains(@src,'integrichain_logo_header')]")).isDisplayed();
		System.out.println("User is on Home Page");
		
		screenshot("HomePage");
		loginit("Clicking on Logout");
		driver.findElement(By.xpath("//td[contains(text(),'Logout')]")).click();
	
		
	}

	@AfterTest
	public void closeBrowser() {
		driver.manage().deleteAllCookies();
		loginit("Closing browser");
		driver.close();
	}


	@DataProvider(name = "userpass")
	public Object[][] getDataFromDataprovider() {
		return new Object[][] { { "agupta_a@davizta.com", "Admin@1234" },
				// { "agupta_m@davizta.com", "Admin@1234" },
				// { "Bhupesh", "USA" }
		};
	}

}
