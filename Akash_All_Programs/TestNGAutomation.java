package firstpackage;
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
import org.testng.annotations.Parameters;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.io.FileNotFoundException;
import java.io.IOException;

public class TestNGAutomation {

	public String baseUrl = "XXX";
	String driverPath = "D:\\ChromeDriver\\chromedriver_win32\\chromedriver.exe";
	public WebDriver driver;
	// WebDriverWait wait = new WebDriverWait(driver,30);
	
	@BeforeTest(groups = { "Akash" })
	public void launchUrl() throws IOException {
		System.setProperty("webdriver.chrome.driver", driverPath);
		driver = new ChromeDriver();
		driver.get(baseUrl);	
	}

	@Test(priority = 1, groups = { "Akash" })
	public void verifyLoginPage() {
		driver.manage().window().maximize();

		// wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//input[@name='username']")));
		driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
		String Title = driver.getTitle();
		System.out.println(Title);
		Assert.assertEquals(Title, "ICyte");
		System.out.println("On Login Page");
		System.out.println();
	}

	@Test(dataProvider = "userpass", priority = 2, groups = { "Akash" }, dependsOnMethods = { "verifyLoginPage" })
	// @Parameters({"user","password"})
	public void verifyHomePage(String user, String password) throws IOException {
		driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
		driver.findElement(By.name("username")).sendKeys(user);
		driver.findElement(By.name("password")).sendKeys((password));
		driver.findElement(By.xpath("//div[contains(text(),'Login')]")).click();
		driver.manage().timeouts().implicitlyWait(20, TimeUnit.SECONDS);
		driver.findElement(By.xpath("//img[contains(@src,'integrichain_logo_header')]")).isDisplayed();
		System.out.println("User is on Home Page");
		driver.findElement(By.xpath("//td[contains(text(),'Logout')]")).click();
		
	}

	@AfterTest
	public void closeBrowser() {
		driver.manage().deleteAllCookies();
		driver.close();
	}


	@DataProvider(name = "userpass")
	public Object[][] getDataFromDataprovider() {
		return new Object[][] { { "YYY.com", "AdminXX4" },
				// { "XXXX", "Adm@XX" },
				// { "Bhupesh", "USA" }
		};

	}

}

