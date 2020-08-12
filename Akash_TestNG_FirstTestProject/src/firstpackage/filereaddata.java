package firstpackage;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.Properties;
import java.util.concurrent.TimeUnit;

import org.apache.commons.io.FileUtils;
import org.apache.log4j.Logger;
import org.apache.log4j.PropertyConfigurator;
import org.openqa.selenium.By;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.annotations.DataProvider;

public class filereaddata {
	
	public String baseUrl = "https://driveqa.davizta.com:6913/davizta/login.html";
	String driverPath = "D:\\ChromeDriver\\chromedriver_win32\\chromedriver.exe";
	public WebDriver driver;
	public WebDriverWait wait;
	Logger logger;
	
	public void browserlaunch() throws IOException {
		System.setProperty("webdriver.chrome.driver", driverPath);
		driver = new ChromeDriver();
		driver.get(baseUrl);
	
		driver.manage().window().maximize();
		//driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
			}

		public String datafetch(String key) throws IOException {
			FileInputStream fis = new FileInputStream("D:\\Eclipse Workplace\\FirstTestProject\\datalocators.properties");
			// create Properties class object to access properties file
			Properties prop = new Properties();
			// load the properties file
			prop.load(fis);
			return prop.getProperty(key);
}
		public boolean explicitwaitIsElementDisplayed(String locator,WebDriver driver) {
			
			wait = new WebDriverWait(driver,30);
			return wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath(locator))).isDisplayed();
		}
		
		
		public void loginit (String message) {
			logger=  Logger.getLogger("firstTestNGfile");
			PropertyConfigurator.configure("log4j.properties");
			logger.info(message);
			}
		
		public void screenshot(String filename,WebDriver driver) throws IOException {
			
			TakesScreenshot ts=(TakesScreenshot)driver;
			File source= 	ts.getScreenshotAs(OutputType.FILE);
			File DestFile = new File("./Screenshots/"+filename+".png");
			FileUtils.copyFile(source, DestFile); 
			}
		
		@DataProvider(name = "userpass")
		public Object[][] getDataFromDataprovider() {
			return new Object[][] { { "agupta_a@davizta.com", "Admin@1234" },
					// { "agupta_m@davizta.com", "Admin@1234" },
					// { "Bhupesh", "USA" }
			};
		}

}

		//***********************************************************************************************
		

