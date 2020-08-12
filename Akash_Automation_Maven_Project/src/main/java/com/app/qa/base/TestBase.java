package com.app.qa.base;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Properties;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

import com.app.qa.utils.TestUtils;

public class TestBase {

	public static WebDriver driver;
	public Properties prop;

	public String datafetch(String key) throws IOException {
		//try {
			
			FileInputStream fis = new FileInputStream("D:\\Eclipse Workplace\\Automation\\src\\main\\java\\com\\app\\qa\\config\\config.properties");
			// create Properties class object to access properties file
			Properties prop = new Properties();
			// load the properties file
			prop.load(fis);
		//} //catch (FileNotFoundException e) {
			///e.printStackTrace();
		//} //catch (IOException e) {
			//e.printStackTrace();

//}
		return prop.getProperty(key);
	}
	
	public  void initialization() throws IOException {
		String browsername = datafetch("browser");
		//String browsername = prop.getProperty("browser");
		if (browsername.equals("chrome")) {
			System.setProperty("webdriver.chrome.driver", "D:\\ChromeDriver\\chromedriver_win32\\chromedriver.exe");
			driver = new ChromeDriver();
		} else if (browsername.equals("firefox")) {
			System.setProperty("webdriver.gecko.driver", "D:\\ChromeDriver\\chromedriver_win32\\chromedriver.exe");
			driver = new FirefoxDriver();
		}

		driver.manage().window().maximize();
		driver.manage().deleteAllCookies();
		driver.manage().timeouts().pageLoadTimeout(TestUtils.PAGE_LOAD_TIMEOUT, TimeUnit.SECONDS);
		driver.manage().timeouts().implicitlyWait(TestUtils.IMPLICIT_WAIT, TimeUnit.SECONDS);

		driver.get(datafetch(("url")));

	}
}
